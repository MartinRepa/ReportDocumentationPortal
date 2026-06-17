import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'dummy.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS ReportList')

cursor.execute('''
    CREATE TABLE ReportList (
        ReportID            INTEGER PRIMARY KEY AUTOINCREMENT,
        RequestorName       TEXT,
        RequestorDepartment TEXT,
        RequestorEmail      TEXT,
        RequestorPosition   TEXT,
        RequestDate         TEXT,
        ReportTitle         TEXT,
        ReportDescription   TEXT,
        ReportRequirements  TEXT,
        RequestType         TEXT,
        ReportPurpose       TEXT,
        DeliveryDate        TEXT,
        StaffData           TEXT,
        DataSources         TEXT,
        DataFields          TEXT,
        Filters             TEXT,
        AgentName           TEXT,
        AgentEmail          TEXT,
        AgentPosition       TEXT,
        DeliveredBy         TEXT,
        SharepointLink      TEXT
    )
''')

dummy_data = [
    (
        'Alice Johnson', 'Finance', 'alice.johnson@company.com', 'Finance Manager',
        '2024-01-10', 'Monthly Budget Report',
        'Summary of monthly budget vs actuals across all departments.',
        'Include variance analysis and YTD comparison.',
        'New Report', 'Budget oversight and cost control',
        '2024-01-31', 'No',
        'ERP System, GL Database', 'Department, CostCenter, BudgetAmount, ActualAmount, Variance',
        'Month=January 2024, FiscalYear=2024',
        'Carlos Rivera', 'carlos.rivera@company.com', 'BI Developer',
        'Carlos Rivera', 'https://sharepoint.company.com/sites/BI/Reports/MonthlyBudget'
    ),
    (
        'Bob Smith', 'IT', 'bob.smith@company.com', 'IT Director',
        '2024-01-18', 'Server Uptime Report',
        'Weekly report on server availability and downtime incidents.',
        'Break down by server name, incident type, and duration.',
        'Recurring', 'Infrastructure monitoring and SLA compliance',
        '2024-01-25', 'No',
        'Monitoring Tool, Incident DB', 'ServerName, UptimePct, DowntimeMinutes, IncidentType',
        'Week=3, Year=2024',
        'Maria Nguyen', 'maria.nguyen@company.com', 'Data Analyst',
        'Maria Nguyen', 'https://sharepoint.company.com/sites/BI/Reports/ServerUptime'
    ),
    (
        'Carol White', 'HR', 'carol.white@company.com', 'HR Business Partner',
        '2024-02-01', 'Headcount Report',
        'Quarterly headcount breakdown by department and employment type.',
        'Include full-time, part-time, and contractor counts.',
        'New Report', 'Workforce planning and budget allocation',
        '2024-02-15', 'Yes',
        'HRIS System', 'Department, EmployeeType, Headcount, OpenPositions',
        'Quarter=Q1 2024',
        'Carlos Rivera', 'carlos.rivera@company.com', 'BI Developer',
        'Carlos Rivera', 'https://sharepoint.company.com/sites/BI/Reports/Headcount'
    ),
    (
        'Alice Johnson', 'Finance', 'alice.johnson@company.com', 'Finance Manager',
        '2024-02-08', 'Q1 Revenue Report',
        'Revenue breakdown by product line and region for Q1.',
        'Include MoM trend and comparison to Q1 prior year.',
        'Recurring', 'Executive reporting and investor relations',
        '2024-04-05', 'No',
        'CRM, ERP System', 'ProductLine, Region, Revenue, PriorYearRevenue, Growth',
        'Quarter=Q1 2024, Region=All',
        'Maria Nguyen', 'maria.nguyen@company.com', 'Data Analyst',
        'Maria Nguyen', 'https://sharepoint.company.com/sites/BI/Reports/Q1Revenue'
    ),
    (
        'David Lee', 'Sales', 'david.lee@company.com', 'Sales Manager',
        '2024-02-14', 'Sales Pipeline Report',
        'Open opportunities by stage, region, and assigned rep.',
        'Show probability-weighted forecast and close date distribution.',
        'New Report', 'Sales forecasting and pipeline management',
        '2024-02-28', 'No',
        'CRM (Salesforce)', 'OpportunityName, Stage, Region, Rep, Amount, CloseDate',
        'Status=Open, FiscalYear=2024',
        'Carlos Rivera', 'carlos.rivera@company.com', 'BI Developer',
        'Carlos Rivera', 'https://sharepoint.company.com/sites/BI/Reports/SalesPipeline'
    ),
    (
        'Carol White', 'HR', 'carol.white@company.com', 'HR Business Partner',
        '2024-03-01', 'Turnover Report',
        'Employee turnover rate by department and quarter.',
        'Include voluntary vs involuntary separation breakdown.',
        'Recurring', 'Retention strategy and HR planning',
        '2024-03-15', 'Yes',
        'HRIS System, Exit Survey DB', 'Department, TurnoverRate, VoluntarySep, InvoluntarySep',
        'Quarter=Q1 2024',
        'Maria Nguyen', 'maria.nguyen@company.com', 'Data Analyst',
        'Maria Nguyen', 'https://sharepoint.company.com/sites/BI/Reports/Turnover'
    ),
]

cursor.executemany('''
    INSERT INTO ReportList (
        RequestorName, RequestorDepartment, RequestorEmail, RequestorPosition,
        RequestDate, ReportTitle, ReportDescription, ReportRequirements,
        RequestType, ReportPurpose, DeliveryDate, StaffData,
        DataSources, DataFields, Filters,
        AgentName, AgentEmail, AgentPosition, DeliveredBy, SharepointLink
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', dummy_data)

conn.commit()
conn.close()

print(f"Dummy DB created at: {DB_PATH}")
print(f"Inserted {len(dummy_data)} rows into ReportList.")
