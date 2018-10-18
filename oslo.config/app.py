from oslo_config import cfg
from oslo_config import generator

import sys

'''
https://docs.openstack.org/oslo.config/latest/

This program demonstrates:
    1. arguments from config files.
    2. arguments from command line.
    3. saving arguments into files.

'''

opt_group = cfg.OptGroup(name="simple", title="A simple example")
simple_opts = [
    cfg.BoolOpt("enable", default=False, help=('True enables, False disables'))
]

cli_opts = [
    cfg.StrOpt("file", default="gen.conf", help="the config file to save as.")
]

CONF = cfg.CONF

CONF.register_group(opt_group)
CONF.register_opts(simple_opts, opt_group)
CONF.register_cli_opts(cli_opts)

if __name__ == "__main__":

    '''
    run it: 
        python app.py --file gen.conf
    '''
    #CONF(default_config_files=['app.conf'])
    CONF(sys.argv[1:])

    print(CONF.simple.enable)
    print(CONF.file)

    # only registered namespaces can work..
    # oslo-config-generator --namespace oslo.messaging
    generator.main(args=['--namespace', 'oslo.messaging', '--output-file', CONF.file])
