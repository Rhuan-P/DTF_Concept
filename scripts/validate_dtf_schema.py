import os
import sys

def validate_schema():
    # Mandatory sections for different types
    schema_requirements = {
        ".dtc": [
            "Project Overview", "System Architecture", "Tech Stack", "Patterns", 
            "Directory Structure", "Design Principles", "Integrations", 
            "Security", "Performance", "Maintainability", "System Evolution", 
            "Architectural Decisions", "Risks", "Review/Approval", "Appendices"
        ],
        ".dtr": [
            "Requirements Overview", "Functional Requirements (RF)", 
            "Non-Functional Requirements (NFR)", "Technical Context", 
            "Restrictions/Assumptions", "Full Workflow", "Technical Decisions", 
            "Performance/Security", "Implementation Plan", "Test Plan", 
            "Rollout/Monitoring", "Acceptance Checklist"
        ],
        ".dta": [
            "Acceptance Overview", "Acceptance Criteria (AC)", 
            "Test Checklist", "Rollout/Monitoring", "Observability Instrumentation", 
            "Document Review Checklist"
        ],
        ".dti": [
            "Technical Implementation details", "Code Snippets", 
            "Diagrams"
        ]
    }

    violations = []
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if any(file.startswith(marker) for marker in [".dtc", ".dtr", ".dta", ".dti"]):
                # Determine the type based on the prefix
                file_type = None
                for marker in [".dtc", ".dtr", ".dta", ".dti"]:
                    if file.startswith(marker):
                        file_type = marker
                        break
                
                if file_type:
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            required_sections = schema_requirements[file_type]
                            for section in required_sections:
                                if section not in content:
                                    violations.append(f"Missing '{section}' in {path}")
                    except Exception as e:
                        violations.append(f"Could not read {path}: {str(e)}")

    if violations:
        print("Validation failed:")
        for v in violations:
            print(f"- {v}")
        sys.exit(1)
    else:
        print("All schemas validated successfully.")

if __name__ == "__main__":
    validate_schema()
