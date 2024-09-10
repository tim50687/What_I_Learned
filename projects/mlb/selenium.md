### Dockerfile
Your Dockerfile looks mostly correct, but let's refine it to make sure everything is in order. Here’s the updated Dockerfile:

```dockerfile
FROM amazon/aws-lambda-python:3.12

# Install Chrome dependencies
RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm jq unzip

# Copy and run the Chrome installer script
COPY chrome-installer.sh /chrome-installer.sh
RUN /chrome-installer.sh
RUN rm /chrome-installer.sh

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy function code
COPY functions/ /var/task/functions/
COPY utils/ /var/task/utils/

CMD ["functions.fetch_stats.lambda_handler"]
```

### serverless.yml
Your `serverless.yml` configuration looks good, but we need to make sure it’s correctly set up to build and deploy your Docker image. Here’s the refined version:

```yaml
service: mlb-data-fetcher

provider:
  name: aws
  runtime: python3.12
  architecture: x86_64
  stage: dev
  region: us-east-2
  ecr:
    images:
      selenium-chrome-python:
        path: ./

functions:
  fetchStats:
    image:
      name: selenium-chrome-python
      command: ["functions.fetch_stats.lambda_handler"]
    events:
      - schedule:
          name: daily8amEST
          description: Runs the fetchStats function every day at 8 AM EST
          rate: cron(0 13 * * ? *)
          enabled: true

plugins:
  - serverless-python-requirements
```

### Directory Structure
Ensure your project directory structure is correctly set up as follows:

```
.
├── Dockerfile
├── chrome-installer.sh
├── functions
│   ├── __init__.py
│   └── fetch_stats.py
├── requirements.txt
├── serverless.yml
└── utils
    ├── __init__.py
    ├── data_fetcher.py
    ├── s3_uploader.py
    └── stats_process.py
```

### Building and Pushing Docker Image

1. **Authenticate Docker to Your Amazon ECR:**
   ```sh
   aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-2.amazonaws.com
   ```

2. **Create a Repository in ECR:**
   ```sh
   aws ecr create-repository --repository-name selenium-chrome-python --region us-east-2
   ```

3. **Build the Docker Image:**
   ```sh
   docker build -t selenium-chrome-python .
   ```

4. **Tag the Docker Image:**
   ```sh
   docker tag selenium-chrome-python:latest <account-id>.dkr.ecr.us-east-2.amazonaws.com/selenium-chrome-python:latest
   ```

5. **Push the Docker Image to ECR:**
   ```sh
   docker push <account-id>.dkr.ecr.us-east-2.amazonaws.com/selenium-chrome-python:latest
   ```

### Deploy with Serverless Framework

1. **Deploy the Serverless Service:**
   ```sh
   serverless deploy
   ```

By following these steps, your Lambda function will be correctly set up with a custom Docker image, enabling you to run Selenium with Chrome for your web scraping tasks. If you encounter any issues or need further clarification, feel free to ask!

----
> Above didn't work because docker image layer too big to upload to ecr. Need to use lambda layers instead.

----

Let's include the `functions` and `utils` folders in our directory structure and Dockerfile setup. Below is the updated directory structure and steps, including the `functions` and `utils` folders.

### Updated Project Directory Structure

```
project-root/
├── infra/
│   ├── cdk.json
│   ├── infra-stack.ts
│   └── package.json
├── src/
│   ├── chrome-installer.sh
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── functions/
│   │   ├── __init__.py
│   │   └── fetch_stats.py
│   └── utils/
│       ├── __init__.py
│       ├── data_fetcher.py
│       ├── s3_uploader.py
│       └── stats_process.py
└── .github/
    └── workflows/
        └── deploy.yml
```

### Updated `Dockerfile`

In the `src` directory, create or update the `Dockerfile`:

```dockerfile
FROM amazon/aws-lambda-python:3.12

# Install Chrome dependencies
RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm jq unzip

# Copy and run the Chrome installer script
COPY chrome-installer.sh /chrome-installer.sh
RUN chmod +x /chrome-installer.sh && /chrome-installer.sh && rm /chrome-installer.sh

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy function and utility code
COPY functions/ /var/task/functions/
COPY utils/ /var/task/utils/

CMD [ "functions.fetch_stats.lambda_handler" ]
```

