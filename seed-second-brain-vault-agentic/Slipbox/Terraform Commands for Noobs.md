# Commands

A quick reference guide for the most commonly used Terraform commands.

## Basic Workflow

### Initialize Terraform
```bash
terraform init
```
Downloads providers and modules. Run this first in any new Terraform directory.

### Format Code
```bash
terraform fmt
```
Auto-formats `.tf` files to follow standard conventions.

### Validate Configuration
```bash
terraform validate
```
Checks if your configuration is syntactically valid.

### Preview Changes
```bash
terraform plan
```
Shows what resources will be created, modified, or destroyed without making changes.

### Apply Changes
```bash
terraform apply
```
Creates/updates infrastructure. Prompts for confirmation before proceeding.

### Apply Without Confirmation
```bash
terraform apply -auto-approve
```
Applies changes without asking for `yes` confirmation (use carefully!).

### Destroy All Resources
```bash
terraform destroy
```
Deletes all resources managed by Terraform. Prompts for confirmation.

## Working with Outputs

### Show All Outputs
```bash
terraform output
```
Displays all output values from your configuration.

### Show Specific Output
```bash
terraform output bucket_name
```
Shows just the value of `bucket_name` output.

### Show Raw Output (No Quotes)
```bash
terraform output -raw bucket_name
```
Useful for piping to other commands or scripts.

## Working with State

### List All Resources
```bash
terraform state list
```
Shows all resources in the state file.

### Show Resource Details
```bash
terraform state show aws_s3_bucket.my_bucket
```
Displays detailed information about a specific resource.

### Remove Resource from State (Without Destroying)
```bash
terraform state rm aws_s3_bucket.my_bucket
```
Removes from Terraform management but keeps the actual resource in AWS.

### Pull Current State
```bash
terraform state pull
```
Downloads and displays the current state file (useful for debugging).

## Targeted Operations

### Plan Specific Module
```bash
terraform plan -target=module.storage
```
Shows changes only for the `storage` module.

### Apply Specific Module
```bash
terraform apply -target=module.storage
```
Creates/updates only the `storage` module resources.

### Apply Multiple Modules
```bash
terraform apply -target=module.triggers -target=module.storage
```
Applies changes to multiple specified modules.

### Destroy Specific Module
```bash
terraform destroy -target=module.analytics
```
Destroys only the `analytics` module resources.

### Preview Destruction of Specific Module
```bash
terraform plan -destroy -target=module.analytics
```
Shows what would be destroyed without actually destroying it.

## Working with Variables

### Set Variable via Command Line
```bash
terraform apply -var="environment=prod"
```
Overrides variable values from the command line.

### Use Variable File
```bash
terraform apply -var-file="production.tfvars"
```
Uses a specific `.tfvars` file instead of the default `terraform.tfvars`.

## Workspaces

### List Workspaces
```bash
terraform workspace list
```
Shows all available workspaces (environments).

### Create New Workspace
```bash
terraform workspace new staging
```
Creates and switches to a new workspace.

### Switch Workspace
```bash
terraform workspace select dev
```
Switches to an existing workspace.

### Show Current Workspace
```bash
terraform workspace show
```
Displays the currently active workspace.

## Import Existing Resources

### Import Resource into State
```bash
terraform import aws_s3_bucket.my_bucket my-bucket-name
```
Imports an existing AWS resource into Terraform management.

## Debugging and Troubleshooting

### Enable Detailed Logging
```bash
export TF_LOG=DEBUG
terraform apply
```
Shows detailed debug output (set to `TRACE` for even more detail).

### Disable Logging
```bash
unset TF_LOG
```
Turns off debug logging.

### Force Unlock State
```bash
terraform force-unlock [LOCK_ID]
```
Manually unlocks state if a previous operation crashed.

### Refresh State
```bash
terraform refresh
```
Updates state file with real infrastructure status (rarely needed with modern Terraform).

## Graph and Visualization

### Generate Dependency Graph
```bash
terraform graph | dot -Tpng > graph.png
```
Creates a visual dependency graph (requires Graphviz installed).

## Module-Specific Commands (GroundSense Project)

### Deploy Order (With Dependencies)
```bash
# 1. IAM user and permissions
terraform apply -target=module.iam

# 2. Lambda functions and event handlers
terraform apply -target=module.triggers

# 3. Storage (S3, DynamoDB)
terraform apply -target=module.storage

# 4. Data ingestors
terraform apply -target=module.ingestors

# 5. Analytics (Glue, Athena)
terraform apply -target=module.analytics
```

### Destroy Order (Reverse Dependencies)
```bash
# 1. Destroy analytics (no dependencies on it)
terraform destroy -target=module.analytics

# 2. Destroy ingestors (depends on storage)
terraform destroy -target=module.ingestors

# 3. Destroy storage (depends on triggers)
terraform destroy -target=module.storage

# 4. Destroy triggers (no dependencies on it)
terraform destroy -target=module.triggers

# 5. Destroy IAM (no dependencies on it)
terraform destroy -target=module.iam
```

## Common Patterns

### Plan and Save for Later
```bash
terraform plan -out=tfplan
terraform apply tfplan
```
Saves the plan to a file, then applies exactly that plan.

### Show Saved Plan
```bash
terraform show tfplan
```
Displays the contents of a saved plan file.

### Apply Only Resource Additions
```bash
terraform plan -target=module.storage
# Review, then apply
terraform apply -target=module.storage
```
Careful incremental deployment.

## Tips

- **Always run `terraform plan` before `apply`** to preview changes
- **Use `-target` carefully** - it can lead to inconsistent state if misused
- **Commit your `.tf` files to git** but never commit `terraform.tfstate` or `.tfvars` with secrets
- **Use workspaces** for managing multiple environments (dev/staging/prod)
- **Lock your provider versions** in `terraform { required_providers { ... } }` block
