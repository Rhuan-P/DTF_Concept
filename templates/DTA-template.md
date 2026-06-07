# DTA — Documento Técnico de Aceitação

**Projeto**: [Nome do Projeto]  
**Contexto**: [.dtc/context.md](../.dtc/context.md)  
**Requisito/Implementação**: [Link para DTR e DTI, ou ID da feature]  
**Versão**: [Versão do Documento]  
**Data**: [Data de Criação]  
**Autor**: [Nome do Autor]  
**Status**: [Rascunho | Em Revisão | Aprovado]

---

## 1. Visão Geral da Aceitação

### 1.1 Feature para Validação
[Ex: "Autenticação OAuth2 Social (Google + GitHub)"]

### 1.2 Objetivo de Validação
Definir critérios objetivos para validar que a implementação atende aos requisitos do DTR e segue os padrões arquiteturais do projeto.

### 1.3 Escopo da Validação
| Inclusivo | Exclusivo |
|-----------|------------|
| OAuth2 flow completo (Google + GitHub) | SMS authentication |
| Account linking across providers | SAML/OIDC flows (for another DTR) |
| Token exchange and encryption | Social login via other providers (LinkedIn, etc.) |

---

## 2. Critérios de Aceitação (Acceptance Criteria)

### AC-001: OAuth2 Flow Completo para Google

**Requisito do DTR**: Implementar autenticação com Google OAuth2  
**Cenário de teste**: Usuário visita página de login e clica em "Login com Google"

| Step | Expected Behavior | Priority |
|------|-------------------|----------|
| 1. Click on "Login with Google" button | Redirects to https://accounts.google.com/o/oauth2/v2/auth with correct parameters | P0 |
| 2. User accepts terms on consent screen | Redirects back to /auth/callback/google with code parameter | P0 |
| 3. Backend exchanges code for tokens | Returns access_token, refresh_token, expires_at | P0 |
| 4. Google user info fetched successfully | Response contains email, name, picture, sub (user ID) | P0 |
| 5. User account created/linked | Database shows correct google_provider_id or link entry | P0 |

**Acceptance test**: 
```bash
# Manual test in browser:
1. Visit https://your-app.com/login
2. Click "Login with Google"
3. Consent screen appears (Google identity)
4. Accept terms
5. Redirect to /login?token=xxx&email=user@gmail.com&name=User Name
6. Session created, user redirected to dashboard

Expected: Dashboard shows user profile with correct information
```

---

### AC-002: OAuth2 Flow Completo para GitHub

**Cenário de teste**: Usuário clica em "Login com GitHub"

| Step | Expected Behavior | Priority |
|------|-------------------|----------|
| 1. Click on "Login with GitHub" button | Redirects to https://github.com/login/oauth/authorize | P0 |
| 2. User accepts terms on GitHub consent screen | Redirects back to /auth/callback/github with code parameter | P0 |
| 3. Backend exchanges code for tokens | Returns access_token, refresh_token | P0 |
| 4. GitHub user info fetched successfully | Response contains login (email), name, avatar_url | P0 |
| 5. User account created/linked | Database shows correct github_provider_id or link entry | P0 |

**Acceptance test**: Same flow as Google OAuth2 but using GitHub identity provider.

---

### AC-003: Single Sign-On Across Sessions

**Cenário de teste**: Usuário faz login com Google, depois fecha e abre novo navegador

| Step | Expected Behavior | Priority |
|------|-------------------|----------|
| 1. User logs in with Google OAuth2 | Session created in system | P0 |
| 2. User closes browser and opens new one | Clicks "Login with Google" again, gets redirected to consent screen (if first use) or no redirect (if already logged in) | P1 |

**Technical requirement**:
- Cookie must be HttpOnly, Secure, SameSite=Strict
- Session stored in Redis/DB for persistence across browser sessions
- Session TTL: 7 days minimum

---

### AC-004: Account Linking (Multiple Providers)

**Cenário de teste**: Usuário cria conta com Google, depois faz login com GitHub

| Step | Expected Behavior | Priority |
|------|-------------------|----------|
| 1. User signs up via Google OAuth2 | User created with google_provider_id set | P0 |
| 2. User logs in with GitHub OAuth2 | Same user account linked to GitHub provider (if email matches) | P0 |
| 3. UI shows all linked providers | Profile page lists both Google and GitHub as login options | P1 |

**Edge case handling**:
- If email addresses don't match across providers, require explicit link action
- Prevent linking same provider twice (e.g., two Google accounts)

---

### AC-005: Error Handling & Fallback

**Cenário de teste 1**: Google OAuth2 flow fails (user cancelled consent)

