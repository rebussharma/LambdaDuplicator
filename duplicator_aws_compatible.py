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



def lambda_handler(event, context):
    client = lambdaService()
    origina_func_name = event['orig_func_name']
    orig_func = get_original_func(client, origina_func_name)
    message = ""
    if orig_func != -1 and orig_func != -2:
        code = get_code(orig_func)
        if code != -1:
            new_func = create_lambda_func(client, orig_func, event['new_func_name'], code)
            if new_func != -1:
                valid = validate_new_func(new_func)
                if valid:
                    message = "Function Creation Successful"
                else:
                    message = "Function Created Failed"
            else:
                message = "New Function was Not Created"
        else:
            message = "No Valid Code File Was Found"
    else:
        if orig_func == -2:
            message = "AWS Lambda Client Could Not Be Created"
        else:
            message = "Original Function Does Not Exists"
            
    # TODO implement
    return {
        'message': message
    }

