# -*- coding: utf-8

from oslo_policy import policy
from oslo_config import cfg
from oslo_log import log



CONF = cfg.CONF
CONF(['--config-file', 'policy.conf'])

rule_name = 'identity:get_domain'

# 创建enforcer之后需要手动load_rules 才能体现在enforcer.rules中。
enforcer = policy.Enforcer(CONF)
enforcer.load_rules(True)
print("after load_rules: ", enforcer.rules.get(rule_name))

# 通过register_default 可以注册新的规则，但是需要重新load_rules。
enforcer.register_default(policy.RuleDefault(name='test', check_str="rule:x or role:test or role:admin"))
enforcer.load_rules(True)
print("registered rules: ", enforcer.registered_rules)
print("after test rule registered: ", enforcer.rules.get('test'))

enforcer.register_default(policy.RuleDefault(name='identity:get_domain', check_str="rule:admin_required or project_id:%(target.project.id)s"))

# 规则的验证过程： 
print("test pass", enforcer.authorize('identity:get_domain', {}, {'roles': ['test']}))

creds = '''
{
    "token": {
        "issued_at": "2018-11-01T06:32:45.000000Z",
        "expires": "2018-11-01T07:32:45Z",
        "id": "b5843c0328c3425680c880497d49b56c",
        "tenant": {
            "description": "admin tenant",
            "enabled": true,
            "id": "fde45211da0a44ecbf38cb0b644ab30d",
            "name": "admin"
        },
        "audit_ids": [
            "GDJ6iguWQfWDCKvei-CN9A"
        ],
        "username": "admin",
        "roles_links": [],
        "roles": ["admin"],
        "name": "admin",
        "project": {
            "id": "fde45211da0a44ecbf38cb0b644ab30d"
        }
    }
}
'''

rule = enforcer.rules.get(rule_name)

print(rule)
print(type(rule))

print(enforcer.registered_rules)
#enforcer.register_default(policy.RuleDefault(rule_name, rule))

enforcer.register_default(policy.RuleDefault(name='identity:get_domains', check_str="rule:admin_required or project_id:%(target.project.id)s"))
#print(enforcer.authorize(rule_name, {}, creds))
print(enforcer.authorize(rule_name, {}, creds))

'''
1. pip install keystone
2. oslopolicy-sample-generator --namespace keystone --format json --output-file policy.json
3. oslopolicy-checker --policy policy.json --access token_admin.json --rule identity:get_project_tag --is_admin=True
   $ passed: identity:get_project_tag

'''

'''
感觉文档写的不明不白。

policy 格式现在是清楚了。但是怎么用它不清楚。

验证的过程不清楚。
构建用户token信息不清楚，没有一个地方提到。

我的期望的oslo_policy 模块 是 

给我提供一个入口，authorize! 
围绕这一个入口：加载规则，验证规则，
构建验证过程所需要的用户信息creds，

出口一个：True or False


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