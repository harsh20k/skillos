# Commands

A quick reference guide for the most commonly used AWS CLI commands.

## Initial Setup

### Install AWS CLI
```bash
# macOS
brew install awscli

# Linux
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Windows - download installer from AWS website
```

### Configure AWS CLI (First Time)
```bash
aws configure
```
You'll be prompted for:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-east-1`)
- Default output format (e.g., `json`)

### Configure with Named Profile
```bash
aws configure --profile my-profile
```
Creates a separate profile for different AWS accounts/users.

### View Current Configuration
```bash
aws configure list
```
Shows your current AWS CLI settings.

### Test Your Configuration
```bash
aws sts get-caller-identity
```
Returns your user ID, account ID, and ARN (confirms authentication works).

## Managing Profiles

### List All Profiles
```bash
cat ~/.aws/credentials
```
Shows all configured profiles.

### Use Specific Profile
```bash
aws s3 ls --profile my-profile
```
Runs command with a specific profile.

### Set Default Profile for Session
```bash
export AWS_PROFILE=my-profile
```
All subsequent commands use this profile until terminal closes.

### Switch Regions for Single Command
```bash
aws s3 ls --region us-west-2
```
Overrides default region for one command.

## S3 Commands

### List All Buckets
```bash
aws s3 ls
```
Shows all S3 buckets in your account.

### List Contents of a Bucket
```bash
aws s3 ls s3://my-bucket-name/
```
Shows files/folders in the bucket root.

### List Contents Recursively
```bash
aws s3 ls s3://my-bucket-name/ --recursive
```
Shows all files including subdirectories.

### Upload a File to S3
```bash
aws s3 cp /path/to/local/file.txt s3://my-bucket-name/
```
Copies local file to S3 bucket root.

### Upload to Specific Path
```bash
aws s3 cp /path/to/local/file.txt s3://my-bucket-name/folder/subfolder/
```
Uploads to a specific S3 "folder" (prefix).

### Upload Directory Recursively
```bash
aws s3 cp /path/to/local/folder/ s3://my-bucket-name/folder/ --recursive
```
Uploads entire directory and its contents.

### Download File from S3
```bash
aws s3 cp s3://my-bucket-name/file.txt /path/to/local/
```
Downloads file to local directory.

### Download Directory Recursively
```bash
aws s3 cp s3://my-bucket-name/folder/ /path/to/local/ --recursive
```
Downloads entire S3 prefix to local directory.

### Sync Local to S3 (Like rsync)
```bash
aws s3 sync /path/to/local/folder/ s3://my-bucket-name/folder/
```
Only uploads new/changed files (efficient for backups).

### Sync S3 to Local
```bash
aws s3 sync s3://my-bucket-name/folder/ /path/to/local/folder/
```
Downloads only new/changed files from S3.

### Delete File from S3
```bash
aws s3 rm s3://my-bucket-name/file.txt
```
Deletes a single file.

### Delete All Files in Bucket
```bash
aws s3 rm s3://my-bucket-name/ --recursive
```
Deletes all objects in bucket (bucket itself remains).

### Move/Rename File in S3
```bash
aws s3 mv s3://my-bucket-name/old-name.txt s3://my-bucket-name/new-name.txt
```
Moves or renames an S3 object.

## IAM Commands

### List IAM Users
```bash
aws iam list-users
```
Shows all IAM users in your account.

### Create IAM User
```bash
aws iam create-user --user-name my-new-user
```
Creates a new IAM user.

### Create Access Keys for User
```bash
aws iam create-access-key --user-name my-new-user
```
Generates access key ID and secret for the user.

### List Access Keys for User
```bash
aws iam list-access-keys --user-name my-new-user
```
Shows all access keys for a specific user.

### Delete Access Key
```bash
aws iam delete-access-key --user-name my-user --access-key-id AKIAIOSFODNN7EXAMPLE
```
Removes an access key (use carefully!).

### Attach Policy to User
```bash
aws iam attach-user-policy \
  --user-name my-user \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```
Grants permissions by attaching a managed policy.

### List Policies Attached to User
```bash
aws iam list-attached-user-policies --user-name my-user
```
Shows all policies attached to the user.

## Lambda Commands

### List Lambda Functions
```bash
aws lambda list-functions
```
Shows all Lambda functions in your account.

### Invoke Lambda Function
```bash
aws lambda invoke \
  --function-name my-function \
  --payload '{"key": "value"}' \
  response.json
```
Executes the Lambda and saves output to `response.json`.

### View Lambda Response
```bash
cat response.json
```
Shows the output from the invocation.

### Get Lambda Function Details
```bash
aws lambda get-function --function-name my-function
```
Returns configuration and metadata.

## DynamoDB Commands