### Updated `fetch_stats.py`

Ensure that `fetch_stats.py` in the `functions` directory looks like this:

```python
import json
import os
import sys

# Add the parent directory to the system path to find utils
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.data_fetcher import FangraphsScraper
from utils.s3_uploader import upload_to_s3

BUCKET_NAME = 'timjimmymlbdata'

def lambda_handler(event, context):
    base_url_fb = "https://www.fangraphs.com/leaders/major-league"
    url_fb = FangraphsScraper.generate_url(base_url_fb, "fb")
    data_fb = FangraphsScraper.get_data(url_fb, "fb", file_path="/tmp/fangraphs_fb_data.json")

    base_url_barrel_hh = "https://www.fangraphs.com/leaders/major-league"
    url_barrel_hh = FangraphsScraper.generate_url(base_url_barrel_hh, "barrel_hh")
    data_barrel_hh = FangraphsScraper.get_data(url_barrel_hh, "barrel_hh", file_path="/tmp/fangraphs_barrel_hh_data.json")

    # Write to /tmp directory for Lambda environment
    fb_data_path = '/tmp/fangraphs_fb_data.json'
    barrel_hh_data_path = '/tmp/fangraphs_barrel_hh_data.json'

    # Write to tmp
    with open(fb_data_path, 'w') as f:
        json.dump(data_fb, f, indent=4, ensure_ascii=False)
    with open(barrel_hh_data_path, 'w') as f:
        json.dump(data_barrel_hh, f, indent=4, ensure_ascii=False)

    upload_to_s3(fb_data_path, BUCKET_NAME, 'fangraphs_fb_data.json')
    upload_to_s3(barrel_hh_data_path, BUCKET_NAME, 'fangraphs_barrel_hh_data.json')

    return {
        'statusCode': 200,
        'body': json.dumps('Data fetched and saved successfully')
    }
```


#### `deploy.yml`

```yaml
name: Deploy to AWS

on:
  push:
    branches: ["main"]

env:
  CDK_VERSION: "2.126.0"
  AWS_ACCOUNT_ID: ${{ secrets.AWS_ACCOUNT_ID }}
  AWS_REGION: ${{ secrets.AWS_REGION }}
  API_KEY: ${{ secrets.API_KEY }}  
  APPLICATION_TAG: ${{ vars.APPLICATION_TAG }}
  APPLICATION_NAME: "selenium-lambda"

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    name: Build & Deploy
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ASSUME_ROLE_ARN }}
          role-session-name: github-action-role
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Bootstrap
        run: |
          npm install -g aws-cdk
          npm install
          cdk bootstrap

      - name: Deploy
        run: |
          cdk deploy --require-approval never
```

### CDK Infrastructure Code

Create the CDK infrastructure files in the `infra` directory:

#### `cdk.json`

```json
{
  "app": "npx ts-node infra-stack.ts"
}
```

#### `infra-stack.ts`

```typescript
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const lambdaFunction = new lambda.DockerImageFunction(this, 'SeleniumLambda', {
      code: lambda.DockerImageCode.fromImageAsset('../src'),
      timeout: cdk.Duration.seconds(40),
      memorySize: 512,
    });

    const api = new apigateway.LambdaRestApi(this, 'Endpoint', {
      handler: lambdaFunction,
      proxy: false
    });

    const integration = new apigateway.LambdaIntegration(lambdaFunction);
    api.root.addMethod('GET', integration, {
      apiKeyRequired: true
    });

    const plan = api.addUsagePlan('UsagePlan', {
      name: 'Basic',
      quota: {
        limit: 1000,
        period: apigateway.Period.DAY,
      },
    });

    const key = api.addApiKey('ApiKey');
    plan.addApiKey(key);
    plan.addApiStage({
      stage: api.deploymentStage,
    });
  }
}

const app = new cdk.App();
new InfraStack(app, 'InfraStack');
app.synth();
```

#### `package.json`

