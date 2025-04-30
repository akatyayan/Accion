# Accion

## Dockerfile for nginx 1.19 Explanation ###

Removed attempts to chown /var/log/nginx and /var/cache/nginx — these are owned by root and required by NGINX internally.

NGINX continue using those as root (Alpine nginx still runs as root inside container for master process, but worker processes run as nginx).

still serving your content (e.g., /var/www/html) as a non-root user.

Security Best Practices Followed:

✅ Alpine base image	Reduces size and surface area
✅ Fixed version (1.19)	Avoids surprises from rolling updates
✅ Non-root user	Limits privilege escalation risks
✅ Metadata labels	For tracking and audit
✅ Clean and minimal	No extra packages or tools


### Kubernetes Explanation ####

✅ StatefulSet:- 	   Ensures stable hostname, storage, and ordered deployment.
✅ PVC:- 	           Each pod gets its own persistent volume for stateful data.
✅ Headless Service:-   Needed for StatefulSets to assign DNS and identity.
✅ Resource Limits:-    Prevent resource hogging, define compute boundaries.
✅ Non-root User :- 	   Best practice for container security.



## Text Manipulation Problem Explanation ##


✅ grep:- 	Extracts lines with keywords (ERROR/WARNING)
✅ sed:- 	Redacts IPs and emails for privacy
✅ tr:-  	Converts all characters to lowercase
✅ awk:- 	Extracts the log level field and summarizes counts



## Detailed Explanation of the CI/CD Pipeline ##

Let me walk you through each component of this deployment pipeline:
1. GitHub Actions Workflow
The GitHub Actions workflow I've created handles the entire CI/CD process and is triggered by:

Code pushes to main/master branches
Pull requests targeting main/master
Manual triggers with environment selection

2. Build Job
Purpose: Create the Docker image and store it in a registry.

Docker Buildx: Sets up an enhanced Docker build environment
Container Registry Authentication: Logs into GitHub Container Registry
Metadata Extraction: Creates appropriate tags for your image
Build and Push: Builds the Docker image with caching and pushes it to the registry

3. Security Scanning Job
Purpose: Ensure the image is secure before deployment.

Trivy Scanner: Scans the image for vulnerabilities and uploads results to GitHub Security
Hadolint: Checks the Dockerfile for best practices and potential issues
Gitleaks: Scans the codebase for accidentally committed secrets

4. Config Validation Job
Purpose: Validate Kubernetes manifests before applying them.

Kubeval: Ensures your Kubernetes YAML files conform to the Kubernetes schema

5. Staging Deployment Job
Purpose: Deploy to a staging environment for testing.

kubectl Setup: Configures kubectl with your cluster credentials
Image Update: Updates the image tag in the deployment manifest
Deployment: Applies Kubernetes manifests to the staging namespace
Verification: Confirms the deployment was successful with health checks

6. Production Deployment Job
Purpose: Safely deploy to production with a canary strategy.

Canary Deployment: First deploys a canary instance with the new version
Validation Period: Waits to ensure the canary performs well
Full Deployment: Updates the main deployment and removes the canary
Verification: Confirms production deployment success
Notification: Sends deployment status to Slack


Prerequisites and Setup
To use this pipeline, you'll need:

GitHub Repository: With your Nginx application code
Kubernetes Cluster: Running and accessible
GitHub Secrets: 

KUBECONFIG:  Kubernetes config for accessing the cluster
SLACK_WEBHOOK: For notifications