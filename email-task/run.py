from mail import send_mail
from sqs_connect import SQS_Client
import time

sqs = SQS_Client()
msg = sqs.consume()
print(msg)

if msg:
    print("message ingested from queue")

    send_mail(
        recv_addr = msg['recv_addr']['StringValue'], 
        subject = msg['subject']['StringValue'],
        body = "".join([ 
            msg['body']['StringValue'], 
            "\n\n", 
            f"consumed by email-task service in : {time.time() - float(msg['dispatched_at']['StringValue'])} s" 
        ]),
    )

else:
    print("no more messages to ingest")




# copy and paste to build & run server locally
'''
docker build --no-cache -t ecs-email-task . && docker run --env-file=.env ecs-email-task
'''

# copy paste this to update on docker hub
'''
docker build --no-cache -t ecs-email-task . && docker tag ecs-email-task:latest devesh243/ecs-email-task:latest && docker push devesh243/ecs-email-task:latest
'''