### List Tables
```bash
aws dynamodb list-tables
```
Shows all DynamoDB tables.

### Describe Table
```bash
aws dynamodb describe-table --table-name my-table
```
Shows table schema, indexes, and settings.

### Scan Table (Get All Items)
```bash
aws dynamodb scan --table-name my-table
```
Returns all items in the table (expensive for large tables).

### Scan with Limit
```bash
aws dynamodb scan --table-name my-table --max-items 10
```
Returns only first 10 items.

### Get Specific Item
```bash
aws dynamodb get-item \
  --table-name my-table \
  --key '{"id": {"S": "123"}}'
```
Retrieves a single item by primary key.

## CloudWatch Logs Commands

### List Log Groups
```bash
aws logs describe-log-groups
```
Shows all CloudWatch log groups.

### Tail Lambda Logs (Live)
```bash
aws logs tail /aws/lambda/my-function --follow
```
Shows real-time logs as they come in (like `tail -f`).

### View Recent Logs
```bash
aws logs tail /aws/lambda/my-function --since 1h
```
Shows logs from the last hour.

### Filter Logs
```bash
aws logs filter-log-events \
  --log-group-name /aws/lambda/my-function \
  --filter-pattern "ERROR"
```
Shows only log lines containing "ERROR".

## EC2 Commands

### List EC2 Instances
```bash
aws ec2 describe-instances
```
Shows all EC2 instances with details.

### List Only Running Instances
```bash
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,PublicIpAddress]' \
  --output table
```
Shows a clean table of running instances.

### Start Instance
```bash
aws ec2 start-instances --instance-ids i-1234567890abcdef0
```
Starts a stopped instance.

### Stop Instance
```bash
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```
Stops a running instance.

## SNS Commands

### List Topics
```bash
aws sns list-topics
```
Shows all SNS topics.

### List Subscriptions for Topic
```bash
aws sns list-subscriptions-by-topic --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic
```
Shows all subscriptions for a specific topic.

### Publish Message to Topic
```bash
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --message "Hello from AWS CLI"
```
Sends a message to all subscribers.

## EventBridge Scheduler Commands

### List Schedules
```bash
aws scheduler list-schedules
```
Shows all EventBridge schedules.

### Get Schedule Details
```bash
aws scheduler get-schedule --name my-schedule-name
```
Shows configuration for a specific schedule.

## Glue Commands

### List Glue Databases
```bash
aws glue get-databases
```
Shows all Glue catalog databases.

### List Crawlers
```bash
aws glue list-crawlers
```
Shows all Glue crawlers.

### Start Crawler
```bash
aws glue start-crawler --name my-crawler
```
Manually triggers a Glue crawler run.

### Get Crawler Status
```bash
aws glue get-crawler --name my-crawler
```
Shows crawler state (READY, RUNNING, STOPPING).

## Athena Commands

### List Workgroups
```bash
aws athena list-work-groups
```
Shows all Athena workgroups.

### Execute Query
```bash
aws athena start-query-execution \
  --query-string "SELECT * FROM my_table LIMIT 10" \
  --query-execution-context Database=my_database \
  --result-configuration OutputLocation=s3://my-results-bucket/
```
Runs an Athena SQL query.

## Useful Tips

### Format Output as Table
```bash
aws s3 ls --output table
```
Makes output more readable.

### Format Output as Text
```bash
aws s3 ls --output text
```
Good for scripting (easier to parse).

### Use JQ for JSON Parsing
```bash
aws iam list-users | jq '.Users[].UserName'
```
Extracts just usernames from JSON output (requires `jq` installed).

### Get Help for Any Command
```bash
aws s3 help
aws s3 cp help
```
Shows detailed documentation for commands.

### Dry Run (Preview)
```bash
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0 --dry-run
```
Tests if you have permission without actually executing (not all services support this).

## GroundSense Project Commands

### List All GroundSense Resources
```bash
# Lambda functions
aws lambda list-functions --query 'Functions[?contains(FunctionName, `groundsense`)].FunctionName'

# S3 buckets
aws s3 ls | grep groundsense

# DynamoDB tables
aws dynamodb list-tables --query 'TableNames[?contains(@, `groundsense`)]'
```

### Tail GroundSense Lambda Logs
```bash
aws logs tail /aws/lambda/groundsense-dev-seismic-poller --follow
aws logs tail /aws/lambda/groundsense-dev-document-fetcher --follow
aws logs tail /aws/lambda/groundsense-dev-alert --follow
aws logs tail /aws/lambda/groundsense-dev-kb-sync --follow
```

### Manually Trigger Seismic Poller
```bash
aws lambda invoke \
  --function-name groundsense-dev-seismic-poller \
  --payload '{}' \
  /tmp/poller-response.json && cat /tmp/poller-response.json
```
