import json
import boto3
import uuid
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Perfomance')

def lambda_handler(event, context):
    data = json.loads(event['body'], parse_float=Decimal)
    
    review = {
        'employeeID': data['employeeID'],  # Partition Key
        'reviewDate': datetime.utcnow().isoformat(),  # Sort Key
        'reviewID': str(uuid.uuid4()),
        'score': data['score'],
        'comments': data['comments']
    }

    table.put_item(Item=review)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Performance review added successfully'})
    }
