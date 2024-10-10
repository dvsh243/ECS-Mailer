from fastapi import FastAPI
from models import send_mail_Request
from sqs_connect import SQS_Client
from ecs_connect import ECS_Client
import time

sqs = SQS_Client()
ecs = ECS_Client()
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/mail")
async def send_mail(
        request: send_mail_Request
    ):
    start_time = time.time()

    messageAttributes = {
            'recv_addr': {'StringValue': request.recv_addr, 'DataType': 'String'},
            'subject': {'StringValue': request.subject, 'DataType': 'String'},
            'body': {'StringValue': request.body, 'DataType': 'String'},
            'dispatched_at': {'StringValue': start_time.__str__(), 'DataType': 'String'},
        }
    sqs.publish(messageAttributes)
    ecs.dispatch()  # create a container to process this message
    
    return {"task status": "dispached", "resposne": f"{time.time() - start_time} s"}




# copy and paste to build & run server locally
'''
docker build --no-cache -t ecs-email-server . && docker run --env-file=.env -p 8000:8000 ecs-email-server
'''

# copy paste this to update on docker hub
'''
docker build --no-cache -t ecs-email-server . && docker tag ecs-email-server:latest devesh243/ecs-email-server:latest && docker push devesh243/ecs-email-server:latest
'''