| Step | Expected Behavior | Priority |
|------|-------------------|----------|
| 1. User cancels on consent screen | Redirects to /login with error message "Please complete authentication" | P0 |
| 2. Error message visible and user-friendly | Message: "Cancelou a autenticação com Google"? Clique novamente para tentar de novo. | P0 |

**Cenário de teste 2**: OAuth token exchange fails

| Step | Expected Behavior | Priority |
|------|-------------------|----------|
| 1. Token exchange returns error (invalid code, expired) | Redirects to /login with error message "Autenticação falhou" | P0 |
| 2. User can retry authentication | Same OAuth flow repeats | P0 |

---

### AC-006: Security - PKCE Implementation

**Requisito**: Implementar PKCE conforme RFC7636 Section 4.1.3

| Test Case | Expected Behavior | Priority |
|-----------|-------------------|----------|
| PKCE code challenge generated (S256) | Code challenge in auth URL is base64url(SHA256(code_verifier)) | P0 |
| Invalid code verifier rejected | Access denied if code_verifier doesn't match during exchange | P0 |
| State parameter validated | CSRF attack prevented via state nonce validation | P0 |

**Acceptance test**: 
```python
import httpx
# Test that auth URL contains PKCE parameters:
response = requests.get(f"{base_url}/login?auth=google")
assert "code_challenge_method=S256" in str(response.url)
assert "code_challenge=" in str(response.url)

# Attempt auth without PKCE:
requests.post("http://localhost:8000/auth/callback/google", 
    params={"code": "invalid_code", "state": "test"})
# Should return 403 Forbidden (CSRF protection)
```

---

### AC-007: Security - Token Encryption

**Requisito**: OAuth tokens encrypted at rest conforme DTC NFR requirements

| Test Case | Expected Behavior | Priority |
|-----------|-------------------|----------|
| Access token stored encrypted in database | DB shows encrypted token (not plaintext) | P0 |
| Refresh token encrypted if present | Same as access token | P0 |
| Token decryption requires secure key file | Missing /secure/tokens.key raises RuntimeError at startup | P0 |
| No plaintext tokens in logs or memory dumps | Scan of logs/memory shows no base64url tokens | P1 |

**Manual verification**:
```bash
# Check that access token column is encrypted in DB:
SELECT google_provider_id, 
       (access_token_encrypted IS NOT NULL) as token_exists,
       LEFT(access_token_encrypted, 10) as token_prefix  # Should be base64 encoded
FROM users WHERE google_provider_id IS NOT NULL;

# Expected output:
# google_provider_id | token_exists | token_prefix
# 123e4567...        | t            | UGFzZX... (base64 starts with uppercase)
```

---

### AC-008: Performance - OAuth Flow Latency

**Requisito**: Auth flow completes within performance targets (NFR-001)

| Metric | Target | Acceptance Threshold | Priority |
|--------|--------|---------------------|----------|
| Initial redirect time | <50ms | >50ms fails | P0 |
| Consent screen load time | <200ms | >200ms warning | P1 |
| Auth completion p95 | <5 seconds | >10s fails | P0 |

**Acceptance test**: 
```bash
# Run 10 auth flows, measure total time:
start_time=$(date +%s.%N)
curl -sI "https://your-app.com/login?auth=google"
# Redirect to Google consent screen
echo "Y" | sleep 5  # Accept consent manually
wait_for_redirect() { while curl -sI "http://localhost:8000/" 2>/dev/null; do sleep 1; done; }
end_time=$(date +%s.%N)
echo "Total time: $(echo "$end_time - $start_time" | bc)"

# Run in loop and calculate p95:
for i in {1..100}; do
    curl -sI "http://localhost:8000/login?auth=google" >> /tmp/auth_times.txt
done
p95=$(sort /tmp/auth_times.txt | awk 'NR == int(95*length($0)/100) {print $1}')
echo "p95 completion time: ${p95}s"
```

---

### AC-009: Scalability - Concurrent Auth Requests

**Requisito**: Handle concurrent auth requests without degradation (NFR-004)

| Test Case | Expected Behavior | Priority |
|-----------|-------------------|----------|
| 1000 concurrent OAuth2 callbacks | No errors, no timeout failures | P0 |
| Redis cache handles state management | No duplicate auth URLs for same session | P1 |

**Acceptance test**: 
```bash
# Load test with wrk:
wrk -t4 -c100 -d30s "http://localhost:8000/login?auth=google"
# Check that all 4 threads complete without Redis queue buildup
redis-cli --scan type "oauth_state" | wc -l  # Should show manageable count
```

---

### AC-010: Accessibility - WCAG 2.1 AA Compliance

