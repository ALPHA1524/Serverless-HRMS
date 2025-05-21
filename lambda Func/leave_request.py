import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Leaves')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    leave_request = {
        'leaveID': str(uuid.uuid4()),
        'employeeID': body['employeeID'],
        'startDate': body['startDate'],
        'endDate': body['endDate'],
        'reason': body['reason'],
        'status': 'Pending'
    }

    table.put_item(Item=leave_request)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Leave request submitted'})
    }
