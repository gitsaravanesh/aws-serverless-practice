import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("UserName")  # Replace with your actual DynamoDB table name

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])  # Extract JSON body
        name = body.get("name")  # Get 'name' from the request
        
        if not name:
            return {"statusCode": 400, "body": json.dumps({"message": "Name is required"})}
        
        # Store name in DynamoDB
        table.put_item(Item={"id": name})

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"  # Enable CORS
            },
            "body": json.dumps({"message": "Name stored successfully"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
