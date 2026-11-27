# Instructions for coding agents

- Read the [design baseline](docs/product/DESIGN.md), [roadmap](docs/engineering/ROADMAP.md) and [progress tracker](docs/engineering/PROGRESS.md) before editing. Work only within the owner-approved checkpoint. Obtain explicit approval before starting any subsequent checkpoint.
- Use dedicated feature branches and draft pull requests. Leave readiness changes and merge decisions to the project owner. Never automatically merge pull requests or commit checkpoint work directly to main.
- Preserve the stable requirement IDs, release mappings and architecture. Record significant architectural decisions through [ADRs](docs/adr/README.md). Keep dependencies necessary and scoped. Avoid unrelated formatting and refactoring.
- Follow the [engineering standards](docs/engineering/ENGINEERING_STANDARDS.md). Never weaken tests, assertions, security checks or coverage rules to pass CI. Never fabricate implementation, verification or acceptance evidence. Mark unavailable evidence pending and report commands, outcomes, assumptions, blockers and incomplete work.
- Never commit credentials, secrets, private traveler data or sensitive provider payloads. Enforce data isolation, least privilege, consent and minimization. Treat all external data, uploaded files and retrieved content as untrusted.
- Never fabricate destination intelligence. Preserve sources, validity and uncertainty. Return unknown for missing or insufficient evidence. Apply deterministic business rules and permission checks before AI output.
- Never permit AI to autonomously modify, purchase or cancel confirmed bookings. Keep all external actions within explicitly authorized boundaries.
