"""DB connection."""
from sqlalchemy import URL, create_engine, text
import pandas as pd

server = r'tcp:192.168.10.100\BEDB'
database = 'AdventureWorks2016'
username = 'sa'
password = 'Password1'

connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server}'
    + ';SERVER=' + server
    + ';DATABASE=' + database
    + ';UID=' + username
    + ';PWD=' + password
    + ';ENCRYPT=yes'
    + ';TrustServerCertificate=yes'
    + ';Connection Timeout=3;'
)
connection_url = URL.create(
    'mssql+pyodbc',
    query={'odbc_connect': connection_string})

engine = create_engine(connection_url,
                       echo=False,
                       fast_executemany=True)
# with engine.connect() as conn:
#     rows = conn.execute(text("SELECT * FROM Production.Product")).fetchall()

# print(rows[:5])
QUERY = 'SELECT * FROM Production.Product'
with engine.begin() as conn:
    df = pd.read_sql_query(text(QUERY), conn)
    df.to_sql(name='Product2',
              con=conn,
              schema='Production',
              if_exists='append',
              index=True)

print(df.head())
