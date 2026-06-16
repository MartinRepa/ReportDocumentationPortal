from flask import Flask, request, render_template, jsonify
import pyodbc
import configparser
from decode_var import decode_cred
import os
import sys
from dotenv import load_dotenv                                                
import os

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_requestor_name')
def get_requestor_name():
    RequestorDepartment = request.args.get('RequestorDepartment')
    ReportTitle = request.args.get('ReportTitle')
    connection = get_db_connection()
    cursor = connection.cursor()
    
    
    if RequestorDepartment and ReportTitle:
        query = "SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorDepartment=? AND ReportTitle=?"
        cursor.execute(query, (RequestorDepartment, ReportTitle))
    elif RequestorDepartment:
        query = "SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorDepartment=?"
        cursor.execute(query, (RequestorDepartment,))
    elif ReportTitle:
        query = "SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList WHERE ReportTitle=?"
        cursor.execute(query, (ReportTitle,))
    else:
        query = "SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList"
        cursor.execute(query)
    
    names = [row[0] for row in cursor.fetchall()]
    connection.close()
    return jsonify(names)

@app.route('/get_requestor_department')
def get_requestor_department():
    RequestorName = request.args.get('RequestorName')
    ReportTitle = request.args.get('ReportTitle')
    
    connection = get_db_connection()
    cursor = connection.cursor()
    
    if RequestorName and ReportTitle:
        query = "SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=? AND ReportTitle=?"
        cursor.execute(query, (RequestorName, ReportTitle))
    elif RequestorName:
        query = "SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=?"
        cursor.execute(query, (RequestorName,))
    elif ReportTitle:
        query = "SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList WHERE ReportTitle=?"
        cursor.execute(query, (ReportTitle,))
    else:
        query = "SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList"
        cursor.execute(query)
    
    departments = [row[0] for row in cursor.fetchall()]
    connection.close()
    return jsonify(departments)

@app.route('/get_report_title')
def get_report_title():
    RequestorName = request.args.get('RequestorName')
    RequestorDepartment = request.args.get('RequestorDepartment')
    connection = get_db_connection()
    cursor = connection.cursor()
    
    if RequestorName and RequestorDepartment:
        query = "SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=? AND RequestorDepartment=?"
        cursor.execute(query, (RequestorName, RequestorDepartment))
    elif RequestorName:
        query = "SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=?"
        cursor.execute(query, (RequestorName,))
    elif RequestorDepartment:
        query = "SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorDepartment=?"
        cursor.execute(query, (RequestorDepartment,))
    else:
        query = "SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList"
        cursor.execute(query)
    
    titles = [row[0] for row in cursor.fetchall()]
    connection.close()
    return jsonify(titles)



@app.route('/search', methods=['GET'])
def search():
    RequestorName = request.args.get('RequestorName')
    RequestorDepartment = request.args.get('RequestorDepartment')
    ReportTitle = request.args.get('ReportTitle')
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM BI_REPORT_MONITOR.dbo.ReportList 
               WHERE RequestorName=? AND RequestorDepartment=? AND ReportTitle=?"""
    cursor.execute(query, (RequestorName, RequestorDepartment, ReportTitle))
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    connection.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, port=8088)

