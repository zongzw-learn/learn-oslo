'''
# pylint error for relative import.
import tables
from tables import User
from cfgopts import DBCfg
'''
from oslo_utils import importutils
tables = importutils.import_module('tables')
User = importutils.import_class('tables.User')
DBCfg = importutils.import_class('cfgopts.DBCfg')

from oslo_db.sqlalchemy import enginefacade

tables.create_all()

'''
# TypeError: this TransactionFactory is already started

enginefacade.configure(
    connection=DBCfg.get_dbconn()
)
'''

@enginefacade.transaction_context_provider
class MyContext(object):
    'User-defined context class.'

@enginefacade.reader
def some_reader_api_function(context):
    return context.session.query(User).all()

@enginefacade.writer
def some_writer_api_function(context, name, full, pawd):
    u = User(name=name, fullname=full, password=pawd)
    context.session.add(u)

def run_some_database_calls():
    context = MyContext()
    some_writer_api_function(context, 'zong', "andrew zong", 'passw0rd')

    results = some_reader_api_function(context)
    print(results)

run_some_database_calls()