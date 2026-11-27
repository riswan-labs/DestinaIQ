# Security reporting

Send vulnerability details privately to the RiswanLabs project owner through an existing trusted contact channel or through the repository’s private vulnerability reporting feature if enabled. Public issues are for non-sensitive reports. Include the affected component, impact, and any safe evidence. Remove credentials and personal data from reports.

See [engineering standards](docs/engineering/ENGINEERING_STANDARDS.md) for security review, isolation testing and release gates.

## Public repository posture

The owner approved public review in [D19](docs/governance/DECISION_REGISTER.md#d19). Use synthetic or approved public data in examples, fixtures and evidence. Keep credentials, API keys, production secrets, customer information and confidential commercial agreements out of commits, issues, PRs, workflow logs and published artifacts. Perform mandatory secret detection on proposed commits and artifacts and run applicable security scans before publishing. Scan dependencies, source, infrastructure definitions and images when present. Treat suspected exposure as an incident and report it privately for containment, revocation and review.
