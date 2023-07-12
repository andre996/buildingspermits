import requests
import pandas as pd
import pyodbc
from sqlalchemy import create_engine, select, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import urllib
Base = declarative_base()

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


class Buildings(Base):
    __tablename__ = 'buildings'

    column1 = Column('column1', Integer, primary_key=True)
    externalfilenum = Column('externalfilenum', String)
    jobtypedescription = Column('jobtypedescription', String)
    address = Column('address',String)
    issuedate = Column('issuedate',String)
    inspectiontype = Column('inspectiontype',String)
    fulldeficiency = Column('fulldeficiency',String)
    outcome = Column('outcome',String)
    inspectioncompleteddate =Column('inspectioncompleteddate',String)
    disciplinetype = Column('disciplinetype',String)
    general_contractor = Column('general_contractor',String)
    checklist = Column('checklist',String)
    statusname = Column('statusname',String)
    deficiencies = Column('deficiencies',String)
    x_coord = Column('x_coord', Float)
    y_coord = Column('y_coord', Float)
    processid = Column('processid', String)
    point = Column('point', String)
    computed_region_qeuu_piif = Column('computed_region_qeuu_piif', Integer)
    computed_region_xxr9_iwz2 = Column('computed_region_xxr9_iwz2', Integer)
    deficiencyresolved = Column('deficiencyresolved', String)
    resolveddate = Column('resolveddate', String)
    permitclosedate = Column('permitclosedate', String)
    permitholder =Column('permitholder', String)

    def __init__(self,externalfilenum,jobtypedescription,address,issuedate,inspectiontype,fulldeficiency,outcome,inspectioncompleteddate,disciplinetype,general_contractor,checklist,statusname,deficiencies,x_coord,y_coord,processid,point,computed_region_qeuu_piif,computed_region_xxr9_iwz2,deficiencyresolved,resolveddate,permitclosedate,permitholder):

        self.column1 = column1 
        self.externalfilenum = externalfilenum
        self.jobtypedescription = jobtypedescription
        self.address = address
        self.issuedate = issuedate
        self.inspectiontype = inspectiontype
        self.fulldeficiency =fulldeficiency
        self.outcome = outcome
        self.inspectioncompleteddate = inspectioncompleteddate
        self.disciplinetype = disciplinetype
        self.general_contractor = general_contractor
        self.checklist = checklist
        self.statusname = statusname
        self.deficiencies = deficiencies
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.processid = processid
        self.point = point
        self.computed_region_qeuu_piif = computed_region_qeuu_piif
        self.computed_region_xxr9_iwz2 = computed_region_xxr9_iwz2
        self.deficiencyresolved = deficiencyresolved
        self.resolveddate = resolveddate
        self.permitclosedate = permitclosedate
        self.permitholder = permitholder

    def __rep__(self):
        return f'''( 
            {self.column1}
            {self.externalfilenum}
            {self.jobtypedescription}
            {self.address}
            {self.issuedate}
            {self.inspectiontype}
            {self.fulldeficiency}
            {self.outcome}
            {self.inspectioncompleteddate}
            {self.disciplinetype}
            {self.general_contractor}
            {self.checklist}
            {self.statusname}
            {self.deficiencies}
            {self.x_coord}
            {self.y_coord}
            {self.processid}
            {self.point}
            {self.computed_region_qeuu_piif}
            {self.computed_region_xxr9_iwz2}
            {self.deficiencyresolved}
            {self.resolveddate}
            {self.permitclosedate}
            {self.permitholder}
        )'''

# Check videos How to connect an Azure database
engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(params), echo=True) 

Session = sessionmaker(bind=engine)
session = Session()
result = session.query(Buildings).all()
print('connection is ok')

for r in result:
    print(r)

# r = requests.get('https://data.calgary.ca/resource/8ced-xbvn.json')
# df = pd.read_json(json.dumps(r.json()))
