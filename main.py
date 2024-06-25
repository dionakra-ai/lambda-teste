
def lambda_handler(event, context):
    print("Hello, CEIA")
    return {
        "statusCode": 200,
        "body": "Hello, World!"
    }