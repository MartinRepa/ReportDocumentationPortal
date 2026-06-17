from flask import Flask, request, render_template, jsonify
import pyodbc
import configparser
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    db_config = config['database']

    connection = pyodbc.connect(
        f"DRIVER={db_config['driver']};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={os.getenv('USER')};"
        f"PWD={os.getenv('PASSWORD')};"
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
        cursor.execute("SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorDepartment=? AND ReportTitle=?", (RequestorDepartment, ReportTitle))
    elif RequestorDepartment:
        cursor.execute("SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorDepartment=?", (RequestorDepartment,))
    elif ReportTitle:
        cursor.execute("SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList WHERE ReportTitle=?", (ReportTitle,))
    else:
        cursor.execute("SELECT DISTINCT RequestorName FROM BI_REPORT_MONITOR.dbo.ReportList")

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
        cursor.execute("SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=? AND ReportTitle=?", (RequestorName, ReportTitle))
    elif RequestorName:
        cursor.execute("SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=?", (RequestorName,))
    elif ReportTitle:
        cursor.execute("SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList WHERE ReportTitle=?", (ReportTitle,))
    else:
        cursor.execute("SELECT DISTINCT RequestorDepartment FROM BI_REPORT_MONITOR.dbo.ReportList")

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
        cursor.execute("SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=? AND RequestorDepartment=?", (RequestorName, RequestorDepartment))
    elif RequestorName:
        cursor.execute("SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=?", (RequestorName,))
    elif RequestorDepartment:
        cursor.execute("SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorDepartment=?", (RequestorDepartment,))
    else:
        cursor.execute("SELECT DISTINCT ReportTitle FROM BI_REPORT_MONITOR.dbo.ReportList")

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
    cursor.execute(
        "SELECT * FROM BI_REPORT_MONITOR.dbo.ReportList WHERE RequestorName=? AND RequestorDepartment=? AND ReportTitle=?",
        (RequestorName, RequestorDepartment, ReportTitle)
    )
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    connection.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True, port=8088)
