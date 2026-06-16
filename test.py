from flask import Flask, request, render_template, jsonify
import pyodbc
import configparser
from decode_var import decode_cred
import os
import sys

sys.path.append('C:\\PythonProjects\\pr_ReportDocumentationPortal')

user = 'ReportDocumentationPortalUser'
password = 'TiranaBank2024@MR'

app = Flask(__name__)

def get_db_connection():

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__),'config.ini'))
    db_config = config['database']
    return db_config

print(get_db_connection())
config = configparser.ConfigParser()
print(config.read(os.path.join(os.path.dirname(__file__),'config.ini')))