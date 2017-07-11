# google api usage

## spread sheet

```
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread-april-2cd … ba4.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Where is the money Lebowski?").sheet1
```

https://developers.google.com/sheets/api/quickstart/python
https://github.com/burnash/gspread
