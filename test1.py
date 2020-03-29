from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas as pd

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1tYfD3vvSEaW3Cq9-UZoDtlKIfaMMVJq8XnV9XJUdK3s'
SAMPLE_RANGE_NAME = 'Events'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()

    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s' % (row[0], row[4]))
            print(row)

    values = [
        ['Country', 'ISO Code', 'Region', 'ADM1', 'Affected Pop Share', 'Type', 'Meta (e.g. group size thresholds',
         'Start', 'End', 'Source', 'Comment'],
        ['English', 'ISO 3166-2', '', 'Nationwide=Empty\nRegional=Use ADM1-codes (sheet)',
         'Esimate of affected population, if a measure is below ADM1 level (e.g. city).', 'Refer to instructions sheet',
         'Meta information', 'First day the measure was active', 'Last day the measure was active', 'Link'],
        ['Belgium', 'BE', '', '', '1,00', 'Border Closing', '', '20.3.2020', '',
         'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Belgium'],
    ]

    column_names = values.pop(0)
    df = pd.DataFrame(
        [row + [''] * (len(column_names) - len(row)) for row in values],
        columns=column_names
    )

    print(df)

if __name__ == '__main__':
    main()