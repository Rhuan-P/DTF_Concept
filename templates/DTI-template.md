# DTI — Documento Técnico de Implementação

**Projeto**: [Nome do Projeto]  
**Contexto**: [.dtc/context.md](../.dtc/context.md)  
**Requisito**: [Link para DTR relevante, ou criar DTR separado]  
**Versão**: [Versão do Documento]  
**Data**: [Data de Criação]  
**Autor**: [Nome do Autor]  
**Status**: [Rascunho | Em Revisão | Aprovado]

---

## 1. Visão Geral da Implementação

### 1.1 Tarefa de Implementação
[Ex: "Implementar autenticação OAuth2 com Google e GitHub conforme DTR-feature-auth-001"]

### 1.2 Abordagem Técnica Escolhida
[Descreva a abordagem técnica para implementar este requisito.]

```markdown
# Abordagem escolhida:
- Usar FastAPI OAuth2PasswordBearer + authlib para OAuth flows
- Implementar PKCE padrão RFC7636 via python-josejwt
- Async database access with SQLAlchemy Core 2.0 for efficiency
- Redis cache for state management between OAuth redirects

# Por que esta abordagem?
1. FastAPI já possui suporte nativo a OAuth2 (OAuth2PasswordBearer)
2. Authlib fornece implementações robustas de OAuth2 flows
3. python-josejwt para criptografia JWT e PKCE code challenges
4. Redis é padrão do projeto (de .dtc/context.md)

# Alternativas consideradas:
- Flask-OAuthlib: Descontinuído, não tem suporte moderno a OAuth2
- passport.js (Node): Não usamos Node.js no projeto
```

---

## 2. Estrutura de Código

### 2.1 Organização por Feature/Feature-Type

```
src/
├── auth/                    # Nova pasta para feature de autenticação social
│   ├── __init__.py
│   ├── config.py            # OAuth configs (client_id, client_secret)
│   ├── google_oauth.py      # Google OAuth2 implementation
│   ├── github_oauth.py      # GitHub OAuth2 implementation
│   ├── auth_controller.py   # Main controller for auth flow
│   └── session_handler.py   # Session state between redirects
│
├── database/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # User model (existing)
│   │   └── oauth_account.py # New: OAuth account linking model
│   └── migrations/          # SQL migration files for schema changes
│
├── services/
│   ├── __init__.py
│   ├── user_service.py      # Create/link users logic
│   └── session_service.py   # Session management service
│
├── api/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py   # /auth/* endpoints
│   │   └── callback_routes.py # OAuth callback handlers
│   └── middleware/
│       └── security_headers.py # Security headers middleware
│
├── utils/
│   ├── __init__.py
│   ├── token_encryption.py  # Token encryption utilities
│   └── oauth_helpers.py     # PKCE helper functions
│
└── tests/
    ├── unit/
    │   ├── auth/
    │   │   ├── test_google_oauth.py
    │   │   ├── test_github_oauth.py
    │   │   └── test_auth_flow.py
    │   └── session/
    │       └── test_session_handler.py
    └── integration/
        ├── test_oauth_full_flow.py
        └── test_account_linking.py
```

### 2.2 Diagrama de Arquitetura da Implementação
```mermaid
graph TD
    A[User Agent] -->|1. Init OAuth| B[/auth/social/{provider}]
    B -->|2. Generate auth URL| C[AuthController]
    C -->|3. Redirect| D[OAuth Provider Consent Screen]
    D -->|4. Authorization Code| B
    B -->|5. Exchange for tokens| E[token_exchange_service]
    E -->|6. Create user/link account| F[user_service]
    F -->|7. Save to DB| G[(PostgreSQL)]
    E -->|8. Refresh token| H[Redis cache]
    
    I[Security Layer] -.->|Validate PKCE| B
    I -.->|Encrypt tokens| E
```

---

## 3. Implementação Detalhada

### 3.1 OAuth2 Configuração (config.py)

```python
"""OAuth2 configuration for social authentication."""

from typing import TypedDict

class OAuthConfig(TypedDict):
    client_id: str
    client_secret: str
    redirect_uri: str
    scopes: list[str]

# Google OAuth2 config
google_oauth: OAuthConfig = {
    "client_id": os.getenv("GOOGLE_OAUTH_CLIENT_ID"),
    "client_secret": os.getenv("GOOGLE_OAUTH_CLIENT_SECRET"),
    "redirect_uri": os.getenv("OAUTH_REDIRECT_URI", "/auth/callback/google"),
    "scopes": ["email", "profile"],  # Required scopes for user identification
}

# GitHub OAuth2 config
github_oauth: OAuthConfig = {
    "client_id": os.getenv("GITHUB_OAUTH_CLIENT_ID"),
    "client_secret": os.getenv("GITHUB_OAUTH_CLIENT_SECRET"),
    "redirect_uri": os.getenv("OAUTH_REDIRECT_URI", "/auth/callback/github"),
    "scopes": ["user"],  # Minimum scope for GitHub auth
}

def get_oauth_config(provider: str) -> OAuthConfig:
    """Get OAuth configuration by provider name."""
    configs = {
        "google": google_oauth,
        "github": github_oauth,
    }
    return configs.get(provider)
```

