import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import uuid

SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
flow = InstalledAppFlow.from_client_secrets_file('C:/Users/Admin/Documents/GitHub/remote-control/server/credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

service = build('gmail', 'v1', credentials=creds)
message_body = 'PRINT' # sử dụng phương thức format() để thêm giá trị vào nội dung email
#"HOOK"
#"PRINT"
#"LOCK"
message = MIMEText(message_body)

message['to'] = 'testpython18mmt@gmail.com'
message['subject'] = 'client'
create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

try:
    message = (service.users().messages().send(userId="me", body=create_message).execute())
    print(F'sent message to {message} Message Id: {message["id"]}')
except HTTPError as error:
    print(F'An error occurred: {error}')
    message = None


#https://mailtrap.io/blog/python-send-email-gmail/