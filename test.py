from flask import Flask, request, render_template, jsonify
import pyodbc
import configparser
from decode_var import decode_cred
import os
import sys
from dotenv import load_dotenv                                                
import os

load_dotenv()

sys.path.append('C:\\PythonProjects\\pr_ReportDocumentationPortal')

user = os.getenv("USER")
password = os.getenv("PASSWORD")

app = Flask(__name__)

def get_db_connection():

 

    config = configparser.ConfigParser()

    config.read(os.path.join(os.path.dirname(__file__),'config.ini'))

    db_config = config['database']

 

    connection = pyodbc.connect(

        f"DRIVER={db_config['DRIVER']};"

        f"SERVER={db_config['SERVER']};"

        f"DATABASE={db_config['DATABASE']};"

        f"user={user};"

        f"password={password}"          

    )

    return connection

 

connection = get_db_connection()

cursor = connection.cursor()

query = "SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList"

 

cursor.execute(query)

 

rows = cursor.fetchall()

 

for row in rows:

    print(row)

 

connection.close()

