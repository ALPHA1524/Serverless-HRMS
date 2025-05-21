import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Payroll')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    payroll = {
        'employeeID': body['employeeID'],
        'month': datetime.now().strftime('%Y-%m'),
        'basicPay': body['basicPay'],
        'allowance': body['allowance'],
        'deductions': body['deductions'],
        'netPay': body['basicPay'] + body['allowance'] - body['deductions']
    }

    table.put_item(Item=payroll)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Payroll processed'})
    }
