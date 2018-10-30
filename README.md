# learn-oslo

A repo for acknowledging OpenStack Common Library: OSLO.

oslo常用组件的一览表

库名 	                                         作用 	                       背景知识
oslo.config 	                                配置文件 	                   无
oslo.utils 	                                    工具库 	                       无
oslo.service 	                                带ssl的REST服务器 	            wsgi
oslo.log + oslo.context 	                    带调用链的日志系统 	             无
oslo.messaging 	                                RPC调用 	                    amqp
oslo.db 	                                    数据库 	                        sqlalchemy
oslo.rootwrap 	                                Linux的sudo 	                无
oslo.serialization 	                            序列化 	                        无
oslo.i18n 	                                    国际化 	                        无
oslo.policy 	                                权限系统 	                    deploy paste
oslo.middleware 	                            pipeline 	                    deploy paste
keystonemiddleware 	                            用户系统 	                    deploy paste + keystone
oslo_test 	                                    测试 	                        unittest
