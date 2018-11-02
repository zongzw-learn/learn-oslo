# -*- coding: utf-8

from oslo_cache import core as cache
from oslo_config import cfg

CONF = cfg.CONF

caching = cfg.BoolOpt('caching', default=True)
cache_time = cfg.IntOpt('cache_time', default=3600)
CONF.register_opts([caching, cache_time], "feature-name")

cache.configure(CONF)
example_cache_region = cache.create_region()
MEMOIZE = cache.get_memoization_decorator(
    CONF, example_cache_region, "feature-name")

# Load config file here
CONF(default_config_files=['sample.ini'])

cache.configure_cache_region(CONF, example_cache_region)


@MEMOIZE
def f(x):
    print x
    return x

'''
https://docs.openstack.org/oslo.cache/latest/user/usage.html
作为一个基本的cache模块，提供的缓存的CURD功能的展示在哪里？

好比告诉人说我做了一个无比强大的工具足以可以改变世界。
但是没告诉人说这个工具怎么用。。
想用这个伟大的工具改变世界，请去读懂这个工具的设计细节？？

'''

example_cache_region.set("name", 23)
print(example_cache_region.get("name"))
