### 1. Prepare Your Flask Application for Deployment

1. **Create a `requirements.txt` file:**
   - This file lists all the Python dependencies for your project.
   - You can generate it using `pip freeze`:

   ```sh
   pip freeze > requirements.txt
   ```

2. **Create a `vercel.json` file:**
   - This file configures the Vercel deployment.
   - Create a file named `vercel.json` in your project root with the following content:

   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Modify `app.py`:**
   - Ensure your Flask application can be started by running `app.py`.
   - If your app entry point is different, adjust the `vercel.json` file accordingly.

4. **Static Files Handling:**
   - Vercel serves static files automatically from a `static` directory.
   - Ensure your static files (CSS, JS, images) are placed correctly.

### 2. Set Up APScheduler for Background Tasks on Vercel

APScheduler does not work well on serverless platforms like Vercel because it relies on persistent processes to run tasks at scheduled intervals. As a workaround, you can use external services like AWS Lambda, Google Cloud Functions, or even cron jobs on a separate server to trigger your background tasks.

### 3. Deploy to Vercel

1. **Install Vercel CLI:**
   - Install the Vercel CLI globally:

   ```sh
   npm install -g vercel
   ```

2. **Login to Vercel:**
   - Login to your Vercel account:

   ```sh
   vercel login
   ```

3. **Deploy Your Application:**
   - Deploy your application to Vercel:

   ```sh
   vercel
   ```

### 4. Schedule Background Tasks Externally

Since Vercel is not suitable for persistent background tasks, you can use an external scheduler:

1. **AWS Lambda and CloudWatch:**
   - Use AWS Lambda to create a function for fetching and saving data.
   - Schedule this Lambda function using CloudWatch Events to run at the desired intervals.

2. **Google Cloud Functions:**
   - Use Google Cloud Functions to create a function for fetching and saving data.
   - Schedule this function using Google Cloud Scheduler.

3. **Other Services:**
   - Services like Zapier, IFTTT, or even a VPS with cron jobs can be used to trigger your tasks.

### Example: Scheduling with AWS Lambda

1. **Create Lambda Functions:**
   - Create two Lambda functions: one for fetching home run odds and one for fetching player stats.
   - Use the code from your Flask app, but modify it to run as standalone functions.

2. **Schedule Lambda Functions:**
   - Use CloudWatch Events to schedule these functions to run at your specified intervals (e.g., every 2 hours for odds, daily at 8 PM for stats).

### Summary

1. **Prepare Flask App:**
   - Create `requirements.txt` and `vercel.json`.
   - Ensure your app runs correctly with `app.py`.

2. **Deploy to Vercel:**
   - Use Vercel CLI to deploy your app.

3. **External Scheduling:**
   - Use AWS Lambda, Google Cloud Functions, or similar services to handle background tasks.

### Sample Lambda Function for Fetching Data

```python
import json
import requests

def lambda_handler(event, context):
    base_url_fb = "https://www.fangraphs.com/leaders/major-league"
    url_fb = generate_url(base_url_fb, "fb")
    data_fb = get_or_fetch_data(url_fb, "fb", file_path="/tmp/fangraphs_fb_data.json")

    base_url_barrel_hh = "https://www.fangraphs.com/leaders/major-league"
    url_barrel_hh = generate_url(base_url_barrel_hh, "barrel_hh")
    data_barrel_hh = get_or_fetch_data(url_barrel_hh, "barrel_hh", file_path="/tmp/fangraphs_barrel_hh_data.json")

    # Upload JSON files to S3 or another storage service
    upload_to_s3('/tmp/fangraphs_fb_data.json', 'your-bucket', 'fangraphs_fb_data.json')
    upload_to_s3('/tmp/fangraphs_barrel_hh_data.json', 'your-bucket', 'fangraphs_barrel_hh_data.json')

    return {
        'statusCode': 200,
        'body': json.dumps('Data fetched and saved successfully')
    }

def generate_url(base_url, type):
    # Your implementation
    pass

def get_or_fetch_data(url, type, file_path):
    # Your implementation
    pass

def upload_to_s3(file_path, bucket_name, object_name):
    import boto3
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, object_name)
```

