import requests
import pandas as pd
import pyodbc
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
import urllib

# Azure has connection window  where you can get this properties
params = urllib.parse.quote_plus(
    'driver=%s;' % '{ODBC Driver 18 for SQL Server}' +
    'Server=tcp:%s;' % 'plotlyserver.database.windows.net,1433' +
    'database=%s;' % 'plotlyOnboarding' +
    'UID=%s;' % 'plotlyadimn' +
    'PWD={%s};' % 'Plotly1234' + # DO TO: should be hide
    'Encrypt=yes;' +
    'TrustServerCertificate=no;' +
    'Connection Timeout=50;')



# Check videos How to connect an Azure database
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(params), echo=True) 
Session = sessionmaker(bind=engine)

with Session() as session:
    statement = select(buildings)
    user_obj = session.execute(statement)
    print(user_obj)

print('connection is ok')

# r = requests.get('https://data.calgary.ca/resource/8ced-xbvn.json')
# df = pd.read_json(json.dumps(r.json()))
