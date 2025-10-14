# Host in the cloud

**As a** DevOps engineer
**I need** the system to be hosted in the cloud
**So that** it is easier to manage and scale in comparison to on-premises solutions

### Details and Assumptions
* Unix-like operating system
* Configured containerized environment

### Acceptance Criteria     
```gherkin
Given the cloud infrastructure is available and accessible
When the deployment process is initiated
Then the system should be successfully deployed to the cloud
    And the system should be accessible through the configured endpoints
    And resources should automatically scale based on load
```
