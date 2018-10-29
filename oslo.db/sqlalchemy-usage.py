'''
from 
    https://www.jianshu.com/p/0d234e14b5d3

good article.

'''

# connection 

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True)
    name = Column(String) 
    fullname = Column(String) 
    password = Column(String) 
    
    def __repr__(self): 
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


print(User.__table__)

Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

# session operation

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

'''
Session = sessionmaker()
Session.configure(bind=engine)  # once engine is available
'''

session = Session()

session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first() 
#BEGIN (implicit) INSERT INTO users (name, fullname, password) VALUES (?, ?, ?) ('ed', 'Ed Jones', 'edspassword')

print(our_user)

session.add_all(
    [ 
        User(name='wendy', fullname='Wendy Williams', password='foobar'), 
        User(name='mary', fullname='Mary Contrary', password='xxg527'), 
        User(name='fred', fullname='Fred Flinstone', password='blah')
    ]
)

ed_user.password = 'f8s7ccs'

print(session.dirty)
print(session.new)

session.commit()

# query

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)

from sqlalchemy.orm import aliased
user_alias = aliased(User, name='user_alias')
for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)

for u in session.query(User).order_by(User.id)[1:3]:
    print(u)

for name, in session.query(User.name).\
        filter_by(fullname='Ed Jones'):
    print(name)

for user in session.query(User).\
        filter(User.name=='ed').\
        filter(User.fullname=='Ed Jones'):
    print(user)

# sql statement

from sqlalchemy import text
for user in session.query(User).\
        filter(text("id<224")).\
        order_by(text("id")).all():
    print(user.name)

print(session.query(User).filter(text("id<:value and name=:name")).\
    params(value=224, name='fred').order_by(User.id).one())

print(session.query(User).from_statement(
                text("SELECT * FROM users where name=:name")).\
                params(name='ed').all())

# counting

print(session.query(User).filter(User.name.like('%ed')).count())

from sqlalchemy import func
print(session.query(func.count(User.name), User.name).group_by(User.name).all())

print(session.query(func.count('*')).select_from(User).scalar())

print(session.query(func.count(User.id)).scalar())

# relationship
