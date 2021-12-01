
from yunionclient.common import base

class K8sService(base.ResourceBase):
    pass


class K8sServiceManager(base.StandaloneManager):
    resource_class = K8sService
    keyword = 'k8s_service'
    keyword_plural = 'k8s_services'
    _columns = []
    _admin_columns = []

