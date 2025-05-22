import pandas as pd
from datetime import datetime

# Read the Excel file
file_path = 'Bir Yıllık.xlsx'
df = pd.read_excel(file_path)

def convert_date(date_str):
    try:
        # Example: 'Fri May 17 23:59:17 +0000 2024'
        dt = datetime.strptime(str(date_str), '%a %b %d %H:%M:%S %z %Y')
        return dt.strftime('%Y-%m-%d')
    except Exception:
        return date_str  # Return as is if parsing fails

if 'Date' in df.columns:
    df['Date'] = df['Date'].apply(convert_date)
    df.to_excel("Bir Yıllık_v1.xlsx", index=False)
    print('Date column converted to YYYY-MM-DD format.')
else:
    print('No Date column found in the file.')

