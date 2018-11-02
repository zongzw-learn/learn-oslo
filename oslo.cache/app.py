from oslo_cache import core as cache
from oslo_cache import _opts

from oslo_config import cfg


CONF = cfg.CONF
_opts.configure(CONF)

CONF(default_config_files=['app.ini'])

print(CONF.cache.backend)
print(CONF.cache.config_prefix)

cache.configure(CONF)

#def key_maker(namespace, fn, **kwargs):
#    return "zongzw_" + namespace + fn.__name__ + kwargs

#region = cache.create_region(function=key_maker)
region = cache.create_region()
cache.configure_cache_region(CONF, region)

mem_decorator = cache.get_memoization_decorator(CONF, region, "cache")

@mem_decorator
def func(arg1, arg2):
    return (arg1, arg2)

func('1', '2')

region.set('1', '2223')
print(region.get('1'))