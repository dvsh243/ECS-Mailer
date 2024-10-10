import os
import boto3

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

class ECS_Client:
    
    def __init__(self) -> None:

        self.client = boto3.client(
            'ecs', 
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
            region_name = 'ap-south-1'
        )
        print(f"[x] connected to ECS client.")
    

    def dispatch(self):

        self.client.run_task(
            cluster = 'cluster1',
            taskDefinition = 'email-task',
            launchType = 'FARGATE',
            networkConfiguration = {
                'awsvpcConfiguration': {
                    'subnets': ["subnet-0118cda9fd6c42011", "subnet-0857fe2d24f2e47c9", "subnet-0b6eadbbc64dff27f"],
                    'securityGroups': ["sg-0bd06ba5a22f7f64f"],  # all traffic
                    'assignPublicIp': 'ENABLED'
                }
            }
        )
        print(f"[x] task dispached.")