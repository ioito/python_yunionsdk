
from yunionclient.common import base

class WafIpset(base.ResourceBase):
    pass


class WafIpsetManager(base.StandaloneManager):
    resource_class = WafIpset
    keyword = 'waf_ipset'
    keyword_plural = 'waf_ipsets'
    _columns = []
    _admin_columns = []

