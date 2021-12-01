
from yunionclient.common import base

class Topic(base.ResourceBase):
    pass


class TopicManager(base.StandaloneManager):
    resource_class = Topic
    keyword = 'topic'
    keyword_plural = 'topics'
    _columns = []
    _admin_columns = []

