import os
import boto3

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


class SQS_Client:
    
    def __init__(self) -> None:

        self.q_url = "https://sqs.ap-south-1.amazonaws.com/212267546873/q-mail"

        self.client = boto3.client(
            'sqs', 
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
            region_name = 'ap-south-1'
        )
        print(f"[x] connected to SQS client.")
    
    
    def consume(self) -> dict:

        messages = self.client.receive_message(
            QueueUrl=self.q_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,  # polls the queue every 10 seconds
            MessageAttributeNames=['All']
        )

        if 'Messages' not in messages: 
            return {}

        msg = messages['Messages'][0]
        
        # Process the message attributes
        message_attributes = msg['MessageAttributes']
        
        # Delete the message from the queue
        self.client.delete_message(QueueUrl=self.q_url, ReceiptHandle=msg['ReceiptHandle'])
        
        return message_attributes