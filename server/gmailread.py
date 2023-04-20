from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import email
import time
from bs4 import BeautifulSoup
import uuid
from email.mime.text import MIMEText
from requests import HTTPError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    'https://www.googleapis.com/auth/gmail.readonly',
]

def send_mail(cmd, package):
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            path = os.path.abspath('credentials.json')
            flow = InstalledAppFlow.from_client_secrets_file(
                path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next runserver\credentials.json
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    message_body = '{}. {}'.format(cmd, package)  # sử dụng phương thức format() để thêm giá trị vào nội dung email
    message = MIMEText(message_body)

    message['to'] = 'testpython18mmt@gmail.com'
    message['subject'] = 'server'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
    message = None
def read_mail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            path = os.path.abspath('credentials.json')
            flow = InstalledAppFlow.from_client_secrets_file(
                path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next runserver\credentials.json
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        # query list message with subject client and not read
        results = service.users().messages().list(userId='me', q='is:unread subject:client').execute()
        #results = service.users().messages().list(userId='me').execute()
        mes = results.get('messages', [])
        if not mes:
            print("No letter find out")
            return "no"
        else:
            for m in mes:
                 # Call the Gmail v1 API, retrieve message data.
                message = service.users().messages().get(userId='me', id=m['id'], format="raw").execute()

                res = get_info_message(message)

                """
                Đánh dấu thư là đã đọc
                """
                # Mark read letter from gmail
                mark_as_read(service, m)
                return res

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
def get_info_message(message):
    # Parse the raw message.
    mime_msg = email.message_from_bytes(base64.urlsafe_b64decode(message['raw']))

    # print('from', mime_msg['from'])
    # print('to', mime_msg['to'])
    # print('subject', mime_msg['subject'])
    # print("----------------------------------------------------")
    t = ""
    message_main_type = mime_msg.get_content_maintype()
    if message_main_type == 'multipart':
        for part in mime_msg.get_payload():
            if part.get_content_maintype() == 'text':
                # print(1)
                t = part.get_payload()
                # print(part.get_payload())
    elif message_main_type == 'text':
        # print(2)
        t = mime_msg.get_payload()
        # print(mime_msg.get_payload())
    print("\n",t)
    return t
    # print("----------------------------------------------------\n\n\n")

        # Message snippet only.
        # print('Message snippet: %s' % message['snippet'])

def mark_as_read(service, m):
    service.users().messages().modify(userId='me', id=m['id'], body={'removeLabelIds': ['UNREAD']}).execute()
    return


def mac_address():
    send_mail("mac:", hex(uuid.getnode()))
    return

def Connect():
    while True:
        cmd = read_mail()
        # if "QUIT" in msg:
        #     client.close()
        #     s.close()
        #     return
        if "mac" in cmd:
            mac_address()
        # elif "KEYLOG" in msg:
        #     keylogger()
        # elif "DIRECTORY" in msg:
        #     directory_tree()
        # elif "LIVESCREEN" in msg:
        #     live_screen()
        # elif "APP_PRO" in msg:
        #     app_process()       
        # elif "REGISTRY" in msg:
        #     registry()
        # elif "SD_LO" in msg:
        #     shutdown_logout() 
        time.sleep(10)


# def create_window():
#     # create Tk
#     root = tk.Tk()
#     # set window size
#     root.geometry("200x200")
#     # set name
#     root.title("Server")
#     # set background color #B4E4FF
#     root['bg'] = '#B4E4FF'

#     # create button OPEN
#     tk.Button(root, text = "OPEN", width = 10, height = 2, fg = '#FFFFFF', bg = '#2B3467', 
#         borderwidth=0, highlightthickness=0, command = Connect, relief="flat").place(x = 100, y = 100, anchor = "center")
    
#     # Vòng lặp chạy chương trình
#     root.mainloop()


# create_window()
if __name__ == '__main__':
    Connect()
    # while True:
    #     read_mail()
    #     time.sleep(10)

# https://skillshats.com/blogs/send-and-read-emails-with-gmail-api/ link có hết
#https://www.youtube.com/watch?v=HNtPG5ltFf8
#https://developers.google.com/gmail/api/guides/labels