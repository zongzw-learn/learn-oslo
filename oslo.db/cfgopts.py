from oslo_db.sqlalchemy import enginefacade
from oslo_config import cfg

class DBCfg:
    CONF = cfg.CONF
    dbconn = None

    db_opts = [
        cfg.StrOpt('connection',
                help='The SQLAlchemy connection string to use to connect to '
                        'the Nova API database.',
                secret=True),
        cfg.BoolOpt('sqlite_synchronous',
                    default=True,
                    help='If True, SQLite uses synchronous mode.'),
        cfg.StrOpt('slave_connection',
                secret=True,
                help='The SQLAlchemy connection string to use to connect to the'
                        ' slave database.'),
        cfg.StrOpt('mysql_sql_mode',
                default='TRADITIONAL',
                help='The SQL mode to be used for MySQL sessions. '
                        'This option, including the default, overrides any '
                        'server-set SQL mode. To use whatever SQL mode '
                        'is set by the server configuration, '
                        'set this to no value. Example: mysql_sql_mode='),
        cfg.IntOpt('idle_timeout',
                default=3600,
                help='Timeout before idle SQL connections are reaped.'),
        cfg.IntOpt('max_pool_size',
                help='Maximum number of SQL connections to keep open in a '
                        'pool.'),
        cfg.IntOpt('max_retries',
                default=10,
                help='Maximum number of database connection retries '
                        'during startup. Set to -1 to specify an infinite '
                        'retry count.'),
        cfg.IntOpt('retry_interval',
                default=10,
                help='Interval between retries of opening a SQL connection.'),
        cfg.IntOpt('max_overflow',
                help='If set, use this value for max_overflow with '
                        'SQLAlchemy.'),
        cfg.IntOpt('connection_debug',
                default=0,
                help='Verbosity of SQL debugging information: 0=None, '
                        '100=Everything.'),
        cfg.BoolOpt('connection_trace',
                    default=False,
                    help='Add Python stack traces to SQL as comment strings.'),
        cfg.IntOpt('pool_timeout',
                help='If set, use this value for pool_timeout with '
                        'SQLAlchemy.'),
    ]

    @classmethod
    def get_dbconn(cls):
        if not cls.dbconn:
            cls.CONF.register_opts(cls.db_opts, 'database')
            cls.CONF(default_config_files=['database.conf'])
            cls.dbconn = cls.CONF.database.connection
            cls.CONF.reset()
            cls.CONF.unregister_opts(cls.db_opts, 'database')

        return cls.dbconn

if __name__ == "__main__":
    dbconn = DBCfg.get_dbconn()
    print(dbconn)
