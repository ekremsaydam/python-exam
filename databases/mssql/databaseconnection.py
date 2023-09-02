"""MSSQL işlemleri."""
import pandas as pd
import pyodbc  # pip install pyodbc
import sqlalchemy as sa  # pip install SQLAlchemy
from sqlalchemy.engine import URL, create_engine
SERVER = r'tcp:192.168.10.100\BEDB'
DATABASE = 'AdventureWorks2016'
USERNAME = 'sa'
PASSWORD = 'Password1'
CONN = ('DRIVER={SQL Server}'
        + ';SERVER=' + SERVER
        + ';DATABASE=' + DATABASE
        + ';ENCRYPT=no;UID=' + USERNAME
        + ';PWD=' + PASSWORD)

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": CONN})
engine = create_engine(connection_url)
# Sample select query
QUERY = "SELECT * FROM Production.Product"

with engine.begin() as conn:
    df = pd.read_sql_query(sa.text(QUERY), conn)
# print(df.head())

SERVER2 = r'tcp:192.168.10.100\BEDB'
DATABASE2 = 'AdventureWorks2016'
USERNAME2 = 'sa'
PASSWORD2 = 'Password1'
cnxn = pyodbc.connect('DRIVER={SQL Server}'
                      + ';SERVER=' + SERVER2
                      + ';DATABASE=' + DATABASE2
                      + ';ENCRYPT=no;UID=' + USERNAME2
                      + ';PWD=' + PASSWORD2)
cursor = cnxn.cursor()

QUERY = """
"""
