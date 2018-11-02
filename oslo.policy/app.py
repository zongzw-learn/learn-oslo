# -*- coding: utf-8

################## 总结 ##################
'''
关于设计架构：

* 文件列表：
__init__.py		_external.py		fixture.py		opts.py			sphinxext.py		version.py
_cache_handler.py	_i18n.py		generator.py		policy.py		sphinxpolicygen.py
_checks.py		_parser.py		locale			shell.py		tests

* 设计架构：

.json           -->     _parser module      -->   _checks module            --> policy  module

json 文本文件           负责将所有的行转化成规则        定义三种kind，和各种Rule        实现规则的组织Rules，入口函数Enforcer
                        （文本到规则的转化）
'''

'''
关于规则解析：
具体的规则解析过程参见 _parser.py

'''

'''
关于使用方法：
两种方法实现规则的加载。
1. 手动加载，自己生成Rules对象，传递给Enforcer
2. 使用Enforcer自动加载，和CONF配合使用。
'''

'''
关于调试过程：
python -m test.py 

曾经被定位过的点：
b /Users/zong/PythonEnvs/oslo-env/lib/python2.7/site-packages/oslo_policy/policy.py:792
 792     def enforce(self, rule, target, creds, do_raise=False, exc=None,
 793                 *args, **kwargs):

b /Users/zong/PythonEnvs/oslo-env/lib/python2.7/site-packages/oslo_policy/_checks.py:333
 290 @register(None)
 291 class GenericCheck(Check):
 ...
 333     def __call__(self, target, creds, enforcer, current_rule=None):
 334

'''

'''
关于命令行：

1. pip install keystone
2. oslopolicy-sample-generator --namespace keystone --format json --output-file policy.json
3. oslopolicy-checker --policy policy.json --access token_admin.json --rule identity:get_project_tag --is_admin=True
   $ passed: identity:get_project_tag

'''

'''
关于文档缺陷：

感觉文档写的不明不白。缺少原理白皮书！

我的期望的oslo_policy 模块 是 

给我提供一个入口，authorize! 
围绕这一个入口：加载规则，验证规则，
构建验证过程所需要的用户信息creds，

出口一个：True or False

没有地方提到creds的类型。自己去找openstack的实现文档。

from /usr/share/openstack-dashboard/openstack_dashboard/policy.py:

 30     """Mixin that adds the get_policy_target function
 31
 32     policy_target_attrs - a tuple of tuples which defines
 33         the relationship between attributes in the policy
 34         target dict and attributes in the passed datum object.
 35         policy_target_attrs can be overwritten by sub-classes
 36         which do not use the default, so they can neatly define
 37         their policy target information, without overriding the
 38         entire get_policy_target function.
 39     """
 40
 41     policy_target_attrs = (("project_id", "tenant_id"),
 42                            ("user_id", "user_id"),
 43                            ("domain_id", "domain_id"),
 44                            ("target.project.domain_id", "domain_id"),
 45                            ("target.user.domain_id", "domain_id"),
 46                            ("target.group.domain_id", "domain_id"))
 47
 48     def get_policy_target(self, request, datum=None):
 49         policy_target = {}
 50         for policy_attr, datum_attr in self.policy_target_attrs:
 51             if datum:
 52                 policy_target[policy_attr] = getattr(datum, datum_attr, None)
 53             else:
 54                 policy_target[policy_attr] = None
 55         return policy_target


1263                                "is invalid. It should be one of %(allowed)s")
1264                              % {'feature': feature,
1265                                 'allowed': ' '.join(feature_policies.keys())})
1266         role = (('network', policy_name),)
1267         if not policy.check(role, request):
1268             return False


为什么 没有 register_rule(s), 而只有register_default(s)，导致registered_rules无法通过接口赋值。
为什么没有一个文档告诉我说Enforcer.authorize 就是最终往外提供的接口。 

'''


################## 以下是示例代码 ##################

from oslo_policy import policy
from oslo_config import cfg
from oslo_context import context


'''
演示 规则匹配过程：
result 为True只有当： 
1. ctx.roles = ['admin']
2. ctx.project_id = 'myproject'
3. {'target.project.id': 'myproject'}
即，规则和target会被用来匹配 creds.

ctx = context.RequestContext()
ctx.roles = ['admin']
ctx.project_id = 'myproject'

creds = ctx.to_policy_values()

data = '{"myrule": "project_id:%(target.project.id)s"}'
rules = policy.Rules.load(data)
enforcer = policy.Enforcer(cfg.CONF)
enforcer.set_rules(rules)
enforcer.registered_rules = rules

print(rules.get("myrule"))
print(creds)

result = enforcer.enforce(rules.get("myrule"), {'target.project.id': 'myproject'}, creds)

print(result)

'''

