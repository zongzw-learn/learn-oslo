# -*- coding: utf-8
import oslo_i18n

DOMAIN = "oslo_i18n"
_translators = oslo_i18n.TranslatorFactory(domain=DOMAIN)

_ = _translators.primary
_C = _translators.contextual_form
_P = _translators.plural_form

_LI = _translators.log_info
_LW = _translators.log_warning
_LE = _translators.log_error
_LC = _translators.log_critical

def get_available_languages():
    return oslo_i18n.get_available_languages(DOMAIN)

print(get_available_languages())

import oslo_i18n

msg = "Message objects do not support addition."
trans_msg = oslo_i18n.translate(msg, 'zh_CN')

# *** no trying on i18n yet. 

'''
Locale directory

    Python gettext looks for binary mo files for the given domain using the path 
    <localedir>/<language>/LC_MESSAGES/<domain>.mo. The default locale directory varies on distributions, 
    and it is /usr/share/locale in most cases.

    If you store message catalogs in a different location, you need to specify the location via an environment 
    variable named <DOMAIN>_LOCALEDIR where <DOMAIN> is an upper-case domain name with replacing _ and . with -. 
    For example, NEUTRON_LOCALEDIR for a domain neutron and OSLO_I18N_LOCALEDIR for a domain oslo_i18n.

'''

'''
To generate .mo file from .po file:

msgfmt <.po file>

msgfmt can be installed by brew on macosx. however, it's easy to use linux to do it.

locale的命名规则为: 如zh_CN.GBK，zh代表中文， CN代表大陆地区，GBK表示字符集。
'''
