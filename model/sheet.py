import gspread
from oauth2client.service_account import ServiceAccountCredentials

target_insta_id = "merumichandayo"
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/ain/Desktop/Desktop/instaCrolling/model/key.json", scope)
client = gspread.authorize(creds)
sheet = client.open("instaCrawling").worksheet(target_insta_id)

def inputSheet(target_id,insertRow):
        sheet = client.open("instaCrawling").worksheet(target_id)
        sheet.append_row(insertRow)
