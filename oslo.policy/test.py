# -*- coding: utf-8

from oslo_policy import policy
from oslo_config import cfg
from oslo_context import context

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

ctx = context.RequestContext()
print(ctx.to_policy_values())
'''

'''    
with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    enforcer = policy.Enforcer(cfg.CONF)
    enforcer.set_rules(rules)
    print(enforcer.rules)

''' 

'''
with open("policy.json") as fr:
    data = fr.read()
    rules = policy.Rules.load(data)
    print(rules)
    rule = rules.get("identity:get_project_tag")
    print(dir(rule))
'''