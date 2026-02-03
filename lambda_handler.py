"""
AWS Lambda handler for carbon-aware job scheduling.
Author: Vedant Rajhans
"""

import os
import json
import uuid
from datetime import datetime

import boto3

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("CARBON_JOBS_TABLE")
table = dynamodb.Table(table_name)


def fetch_carbon_data(api_key):
    """
    Placeholder for your existing carbon intensity logic.
    """
    print(f"Using API Key: {api_key[:4]}****")
    region = "IN-WEST"  # Example region
    return region


def lambda_handler(event, context):
    # Read API key from environment variables
    api_key = os.environ.get("ELECTRICITY_MAP_API_KEY")

    if not api_key:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "ELECTRICITY_MAP_API_KEY not set"})
        }

    # Fetch carbon data (your existing logic)
    region = fetch_carbon_data(api_key)

    # Simulate SageMaker job trigger
    print("Job Started")

    # Create DynamoDB record
    job_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    table.put_item(Item={
        "JobId": job_id,
        "Region": region,
        "Timestamp": timestamp
    })

    return {
        "statusCode":
        200,
        "body":
        json.dumps({
            "message": "Carbon job triggered successfully",
            "job_id": job_id,
            "region": region,
            "timestamp": timestamp
        })
    }
