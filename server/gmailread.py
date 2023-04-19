from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import email
import base64
import os
from bs4 import BeautifulSoup

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
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
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:/Users/Admin/Documents/GitHub/remote-control/server/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next runserver\credentials.json
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().messages().list(userId='me').execute()
        mes = results.get('messages', [])
        if not mes:
            print("No messages found.")
        else:
            for m in mes:
                msg = service.users().messages().get(userId='me', id=m['id']).execute()
                body_data = msg['payload']['body'].get('data', '')
                msg_str = base64.urlsafe_b64decode(body_data.encode('UTF-8')).decode('UTF-8')
                # msg_str = base64.urlsafe_b64decode(msg['payload']['body']['data'].encode('UTF-8')).decode('UTF-8')
                mime_msg = email.message_from_string(msg_str)
                print(f"Message snippet: {msg['snippet']}")
                print(f"From: {mime_msg['From']}")
                print(f"To: {mime_msg['To']}")
                print(f"Subject: {mime_msg['Subject']}")
                print(f"Date: {mime_msg['Date']}")
                if mime_msg.is_multipart():
                    for part in mime_msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        if "attachment" in content_disposition:
                            filename = part.get_filename()
                            if filename:
                                # Lưu tập tin đính kèm
                                if not os.path.isdir("attachments"):
                                    os.mkdir("attachments")
                                filepath = os.path.join("attachments", filename)
                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                        else:
                            # In ra phần thân của tin nhắn
                            body = part.get_payload(decode=True).decode('utf-8')
                            if content_type == "text/plain":
                                print(f"Message body (plain text): {body}")
                            elif content_type == "text/html":
                                # Parse nội dung HTML và in ra phần thân của tin nhắn
                                soup = BeautifulSoup(body, 'html.parser')
                                print(f"Message body (HTML): {soup.get_text()}")
                else:
                    # In ra phần thân của tin nhắn
                    body = mime_msg.get_payload(decode=True).decode('utf-8')
                    print(f"Message body (plain text): {body}")
                print("------------------------------------------------------------------\n\n\n")
        # results = service.users().labels().list(userId='me').execute()
        # labels = results.get('labels', [])      
        # if not mes:
        #     print("no")
        # else:
        #     for m in mes:
        #         msg = service.users().messages().get(userId='me', id=m['id']).execute()
        #         print(msg['snippet']) #noi dung
        #         headers = msg['payload']['headers']
        #         for header in headers:
        #             if header['name'] == 'From':
        #                 sender_name = header['value']
        #                 print(sender_name)
        #                 break

        #         print("------------------------------------------------------------------\n\n\n")
        # if not mes:
        #     print('No labels found.')
        #     return
        # print('Labels:')
        # for label in mes:
        #     print(label['name'])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()

#https://www.youtube.com/watch?v=HNtPG5ltFf8
#https://developers.google.com/gmail/api/guides/labels