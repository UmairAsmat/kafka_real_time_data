import boto3
import os
from botocore.exceptions import ClientError

def upload_to_s3(local_file, bucket_name, s3_key):
    # Check if file exists
    if not os.path.exists(local_file):
        raise FileNotFoundError(f"The file {local_file} was not found")

    try:
        # Create S3 client
        s3 = boto3.client('s3')
        
        # Try to upload the file
        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"Successfully uploaded {local_file} to s3://{bucket_name}/{s3_key}")
        return True
    
    except ClientError as e:
        if "AccessDenied" in str(e):
            print("AWS credentials not found or don't have sufficient permissions.")
            print("Please configure your AWS credentials using:")
            print("aws configure")
        else:
            print(f"An error occurred: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    # Configuration
    bucket_name = 'portfolio-project-data'
    local_file = 'data/indexProcessed.csv'
    s3_key = 'stock_market/indexProcessed.csv'

    # Upload file
    upload_to_s3(local_file, bucket_name, s3_key)
