from pydantic import BaseModel


class send_mail_Request(BaseModel):
    recv_addr: str = "deveshahuja243@gmail.com"
    subject: str = "mail subject"
    body: str = "mail body"