**Requisito**: Auth UI meets WCAG 2.1 AA standards (NFR-005)

| Test Case | Expected Behavior | Priority |
|-----------|-------------------|----------|
| Color contrast ratio for auth buttons | ≥4.5:1 on all backgrounds | P1 |
| Keyboard navigation possible through login flow | Tab key works, Enter submits forms | P1 |
| Screen reader announces page changes properly | NVDA/VoiceOver reads login button correctly | P2 |

**Acceptance test**: 
```bash
# Automated color contrast check:
node -e 'const colors = require("colors"); console.log(colors.cyan("Run axe-core against /login"));'

# Manual keyboard test:
# 1. Open browser with keyboard only (no mouse)
# 2. Tab through login buttons
# 3. Verify "Login with Google" focus and Enter key works

# Screen reader test:
# 1. Enable NVDA in browser
# 2. Load /login page
# 3. Check that "Login with Google" is announced correctly
```

---

## 3. Checklist de Testes Completos

### 3.1 Unit Tests (>80% coverage do módulo auth/)

- [ ] test_google_oauth_get_auth_url() - Happy path test
- [ ] test_github_oauth_get_auth_url() - Happy path test  
- [ ] test_token_encryption_encrypt_decrypt_cycle()
- [ ] test_pkce_code_challenge_generation()
- [ ] test_oauth_state_nonce_validation()
- [ ] test_user_service_create_from_google_provider()
- [ ] test_user_service_link_existing_user()
- [ ] test_auth_session_expiry_logic()
- [ ] Total coverage: ______% (target >80%)

### 3.2 Integration Tests

- [ ] test_full_oauth_flow_happy_path_with_mocked_providers()
- [ ] test_account_linking_across_multiple_sessions()
- [ ] test_pkce_csrf_protection_without_valid_state()
- [ ] test_token_exchange_failure_handling()
- [ ] test_redis_state_management_under_concurrent_load()
- [ ] test_database_schema_migration_applied_successfully()

### 3.3 Security Tests (Internal Penetration Testing)

- [ ] CSRF prevention validation (no session fixation)
- [ ] Token encryption validated (no plaintext in DB dump)
- [ ] Rate limiting on auth endpoints (no DoS possible)
- [ ] Secure headers present: Content-Security-Policy, X-Frame-Options
- [ ] HTTPOnly cookies set for sessions

### 3.4 Performance Tests

- [ ] p95 latency <5s for auth flow
- [ ] No memory leaks under sustained load (100 concurrent users)
- [ ] Redis cache hit rate >95% for state management
- [ ] Database query execution time <50ms average

### 3.5 Accessibility Tests

- [ ] Axe-core reports 0 violations on /login page
- [ ] Keyboard-only login flow completes successfully
- [ ] Screen reader (NVDA/VoiceOver) reads login correctly

---

## 4. Plano de Rollout e Monitoramento

### 4.1 Feature Flag Implementation

```python
from fastapi import Request, Response

def enable_social_auth_feature():
    """Enable social auth based on feature flag and rollout schedule."""
    is_feature_enabled = request.headers.get("X-Feature-Social-Auth", "false") == "true"
    
    if not is_feature_enabled:
        # Fall back to traditional login (existing auth logic)
        return Response(
            status_code=302,
            headers={
                "Location": "/auth/login?fallback=true",  # Redirect to legacy login
            }
        )
```

### 4.2 Monitoring Events

| Event Name | Description | Alert Threshold | Priority |
|------------|-------------|-----------------|----------|
| `auth.auth_started` | OAuth flow initiated | - | P2 |
| `auth.auth_success` | Auth completed successfully | - | P1 |
| `auth.auth_failure` | Auth failed (any reason) | >1% failure rate | P0 |
| `auth.oauth.token_exchange_failed` | Token exchange API error | Any failures → alert | P0 |
| `auth.account_creation_failed` | User creation/linking error | >0.1% failure rate | P0 |

### 4.3 Observability Implementation

```python
# Add to src/auth/auth_controller.py
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

@router.get("/social/{provider}")
async def init_oauth_flow(
    provider: str,
    request: Request,
    db: AsyncSession,
) -> Response:
    """Initiate OAuth2 authentication flow."""
    
    with tracer.start_as_current_span("oauth.auth_started", kind=SpanKind.SERVER) as span:
        span.set_attribute("auth.provider", provider)
        span.set_attribute("auth.session.id", request.session.get("session_id"))
        
        try:
            # ... implementation logic ...
            
            span.set_status(TraceStatusStatus.SET_STATUS_OK)
            return auth_url
            
        except Exception as e:
            span.record_exception(e)
            span.set_status(TraceStatusStatus.SET_STATUS_ERROR)
            raise
```

