import os
import boto3
import uuid

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
    

    def publish(self, messageAttributes: dict) -> dict:

        messageBody = f"uuid - {uuid.uuid4().__str__()}"

        res = self.client.send_message(
            QueueUrl = self.q_url,
            MessageBody = messageBody,
            MessageAttributes = messageAttributes
        )

        print("[x] message posted to queue")
        return res