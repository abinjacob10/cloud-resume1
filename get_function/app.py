import json
import boto3

# import requests


def get_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('table1')
    response = table.get_item(

            Key = {
                'counts': 'hits'
            }
    )

    item = response['Item']                         # returns of type dictionary
    x=int(item['hits'])       # converts decimal value of 'hits' to int value, because json could serialize int, not decimal,
                              # if decimal is not converted to type which JSON could serialize, we would see this error for third last line
                              # "Object of type decimal is not JSON serializable"
    #print(item['hits'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({ "count" : x })
    
    }
