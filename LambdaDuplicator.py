import boto3
import urllib3
import os


def lambdaService():
    return boto3.client('lambda',
                        region_name='us-east-1',
                        aws_access_key_id=os.environ['aws_access_key_id'],
                        aws_secret_access_key=os.environ['aws_secret_access_key'])


def get_original_func(client_, func_name):
    try:
        return client_.get_function(FunctionName=func_name)
    except client_.exceptions.ResourceNotFoundException:
        return -1
    except client_.exceptions.ClientError as error:
        print(
            "Got Invalid Signature Error. This occurs when 'aws_access_key_id' and/or 'aws_secret_access_key' is "
            "invalid. More error:\n", error)
        return -2

    myDict = \
        {
            'Configuration':
                {
                    'FunctionName': 'duplicator',
                    'FunctionArn': 'arn:aws:lambda:us-east-1:873024044354:function:duplicator',
                    'Runtime': 'java11',
                    'Role': 'arn:aws:iam::873024044354:role/yolo-lambda',
                    'Handler': 'example.Hello::handleRequest',
                    'CodeSize': 8928,
                    'Description': '',
                    'Timeout': 75,
                    'MemorySize': 512,
                    'LastModified': '2022-12-14T22:35:42.000+0000',
                    'CodeSha256': 'jYP1nUIZ6A7Mqr3J5GwlBCMva56NpgTZDLKGRkT7LQo=',
                    'Version': '$LATEST',
                    'VpcConfig':
                        {
                            'SubnetIds': ['subnet-0c90bfd65f6abaa3e', 'subnet-09873a9d174453782'],
                            'SecurityGroupIds': ['sg-070dbeca2204bea66'],
                            'VpcId': 'vpc-08031307437382ca4'
                        },
                    'Environment':
                        {
                            'Variables':
                                {
                                    'key1': 'valu1',
                                    'key2': 'value2'
                                }
                        },
                    'TracingConfig':
                        {
                            'Mode': 'PassThrough'
                        },
                    'RevisionId': '938d0300-4220-4be3-b9b1-af5ba579f7f0',
                    'State': 'Active',
                    'LastUpdateStatus': 'Successful',
                    'PackageType': 'Zip',
                    'Architectures': ['x86_64'],
                    'EphemeralStorage': {
                        'Size': 512
                    }
                },
            'Code':
                {
                    'RepositoryType': 'S3',
                    'Location': 'https://prod-04-2014-tasks.s3.us-east-1.amazonaws.com/snapshots/873024044354/duplicator-f5f169c1-e881-4190-b0df-e4fadb015f33?versionId=2U_3W4sHPqqd5vQGShtX7JanDb4HCSdX&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIF9eO2DvfpCP%2BM1Wo1ZXSWjIQkPuM%2FEQt44xfV2KhFujAiEA8a23UAI8rirdMlXX2jyZxV1XmhRhbKugIVZrra3vWk8q1QQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw3NDk2Nzg5MDI4MzkiDKau%2B4D277oga6ryqCqpBKsnfAo0ggX6XWcLq1k6GWVpgsygFnsu2%2FMYqzuKpSSPoMNJ1GNwg7rw3V1Dh7VlgW8XyXC%2FqwQrjPALDyEQgP5XuD0pm6o2FJnC5WynoaiZ2gyCZ%2FVP0k7X%2BbhuSWg2DnxLfTw9kF0u5akD3mWBYqaH8BrZhqfDVshnwa%2FYJnSF6uzQFLQPbt9sVouk%2BKpJRMsXUSui3FtlBKp%2BgXCl4EIXNruiEhVyqiP1z8XzxCgUtV3PQnzx4Jpv%2B3VAfeLHxHddwWihHpOPk9v9tRjmpJS8gS%2FXwKxzg1SUulX26BOnZfcRz%2FWJtIR%2Bqt%2FgKZtRHVgHc2JXq85medGdI6ocWN8CkHwW2AVUfEPOejA0Sliyj1Zn92Es1nyGkjTlBAAvjpCeeisRDtT%2BAz2SaY4tu57d5T7yYzfmQUpZfZ5wGsZJoy%2FRHD9RfItCi18jm5tYjky8ojFYiu%2FrnDhISyIx7UAxKQ8mS9WOObjXO1PNX5ZFTR38ndu0848ka2zGqN9KmcEk7jWRG0dmEhbkNgv5anY%2FNWORfafk6qbjCo5cUYuM%2BezPOPNJWnlxv4N5BTJQBsQn4BbbrjF4%2BaS8VkLwYR08UlTYpCX4Re9QnuGTZ3FL%2Buc8cE%2BpaQtzPxGgC9d8Wtj5yWAjtySw5lHk1ZZYs2K6BzZ3VjZcq84hss4Glr26laHve8DkhVz%2FcDLzyuF0u%2BP6t2LNjpjZDXbPcaTIpDDLt7YvZk%2BDAf4wmuTunAY6qQFSMH03PGhTd4OFvedFCtbEg83o5L6JtaGgOxXb1E3AbRSRa0yrdhw6uChrKUTb%2Fy4j6juZo4blF8tzxs7UqpEKVChmIQCGDtvxuzyzrdK3TcpPpl8A3X0DBD%2BpeeFJGM7GkdYVlj%2BRk2JJBOgpQZveqlFMItEm3A5ARh6pXB8oPT0ZJuwuszkkzodyU2jj9YiWRnGp2NtyrY6Hi4Qb%2FjUrDNdd63Ax6YUN&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221216T005542Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIA25DCYHY3RSLMNUUS%2F20221216%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=87a2780002c68df0ecbe47fc830fd5c579d72a4c4fe7c4fe28db21a1dc0a9092'
                },
            'Tags':
                {
                    'type': 'test'
                }
        }

    # return myDict