---

### 3.2 PKCE Helper Functions (utils/oauth_helpers.py)

```python
"""PKCE helper functions for OAuth2 flows."""

import secrets
import base64
import json
from typing import TypedDict
from datetime import datetime, timedelta


class OAuthState(TypedDict):
    """OAuth state object for session management."""
    code_verifier: str
    state_nonce: str
    provider: str
    redirect_after_auth: str | None


def generate_code_challenge() -> tuple[str, str]:
    """Generate S256 code challenge per RFC7636.
    
    Returns:
        Tuple of (code_challenge, code_verifier)
    """
    # Generate random bytes for code verifier
    code_verifier = base64.urlsafe_b64encode(
        secrets.token_bytes(32)  # 256 bits
    ).decode().rstrip("=")
    
    # Create SHA256 hash of verifier for challenge
    import hashlib
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).decode().rstrip("=")
    
    return (code_challenge, code_verifier)


def create_oauth_state(provider: str) -> OAuthState:
    """Create OAuth state object for session."""
    state_nonce = secrets.token_urlsafe(32)
    
    return {
        "code_verifier": None,  # Will be set after login
        "state_nonce": state_nonce,
        "provider": provider,
        "redirect_after_auth": os.getenv("OAUTH_RETURN_URL", "/dashboard"),
    }
```

---

### 3.3 Google OAuth Implementation (auth/google_oauth.py)

```python
"""Google OAuth2 authentication implementation."""

import httpx
from fastapi import APIRouter, Request, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_

from ..config import google_oauth
from ..database.models.user import User


class GoogleOAuth:
    """Handles Google OAuth2 authentication flow."""
    
    def __init__(self, db_session: AsyncSession):
        self.db = db_session
    
    async def get_auth_url(self) -> str:
        """Generate authorization URL for Google OAuth."""
        state = create_oauth_state("google")
        
        auth_params = {
            "client_id": google_oauth["client_id"],
            "redirect_uri": google_oauth["redirect_uri"],
            "response_type": "code",
            "scope": " ".join(google_oauth["scopes"]),
            "access_type": "offline",  # Get refresh token
            "prompt": "consent",  # Force consent screen
            "state": state["state_nonce"],  # Anti-CSRF token
        }
        
        # Add PKCE code challenge
        import base64, hashlib, secrets
        code_verifier = secrets.token_urlsafe(32)
        code_challenge = base64.urlsafe_b64encode(
            hashlib.sha256(code_verifier.encode()).digest()
        ).decode().rstrip("=")
        
        auth_params["code_challenge_method"] = "S256"
        auth_params["code_challenge"] = code_verifier
        
        return f"https://accounts.google.com/o/oauth2/v2/auth?{'&'.join(f'{k}={v}' for k, v in auth_params.items())}"
    
    async def exchange_code_for_token(
        self, 
        code: str,
        code_verifier: str
    ) -> dict[str, str]:
        """Exchange authorization code for tokens."""
        
        payload = {
            "code": code,
            "client_id": google_oauth["client_id"],
            "client_secret": google_oauth["client_secret"],
            "grant_type": "authorization_code",
            "redirect_uri": google_oauth["redirect_uri"],
            "code_verifier": code_verifier,
        }
        
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://oauth2.googleapis.com/token",
                data=payload,
                headers=headers,
            )
            
            if response.status_code != 200:
                raise ValueError(f"Failed to exchange token: {response.text}")
            
            return response.json()
    
    async def get_google_user_info(self, access_token: str) -> dict:
        """Fetch Google user profile with access token."""
        
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
        }
        
        response = httpx.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers=headers,
        )
        
        if response.status_code != 200:
            raise ValueError("Failed to fetch Google user info")
        
        return response.json()
```

---

### 3.4 GitHub OAuth Implementation (auth/github_oauth.py)

Similar to GoogleOAuth but using GitHub's API endpoint. Key differences:
- GitHub uses `/login/oauth/authorize` instead of Google's consent screen
- Token exchange at `https://github.com/login/oauth/access_token`
- GitHub user info at `/user` endpoint

```python
# GitHub OAuth implementation (similar structure to GoogleOAuth)
async def get_github_auth_url(self):
    """Generate authorization URL for GitHub OAuth."""
    state = create_oauth_state("github")
    
    auth_params = {
        "client_id": github_oauth["client_id"],
        "redirect_uri": github_oauth["redirect_uri"],
        "scope": " ".join(github_oauth["scopes"]),
        "state": state["state_nonce"],
        # GitHub doesn't require prompt parameter
    }
    
    return f"https://github.com/login/oauth/authorize?{'&'.join(f'{k}={v}' for k, v in auth_params.items())}"
```

---

### 3.5 Auth Controller (auth/auth_controller.py)

