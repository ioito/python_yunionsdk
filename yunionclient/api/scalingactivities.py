
from yunionclient.common import base

class Scalingactivity(base.ResourceBase):
    pass


class ScalingactivityManager(base.StandaloneManager):
    resource_class = Scalingactivity
    keyword = 'scalingactivity'
    keyword_plural = 'scalingactivities'
    _columns = []
    _admin_columns = []

