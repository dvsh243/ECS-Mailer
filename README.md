# ECS-Mailer

- run a task for `server` at ECS Cluster
- at every `/mail` post request,
    - a message is posted to the SQS queue.
    - a task is `email-task` task is dispached remotely from the `server`.
    - the `email-task` consumes a message from SQS queue, send the email from `messageAttributes` provided and shuts down the container.