```json
{
  "name": "infra",
  "version": "1.0.0",
  "bin": {
    "infra": "bin/infra"
  },
  "scripts": {
    "build": "tsc",
    "watch": "tsc -w",
    "cdk": "cdk"
  },
  "devDependencies": {
    "aws-cdk-lib": "^2.0.0",
    "constructs": "^10.0.0",
    "ts-node": "^10.0.0",
    "typescript": "^4.0.0"
  },
  "dependencies": {
    "@aws-cdk/aws-apigateway": "^2.0.0",
    "@aws-cdk/aws-lambda": "^2.0.0"
  }
}
```

### Deploy the Infrastructure

1. **Build and Push Docker Image:**

   ```sh
   docker build -t selenium-chrome-python src
   ```

2. **Initialize CDK:**

   ```sh
   cd infra
   npm install
   cdk bootstrap
   ```

3. **Deploy CDK Stack:**

   ```sh
   cdk deploy
   ```

4. **Trigger the GitHub Actions Workflow:**

   - Push the code to the `main` branch of your GitHub repository.
   - The GitHub Actions workflow will automatically run and deploy the infrastructure.

By following these steps, you should be able to set

 up and deploy your Selenium-based Lambda function using AWS CDK and GitHub Actions.

----
 Here's how you can set up AWS CDK using Python for your infrastructure. The structure will be similar to the JavaScript example but with Python syntax.

### Directory Structure

Here's an updated directory structure for using Python with AWS CDK:

```
project-root/
├── infra/
│   ├── app.py
│   ├── cdk.json
│   ├── requirements.txt
│   ├── infra_stack.py
├── src/
│   ├── chrome-installer.sh
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── functions/
│   │   ├── __init__.py
│   │   └── fetch_stats.py
│   └── utils/
│       ├── __init__.py
│       ├── data_fetcher.py
│       ├── s3_uploader.py
│       └── stats_process.py
└── .github/
    └── workflows/
        └── deploy.yml
```

### CDK Infrastructure Code in Python

Create the CDK infrastructure files in the `infra` directory:

#### `cdk.json`

```json
{
  "app": "python3 app.py"
}
```

#### `app.py`

```python
#!/usr/bin/env python3
import aws_cdk as cdk
from infra_stack import InfraStack

app = cdk.App()
InfraStack(app, "InfraStack")
app.synth()
```

#### `infra_stack.py`

```python
from aws_cdk import (
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    Duration,
    Stack
)
from constructs import Construct

class InfraStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_function = lambda_.DockerImageFunction(
            self, "SeleniumLambda",
            code=lambda_.DockerImageCode.from_image_asset("../src"),
            timeout=Duration.seconds(40),
            memory_size=512,
        )

        api = apigateway.LambdaRestApi(
            self, "Endpoint",
            handler=lambda_function,
            proxy=False
        )

        integration = apigateway.LambdaIntegration(lambda_function)
        api.root.add_method('GET', integration, api_key_required=True)

        plan = api.add_usage_plan(
            'UsagePlan',
            name='Basic',
            quota=apigateway.QuotaSettings(
                limit=1000,
                period=apigateway.Period.DAY
            )
        )

        key = api.add_api_key('ApiKey')
        plan.add_api_key(key)
        plan.add_api_stage(
            stage=api.deployment_stage
        )

```

#### `requirements.txt`

```txt
aws-cdk-lib
constructs>=10.0.0
```

### GitHub Actions Workflow

Create the GitHub Actions workflow in the `.github/workflows` directory:

#### `deploy.yml`

```yaml
name: Deploy to AWS

on:
  push:
    branches: ["main"]

env:
  CDK_VERSION: "2.126.0"
  AWS_ACCOUNT_ID: ${{ secrets.AWS_ACCOUNT_ID }}
  AWS_REGION: ${{ secrets.AWS_REGION }}
  API_KEY: ${{ secrets.API_KEY }}  
  APPLICATION_TAG: ${{ vars.APPLICATION_TAG }}
  APPLICATION_NAME: "selenium-lambda"

permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    name: Build & Deploy
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_ASSUME_ROLE_ARN }}
          role-session-name: github-action-role
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Install dependencies
        run: |
          pip install -r infra/requirements.txt

      - name: Bootstrap
        run: |
          cd infra
          cdk bootstrap

      - name: Deploy
        run: |
          cd infra
          cdk deploy --require-approval never
```

