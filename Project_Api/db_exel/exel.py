from google.oauth2 import service_account
import gspread

# Define los alcances (scopes)
scopes = ['https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']

# Ruta al archivo de credenciales
KEY = 'db_exel/key.json'
SPREADSHEET_ID = '1J7x99lFJr5huXOT_yTLXGIyOzDivY8b9Qb5FYNjmhDA'

# Carga las credenciales desde el archivo JSON
creds = service_account.Credentials.from_service_account_file(KEY, scopes=scopes)

# Autoriza gspread con las credenciales
client = gspread.authorize(creds)

# Abre la hoja de cálculo por ID
sheet = client.open_by_key(SPREADSHEET_ID)

# Selecciona la hoja de trabajo específica por nombre
worksheet = sheet.worksheet('Sheet1')  # Asegúrate de que 'Sheet1' es el nombre correcto de la hoja

class Exel:
    def registerAttendance(values):
        # Añadir los valores a partir de la celda 'A1'
        worksheet.append_rows(values, value_input_option='USER_ENTERED')
        print(f"Datos insertados correctamente en {len(values)} filas.")
