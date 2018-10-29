
'''
pip install -U SQLAlchemy===1.0.11

by default installation: 1.2.12 

>>> from sqlalchemy import events
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/zong/PythonEnvs/oslo-env/lib/python2.7/site-packages/sqlalchemy/__init__.py", line 9, in <module>
    from .sql import (
ImportError: cannot import name events

'''

from oslo_db.sqlalchemy import session
from oslo_db.sqlalchemy import enginefacade

class SomeClass:
    pass

@enginefacade.transaction_context_provider
class MyContext(object):
    '''my cnotext'''

context = enginefacade.transaction_context()
print(type(context.connection))

@enginefacade.reader
def some_reader_api_function(context):
    return context.session.query(SomeClass).all()

@enginefacade.writer
def some_writer_api_function(context, x, y):
    context.session.add(SomeClass(x, y))


def run_some_database_calls():
    context = MyContext()

    results = some_reader_api_function(context)
    some_writer_api_function(context, 5, 10)
    print(results)

'''
@enginefacade.reader.connection
def _refresh_from_db(context, cache):
    sel = sa.select([table.c.id, table.c.name])
    res = context.connection.execute(sel).fetchall()
    cache.id_cache = {r[1]: r[0] for r in res}
    cache.str_cache = {r[0]: r[1] for r in res}
'''