### Deployment Steps

1. **Build and Push Docker Image:**

   ```sh
   cd src
   docker build -t selenium-chrome-python .
   ```

2. **Initialize CDK:**

   ```sh
   cd infra
   pip install -r requirements.txt
   cdk bootstrap
   ```

3. **Deploy CDK Stack:**

   ```sh
   cdk deploy
   ```

4. **Trigger the GitHub Actions Workflow:**

   - Push the code to the `main` branch of your GitHub repository.
   - The GitHub Actions workflow will automatically run and deploy the infrastructure.

This setup ensures that you have a complete CI/CD pipeline using GitHub Actions, CDK for infrastructure as code in Python, and a containerized Lambda function.


> Need to have repo on ecr first 

### Step 1: Authenticate Docker to Your ECR Repository

```sh
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-2.amazonaws.com
```

### Step 2: Create an ECR Repository (if not already created)

```sh
aws ecr create-repository --repository-name selenium-chrome-python --region us-east-2
```

### Step 3: Tag Your Docker Image

```sh
docker tag selenium-chrome-python:latest <account-id>.dkr.ecr.us-east-2.amazonaws.com/selenium-chrome-python:latest
```

### Step 4: Push Your Docker Image to ECR

```sh
docker push <account-id>.dkr.ecr.us-east-2.amazonaws.com/selenium-chrome-python:latest
```


> cloud stack

The aws cloudformation describe-stacks --stack-name CDKToolkit command shows information about the CDKToolkit CloudFormation stack, which includes various outputs such as the ECR repository name. Deleting the ECR repository from the AWS Management Console (ECR website) doesn't remove the outputs from the CloudFormation stack.


You're right! When using AWS CDK to deploy a Lambda function with a Docker image, **Elastic Container Registry (ECR)**, **CloudFormation**, and **Lambda** are all involved. Here's why each of these services is used:

### 1. **Elastic Container Registry (ECR)**

- **ECR** is a fully-managed Docker container registry provided by AWS. It allows you to store, manage, and deploy Docker container images.
- Since you're deploying a **Docker-based Lambda function**, the image needs to be stored somewhere accessible to Lambda. AWS Lambda can't run the Docker image directly from your local machine or from any arbitrary location; it needs to pull the image from a managed container registry like ECR.
  
**Why it's involved:**
- **CDK automatically pushes your Docker image to ECR**. When you define a `DockerImageFunction` in your CDK stack, the Docker image gets built and uploaded to ECR. From there, AWS Lambda can pull the image when it needs to run the function.

### 2. **AWS CloudFormation**

- **CloudFormation** is an AWS service that allows you to manage and provision AWS resources using templates. It provides a way to define your infrastructure as code, ensuring that all resources are created, updated, and deleted in a controlled manner.
  
**Why it's involved:**
- When you run `cdk deploy`, the AWS CDK internally converts your Python code into a **CloudFormation template**. This template specifies the resources (like Lambda, API Gateway, ECR repositories, etc.) and their configurations.
- **CloudFormation** then uses this template to **create, update, or delete the AWS resources** based on your CDK code. It's essentially the service that provisions the infrastructure on AWS, and CDK is a higher-level abstraction that generates CloudFormation templates.

### 3. **AWS Lambda**

- **Lambda** is AWS's serverless compute service. You're using it to run a Docker container with your code inside.
- AWS Lambda supports **container images up to 10 GB**, so you can deploy complex applications or code environments (like Selenium) that don't fit into Lambda's traditional runtime limits.

**Why it's involved:**
- Your CDK stack creates a **Lambda function** using the Docker image stored in ECR.
- Lambda then **pulls the Docker image from ECR** and executes your function when triggered via the API Gateway.

### How These Services Work Together:

1. **CDK builds and pushes your Docker image to ECR**: When you define a `DockerImageFunction`, CDK builds the Docker image using the `Dockerfile` in your project and uploads it to ECR. This makes the image accessible to other AWS services.
   
