import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Employees')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    employee = {
        'employeeID': body['employeeID'],
        'name': body['name'],
        'email': body['email'],
        'department': body['department'],
        'joinDate': body['joinDate']
    }

    table.put_item(Item=employee)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Employee added successfully'})
    }
