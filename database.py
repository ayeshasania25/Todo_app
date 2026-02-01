from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url="postgresql://postgres:Haniya@1" \
"@localhost:5432/TestDB"
engine=create_engine(db_url)
Session=sessionmaker( autocommit=False,autoflush=False,bind=engine)