2. **CDK generates a CloudFormation template**: The CDK code is transformed into a CloudFormation template that includes the definition of the Lambda function, API Gateway, and the ECR repository. CloudFormation is responsible for creating and managing these resources on AWS.

3. **Lambda uses the Docker image from ECR**: When the Lambda function is invoked (via API Gateway or another trigger), it pulls the Docker image from ECR, runs the code inside it, and handles the execution of your function.

### Visual Summary:
- **ECR**: Stores the Docker image for your Lambda function.
- **CloudFormation**: Manages and deploys the infrastructure (Lambda, ECR repository, API Gateway) defined in your CDK code.
- **Lambda**: Executes your code using the Docker image stored in ECR.

### Conclusion:
All three services—**ECR**, **CloudFormation**, and **Lambda**—work together to deploy and run your Docker-based Lambda function. CDK simplifies the process by handling the creation of the necessary resources through CloudFormation and pushing your Docker image to ECR automatically.


## CDK
What is CDK? AWS CDK is a tool that allows you to define your cloud infrastructure using code. In your case, you're writing Python code to describe what resources (like Lambda, API Gateway, and ECR) you want AWS to create for you.

Yes, if you update the code (or make changes to the Dockerfile or any source files), you will need to **rebuild the Docker image** and push it to ECR. But here's how you can handle updates efficiently using AWS CDK without manually deleting resources:

### Do You Need to Delete the CloudFormation Stack or ECR Image?

No, **you do not need to delete anything manually**—neither the CloudFormation stack nor the ECR image. AWS CDK handles updates for you. Let me explain how this works:

### 1. **When You Update Code** (e.g., Python or Dockerfile)

When you make changes to your code or Dockerfile, you'll need to **rebuild the Docker image**. CDK will take care of rebuilding the image and pushing it to ECR automatically when you redeploy. You can follow these steps:

1. **Rebuild the Docker Image Automatically**:
   When you run `cdk deploy`, CDK will detect that changes have been made in your Docker source (`../src`), and it will:
   - Rebuild the Docker image.
   - Push the updated Docker image to ECR.
   - Update the Lambda function to use the new image.

2. **Run CDK to Update Resources**:
   After making changes, simply run:
   ```bash
   cdk deploy
   ```

   **CDK will automatically do the following**:
   - Detect that the Docker source has changed.
   - Rebuild the Docker image.
   - Push the new image to ECR.
   - Update the Lambda function to use the new image.
   - Update any other infrastructure changes you’ve made.

### 2. **CloudFormation Stack Update Process**
When you run `cdk deploy`, CloudFormation handles the update process. This means:
- It will **replace the old Docker image** with the new one in ECR.
- It will update the **Lambda function** to pull the new image from ECR.
- It will update any other changes you've made (e.g., API Gateway, environment variables, etc.).

You do **not need to delete the CloudFormation stack** or the ECR image manually. AWS CloudFormation is smart enough to replace the old image and keep the stack consistent without causing downtime or loss of resources.

### Steps to Update Code:

1. **Make code changes** to your Lambda function (inside `../src`) or update the Dockerfile.
   
2. **Run `cdk deploy`**:
   ```bash
   cdk deploy
   ```
   This will:
   - Rebuild the Docker image.
   - Push the updated image to ECR.
   - Update the Lambda function to use the new image.

### Can You Just Update?

Yes, **you can just update** without needing to manually delete anything. CDK and CloudFormation will handle the updates for you, ensuring a smooth and automatic deployment of the new version.

### When to Delete Resources (Rare Case)

You only need to consider deleting resources manually in very rare cases, such as:
- You no longer need the infrastructure (e.g., you are shutting down the entire project).
- You want to completely reset the environment.

In these cases, you can delete the **CloudFormation stack** through the AWS Console or by running:
```bash
cdk destroy
```
This will clean up all resources, including the ECR images associated with the stack.

### Summary:
- **Rebuild the Docker image automatically**: When you run `cdk deploy`, it will rebuild the image if the code has changed and push it to ECR.
- **Update the stack**: Running `cdk deploy` will update all necessary resources, including the Lambda function, with the new Docker image.
- **No need to delete resources manually** unless you are decommissioning the entire project.
