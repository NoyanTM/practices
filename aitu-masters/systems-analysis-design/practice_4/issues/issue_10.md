# Automate deployment of new changes to the cloud

**As a** Developer
**I need** automation to deploy new changes to the cloud
**So that** I can quickly publish updates without manual interventions to production or testing environment

### Details and Assumptions
* Version control system (e.g., Git) and hosting service (GitHub)
* Configured CI/CD pipeline connected via SSH to the cloud environment

### Acceptance Criteria

```gherkin
Given a developer commits and pushes new code changes to the repository
When the CI/CD pipeline is triggered
Then the build and test stages should run automatically
    And if all checks pass, the system should deploy the new version to the cloud
    And the production environment should reflect the latest changes
    And a deployment log should be available for review
```
