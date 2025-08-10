from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import json

Base = declarative_base()
engine = create_engine('sqlite:///queries.db')
Session = sessionmaker(bind=engine)

class QueryLog(Base):
    __tablename__ = 'query_log'
    id = Column(Integer, primary_key=True)
    case_type = Column(String)
    case_number = Column(String)
    filing_year = Column(String)
    result_json = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

def setup_db():
    Base.metadata.create_all(engine)

def log_query(case_type, case_number, filing_year, result):
    session = Session()
    log = QueryLog(
        case_type=case_type,
        case_number=case_number,
        filing_year=filing_year,
        result_json=json.dumps(result)
    )
    session.add(log)
    session.commit()