Main controller handling OAuth flow:

```python
"""Auth controller for OAuth2 social login flows."""

from fastapi import APIRouter, Request, Response, Query
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta
import uuid

from ..config import google_oauth, github_oauth
from .google_oauth import GoogleOAuth
from .github_oauth import GitHubOAuth


router = APIRouter()


class AuthState:
    def __init__(self):
        self.states = {}  # In production: Redis or database-backed session store
    
    async def save_state(self, provider: str) -> str:
        """Save OAuth state for current session."""
        nonce = str(uuid.uuid4())
        state_data = create_oauth_state(provider)
        
        # Store in session/Redis
        self.states[nonce] = state_data
        
        return nonce


oauth_state_store = AuthState()


@router.get("/social/{provider}")
async def init_oauth_flow(
    provider: str,
    request: Request,
    db: AsyncSession
) -> str:
    """Initiate OAuth2 authentication flow."""
    
    # Generate OAuth state
    nonce = await oauth_state_store.save_state(provider)
    
    # Get appropriate OAuth config
    if provider == "google":
        google_oauth_instance = GoogleOAuth(db)
        auth_url = google_oauth_instance.get_auth_url()
    elif provider == "github":
        github_oauth_instance = GitHubOAuth(db)
        auth_url = await github_oauth_instance.get_auth_url()
    else:
        raise ValueError(f"Unsupported OAuth provider: {provider}")
    
    return Response(
        redirect_url=auth_url,
        headers={
            "Cache-Control": "no-cache",
            "X-Request-ID": str(uuid.uuid4()),
        }
    )
```

---

### 3.6 Database Schema Changes (migrations/001_user_oauth_accounts.sql)

```sql
-- Migration: Add OAuth account linking support to users table
-- See: .dtc/architecture.md for full architecture context
-- DTI-feature-auth-001

-- Step 1: Add new columns to existing users table
ALTER TABLE users
ADD COLUMN google_provider_id UUID,
ADD COLUMN github_provider_id UUID,
ADD COLUMN oauth_state TEXT,
ADD COLUMN last_auth_timestamp TIMESTAMP WITH TIME ZONE;

COMMENT ON COLUMN users.google_provider_id IS 'Google OAuth account ID if linked';
COMMENT ON COLUMN users.github_provider_id IS 'GitHub OAuth account ID if linked';

-- Step 2: Create user_oauth_accounts linking table
CREATE TABLE IF NOT EXISTS user_oauth_accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    provider VARCHAR(50) NOT NULL CHECK (provider IN ('google', 'github')),
    provider_account_id VARCHAR(255),
    access_token_encrypted TEXT NOT NULL,  -- Encrypted with Fernet
    refresh_token_encrypted TEXT,
    expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    CONSTRAINT unique_user_provider UNIQUE (user_id, provider)
);

COMMENT ON TABLE user_oauth_accounts IS 'Link OAuth provider accounts to users';
COMMENT ON COLUMN user_oauth_accounts.provider_account_id IS 'Provider-specific account ID';

-- Step 3: Create auth audit events table for compliance
CREATE TABLE IF NOT EXISTS auth_audit_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type VARCHAR(50) NOT NULL CHECK (event_type IN (
        'auth_started', 'auth_completed', 'auth_failed', 
        'token_exchanged', 'account_created', 'account_linked'
    )),
    user_id UUID REFERENCES users(id),
    ip_address INET,
    user_agent TEXT,
    provider VARCHAR(50),
    auth_error_code TEXT,
    details JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    INDEX idx_auth_event_time (created_at DESC)
);

-- Step 4: Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_oauth_accounts_user ON user_oauth_accounts(user_id);
CREATE INDEX IF NOT EXISTS idx_oauth_accounts_provider ON user_oauth_accounts(provider);
CREATE INDEX IF NOT EXISTS auth_events_created_at ON auth_audit_events(created_at DESC);
```

---

### 3.7 Token Encryption Service (utils/token_encryption.py)

```python
"""Token encryption utility for OAuth tokens."""

from cryptography.fernet import Fernet
import os
from contextlib import contextmanager


@contextmanager
def get_encryption_key():
    """Context manager for loading encryption key."""
    key_file_path = Path("/secure/tokens.key")  # Not in repo!
    
    try:
        with open(key_file_path, "rb") as f:
            key = f.read()
    except FileNotFoundError:
        raise RuntimeError("OAuth token encryption key not found!")
    yield Fernet(key)


def encrypt_token(token: str) -> str:
    """Encrypt OAuth token for storage."""
    with get_encryption_key() as fernet:
        encrypted = fernet.encrypt(token.encode())
        return base64.urlsafe_b64encode(encrypted).decode()


def decrypt_token(encrypted: str) -> str:
    """Decrypt OAuth token from storage."""
    with get_encryption_key() as fernet:
        decrypted = fernet.decrypt(base64.urlsafe_b64decode(encrypted + "==")).decode()
        return decrypted