### 4.4 Rollout Schedule

| Phase | Percentage of Traffic | Duration | Success Criteria |
|-------|----------------------|----------|------------------|
| Feature flag off (maintenance window) | 0% | 2 hours post-deploy | All existing features work, no regressions |
| Phase 1: Internal team only | 5% | 1 week | Auth flow works for internal users, p95 latency <5s |
| Phase 2: Beta users (sign-up required) | 20% | 2 weeks | Beta NPS >7 for new feature, no P0 incidents |
| Phase 3: All users | 100% | After validation complete | Full validation passed, security review approved |

---

## 5. Document Review Checklist

### 5.1 DTA Review Items

- [ ] Todos critérios de aceitação claramente definidos?
- [ ] Acceptance tests são executáveis (manual ou automatizado)?
- [ ] Performance targets alinhados com arquitetura (.dtc/context.md)?
- [ ] Security requirements implementados conforme NFR do DTC?
- [ ] Checklist de testes completo e realístico?

### 5.2 DTI Review Items

- [ ] Code implementation aligned with DTI specifications?
- [ ] Database schema migrations applied correctly?
- [ ] Unit tests passing (>80% coverage)?
- [ ] Integration tests passing in staging?

---

## 6. Aprovações Necessárias

### 6.1 Tech Lead Review

- [ ] Arquiteto/Tech Lead: _____________________ Date: ____
  - ✅ Arquitetura alinhada com .dtc/architecture.md
  - ✅ Código segue padrões de código (.dtc/context.md section 4.1)
  - ✅ Design decisões documentadas (seus comentários nos commits)

### 6.2 Security Review

- [ ] Security Reviewer: _____________________ Date: ____
  - ✅ Token encryption implemented correctly
  - ✅ PKCE CSRF protection validated
  - ✅ Rate limiting configured appropriately
  - ✅ No sensitive data in logs

### 6.3 DevOps/Infrastructure Approval

- [ ] DevOps Engineer: _____________________ Date: ____
  - ✅ Database migrations can be run without downtime
  - ✅ Redis configuration supports state management
  - ✅ Environment variables (GOOGLE_OAUTH_CLIENT_ID, etc.) documented
  - ✅ Monitoring dashboards created with alert rules

### 6.4 Product Owner Validation

- [ ] Product Owner: _____________________ Date: ____
  - ✅ Feature delivers on business value (NPS >7 for new feature)
  - ✅ Rollout schedule acceptable to stakeholders
  - ✅ User-facing documentation updated

---

## 7. Referência de Validação Completa

### 7.1 Executar Testes Manuais

```bash
# Test flow manual acceptance criteria:
echo "=== OAuth2 Auth Flow Acceptance Testing ==="

# Google OAuth2 happy path test:
echo "Step 1: Navigate to login page..."
curl -sI "http://localhost:8000/login?auth=google" | head -5

echo "Step 2: Accept consent (manual action required)..."
echo "Open browser, click 'Login with Google', accept terms..."

echo "Step 3: Verify redirect and session creation..."
curl -s "http://localhost:8000/login/callback?code=AUTH_CODE_HERE" | grep -i "session\|dashboard"
```

### 7.2 Executar Testes Automatizados

```bash
# Run automated acceptance tests:
pytest --acceptance-auth-oauth \
       tests/acceptance/test_oauth_flow.py \
       tests/security/test_token_encryption.py \
       tests/performance/test_auth_latency.py::test_oauth_p95_latency_under_5s
```

### 7.3 Verificar Monitoramento

```bash
# Check monitoring for new events:
grep "auth.auth_started" /var/log/app/auth_events.log | tail -20
grep "auth.auth_failure" /var/log/app/auth_events.log | head -5
```

---

## 8. Rollback Plan (se necessário)

| Scenario | Rollback Action | Time Required |
|----------|-----------------|---------------|
| Auth flow failures >5% | Disable feature flag, revert to legacy login | <5 min |
| Token encryption error | Revert migration, use legacy token storage temporarily | <10 min |
| Performance degradation (>10s p95) | Kill auth workers, scale up before re-enabling | <2 min |

**Rollback command**: 
```bash
curl -X POST "http://localhost:8000/api/feature-flag/social-auth?value=false"
```

---

> **"Este DTA valida que a implementação OAuth2 social atende aos requisitos do projeto."**  
> Referências: [DTR-feature-auth-001](../.dtc/tasks/auth/DTR-feature-auth-001.md), [.dtc/context.md](../.dtc/context.md)
