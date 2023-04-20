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

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    'https://www.googleapis.com/auth/gmail.readonly'
]


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
        mes = results.get('messages', [])
        if not mes:
            print("No letter find out")
        else:
            for m in mes:
                 # Call the Gmail v1 API, retrieve message data.
                message = service.users().messages().get(userId='me', id=m['id'], format='raw').execute()

                get_info_message(message)

                # Mark read letter from gmail
                mark_as_read(service, m)
                #print('Message snippet: %s' % message['snippet'])  #do gửi qua chuỗi ngắn --> làm oke chứ chuỗi dài thì khó
                print("------------------------------------------------------------------\n\n\n")

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
def get_info_message(message):
    # Parse the raw message.
    mime_msg = email.message_from_bytes(base64.urlsafe_b64decode(message['raw']))

    print('from', mime_msg['from'])
    print('to', mime_msg['to'])
    print('subject', mime_msg['subject'])
    print("----------------------------------------------------")
def mark_as_read(service, m):
    service.users().messages().modify(userId='me', id=m['id'], body={'removeLabelIds': ['UNREAD']}).execute()
    return

if __name__ == '__main__':
    while True:

        read_mail()
        time.sleep(10)

# https://skillshats.com/blogs/send-and-read-emails-with-gmail-api/ link có hết
#https://www.youtube.com/watch?v=HNtPG5ltFf8
#https://developers.google.com/gmail/api/guides/labels