def get_code(orig_func_):
    code_url = orig_func_.get('Code').get('Location')
    http = urllib3.PoolManager()
    res = http.request("GET", code_url)
    if res.status == 200:
        return res.data
    else:
        print("Error: The Location Provided Does Not Exist!")
        return -1


def create_lambda_func(client_, orig_func_, new_func_name, code_file):
    orig_func_config = orig_func_.get('Configuration')
    try:
        return client_.create_function(
            FunctionName=new_func_name,
            Runtime=orig_func_config.get('Runtime'),
            Role=orig_func_config.get('Role'),
            Handler=orig_func_config.get('Handler'),
            Code={
                'ZipFile': code_file,
            },
            Description=orig_func_config.get('Description'),
            Timeout=orig_func_config.get('Timeout'),
            MemorySize=orig_func_config.get('MemorySize'),
            Publish=True,
            VpcConfig={
                'SubnetIds':
                    orig_func_config.get('VpcConfig').get('SubnetIds'),
                'SecurityGroupIds':
                    orig_func_config.get('VpcConfig').get('SecurityGroupIds'),
            },
            Environment={
                'Variables': orig_func_config.get('Environment').get('Variables')
            },
            TracingConfig={
                'Mode': orig_func_config.get('TracingConfig').get('Mode')
            },
            Tags=orig_func_.get('Tags')
        )
    except client_.exceptions.ResourceConflictException:
        print("New Function Already Exists")
        return -1


def validate_new_func(new_func_):
    return new_func_.get('ResponseMetadata').get('HTTPStatusCode') == 201


if __name__ == '__main__':
    client = lambdaService()
    orig_func = get_original_func(client, 'duplicator')
    if orig_func != -1 and orig_func != -2:
        code = get_code(orig_func)
        if code != -1:
            new_func = create_lambda_func(client, orig_func, 'duplicatorCopy2', code)
            if new_func != -1:
                valid = validate_new_func(new_func)
                if valid:
                    print("\nFunction Creation Successful")
                else:
                    print("\nFunction Created Failed")
            else:
                print("\nNew Function was Not Created")
        else:
            print("\nNo Valid Code File Was Found")
    else:
        if orig_func == -2:
            print("\nAWS Lambda Client Could Not Be Created")
        else:
            print("\nOriginal Function Does Not Exists")

    '''
    1. Create lambda
        aws lambda create-function --function-name my-function \
            --zip-file fileb://function.zip --handler index.handler --runtime nodejs18.x \
            --role arn:aws:iam::123456789012:role/lambda-ex
            
    2.  Get funciton
        aws lambda get-function --function-name my-function
    3. Configure function 
        aws lambda update-function-configuration \
        --function-name my-function 
        --runtime 
        --role 
        --handler
        --timeout
        --vpc-config SubnetIds =,SecurityGroupIds
        --environment Variables = {"k1": "v1", "k2": "v2"}
    
    4. Create queue
        aws sqs create-queue
        --queue-name
        --attributes MaximumMessageSize =,MessageRetentionPeriod =,VisibilityTimeout =, FifoQueue = false
    
    5. Create event bridge rule
        aws events put-rule
        --name " "
        --schedule-expression "cron(0 9 * * ? *)"
        --event-pattern {\"source\":[\"com.mycompany.myapp\"]}" 
        --state=DISABLED
    5. Create event source mapping
    aws lambda create-event-source-mapping
    --event-source-arn ${ARn of the trigger} \
    --function-name ${name of lambda} \
    --batch-size ${1} \
    --no-enabled
    --starting-position TRIM_HORIZON
              
    '''
