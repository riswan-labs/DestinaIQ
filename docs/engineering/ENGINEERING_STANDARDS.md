# Engineering standards

These are mandatory engineering gates for future implementation and releases. Checkpoint 0.1 establishes the standards and records documentation verification.

| Gate | Required evidence |
| --- | --- |
| Backend tests | At least 90% automated backend production-code coverage with 95% stretch. Publish line and branch results and review substantive uncovered paths. Never exclude substantive code or weaken assertions to raise coverage. Approve the exact threshold metric before CI enforcement. |
| Acceptance | 100% of required acceptance tests pass. Include positive, negative and failure-path tests. |
| Security | Zero unresolved critical findings. High-risk findings require documented approval, mitigation, owner and review date. Run dependency and secret scanning and relevant security tests. |
| Authorization | Demonstrate object and tenant isolation, unauthorized access rejection, consent and revocation for security-sensitive functionality. |
| Database | Verify clean install, upgrade from supported prior state, data preservation and rollback or approved forward recovery. Exercise restore at release. |
| API | Validate request and response contracts, authorization, compatibility, error behavior and failure handling. |
| Environments | Pin tooling and dependencies and prove reproducible setup and CI from a clean environment. |
| Operations | Verify product SLOs at agreed load, monitoring, fallback, rollback and restore. Bind provenance and coverage gates to production release. |

Tie evidence to requirement IDs and the actual commit. Use the [traceability register](TRACEABILITY.md) and [release gates](../product/RELEASE_STRATEGY.md). Document exceptions, owners, mitigation and deadlines. Keep pending tests visible until independently verified.

## Review boundaries

Each PR has a single logical purpose, explicit measurable acceptance criteria, requirement and checkpoint mappings, and command-level evidence. Split substantial checkpoint work into independently reviewable PRs. Keep unrelated checkpoints in separate PRs. Obtain owner approval for any material scope expansion or checkpoint consolidation. Record assumptions, blockers, architectural deviations and pending evidence. Only the project owner can approve checkpoint acceptance. Merging is a separate owner-controlled action.

## Security verification

Detect secrets before pushing proposed changes or publishing artifacts. Run security scans applicable to the changed content, including dependencies, source, infrastructure and images when present. Capture scope and results and require these checks in implementation CI. Use negative and failure-path tests for security-sensitive authorization, tenant and user isolation, consent and recovery. Resolve all critical findings and obtain explicit project-owner approval for each unresolved high-risk exception. Never weaken checks, inflate coverage or fabricate evidence. Keep all restricted information out of the public repository.
