from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, MetaData

from cfgopts import DBCfg

Base = declarative_base()

# way 1 to declare table
class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True)
    name = Column(String) 
    fullname = Column(String) 
    password = Column(String) 
    
    def __repr__(self): 
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)

# way 2 to declare table
from oslo_db.sqlalchemy import enginefacade
enginefacade.configure(
    connection=DBCfg.get_dbconn()
)

engine = enginefacade.writer.get_engine()

metadata = MetaData(bind=engine)

numbers = Table("numbers", metadata, Column('num', Integer))
strings = Table('strings', metadata, Column('str', String))

def create_all():
    numbers.create(checkfirst=True)
    strings.create(checkfirst=True)

    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_all()