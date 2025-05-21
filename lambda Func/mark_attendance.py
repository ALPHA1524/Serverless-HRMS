import json
import boto3
from datetime import date

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Attendance')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    attendance = {
        'employeeID': body['employeeID'],
        'date': str(date.today()),
        'status': body['status']  # Present/Absent/Late
    }

    table.put_item(Item=attendance)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Attendance marked'})
    }
