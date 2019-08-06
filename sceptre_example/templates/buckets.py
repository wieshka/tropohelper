from troposphere.s3 import Bucket
from troposphere import StackId, Sub, Export

from tropohelper import TemplateBuilder

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class S3TemplateBuilder(TemplateBuilder):
    def entry(self):
        for bucket in self.user_data["buckets"]:
            self.current_item = bucket
            self.add_bucket()
            self.consider_output()

    def add_bucket(self):
        self.template.add_resource(Bucket(self.get_resource_name()))


def sceptre_handler(sceptre_user_data):
    resources = S3TemplateBuilder(sceptre_user_data)

    return resources.template.to_json()

