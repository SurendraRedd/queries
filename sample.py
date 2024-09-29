from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def main():
    # Authenticate and create the service
    creds = None
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    # Call the Sheets API
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # Example: Read data from a spreadsheet
    result = sheet.values().get(spreadsheetId='1GwRBEeHnlzZh9tM4NkKzXO8FK0WD6f-e8aRJP9ap04I', range='Sheet1!A1:D10').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            print(', '.join(row))

if __name__ == '__main__':
    main()