'''
验证最终正确的使用方式，enforcer.enforce(rule(not str), ...)

ctx = context.RequestContext()
ctx.roles = ['admin']
creds = ctx.to_policy_values()

with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    enforcer = policy.Enforcer(cfg.CONF)
    enforcer.set_rules(rules)
    enforcer.registered_rules = rules

    print(rules.get("identity:list_project_tags"))
    print(creds)
    
    result = enforcer.enforce(rules.get("identity:list_project_tags"), {'project': {'id': '23432435345345'}}, creds)

    print(result)

'''

'''
演示另外一种不可以的调用方式，authorize使用BaseCheck 类型调用。他会因为
 972         if rule not in self.registered_rules:
 973             raise PolicyNotRegistered(rule)
 直接报错。

ctx = context.RequestContext()
creds = ctx.to_policy_values()

with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    enforcer = policy.Enforcer(cfg.CONF)
    enforcer.set_rules(rules)
    enforcer.registered_rules = rules

    result = enforcer.authorize(rules.get("identity:list_project_tags"), {}, creds)
    # oslo_policy.policy.PolicyNotRegistered: Policy (rule:admin_required or project_id:%(target.project.id)s) has not been registered
    # 代码中显示 authorize 参数 rule，在这里传入的是OrCheck类型，而其要求是 string类型，以便能判断 if rule in self.registered_rules
    # 烂code！
    
    print(result)
'''

'''
演示一种不可以的调用方式：authorize(<string>, ...)

ctx = context.RequestContext()
creds = ctx.to_policy_values()

with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    enforcer = policy.Enforcer(cfg.CONF)
    enforcer.set_rules(rules)
    enforcer.registered_rules = rules

    result = enforcer.authorize("identity:list_project_tags", {}, creds)
    # *** AttributeError: AttributeError("'OrCheck' object has no attribute 'scope_types'",)
    # 现有BaseCheck中还没有scope_types 1.31版本的RuleDefault中引入。
    # 所以文档中讲，可以使用str 类型的rule 作为authorize 参数，但实际上运行至 enforce函数中的分支时出现问题。
    
    print(result)
'''

'''
演示直接对enforcer.registered_rules 使用Rules 对象赋值。
注意registered_rules 是dict类型，而之所以直接可以用Rules对象赋值是因为Rules的基类就是dict，其内部数据格式也是dict。

with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    # print(type(rules)) rules is a Rules
    enforcer = policy.Enforcer(cfg.CONF)
    enforcer.set_rules(rules)
    enforcer.registered_rules = rules
    # print(enforcer.registered_rules) registered_rules is a dict.

'''

'''
验证 使用context.RequestContext 生成creds

ctx = context.RequestContext()
ctx.roles = ['admin']
ctx.project_id = 'myproject'
data = ctx.to_policy_values()
print(type(data))
import json
print(json.dumps(data._dict, indent=2))

result: 
{
  "service_roles": [],
  "user_id": null,
  "roles": [
    "admin"
  ],
  "system_scope": null,
  "service_project_id": null,
  "service_user_id": null,
  "service_user_domain_id": null,
  "service_project_domain_id": null,
  "is_admin_project": true,
  "user_domain_id": null,
  "project_id": "myproject",
  "project_domain_id": null
}

'''

'''
演示 生成enforcer 对象，并将Rules 对象赋值到enforcer

with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    enforcer = policy.Enforcer(cfg.CONF)
    enforcer.set_rules(rules)
    print(enforcer.rules)

''' 

'''
演示从文件中加载dict，通过Rules.load 生成Rules 类型对象

with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    print(rules)
    rule = rules.get("identity:get_project_tag")
    print(dir(rule))
'''

'''
演示 和cfg.CONF 一起使用.

CONF = cfg.CONF
CONF(['--config-file', 'policy.conf'])

rule_name = 'identity:get_domain'

# 创建enforcer之后需要手动load_rules 才能体现在enforcer.rules中。
enforcer = policy.Enforcer(CONF)
enforcer.load_rules(True)
print("after load_rules: ", enforcer.rules.get(rule_name))

# 通过register_default 可以注册新的规则，这个规则是default，目前理解是当所有都匹配不上的时候会使用default，但是需要重新load_rules。
enforcer.register_default(policy.RuleDefault(name='test', check_str="rule:x or role:test or role:admin"))
enforcer.load_rules(True)
print("registered rules: ", enforcer.registered_rules)
print("after test rule registered: ", enforcer.rules.get('test'))

enforcer.register_default(policy.RuleDefault(name='identity:get_domain', check_str="rule:admin_required or project_id:%(target.project.id)s"))

# 规则的验证过程： 
print("test pass", enforcer.authorize('identity:get_domain', {}, {'roles': ['test']}))
'''
