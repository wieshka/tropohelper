from troposphere import Template, Output, Ref, Sub
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TemplateBuilder:
    """
    Simple Wrapper class which eases work with Troposphere templates.
    """
    def __init__(self, user_data):
        """
        This will create empty Template() as wrap a bit around it. Pass sceptre_user_data to init method. 
        """
        self.template = Template()
        self.user_data = user_data
        self.current_item = None
        self.params = {}
        self.entry()

    def entry(self):
        """
        One should always overwrite entry function to override it's behaviour.
        """
        raise ImportError("No entry method specified for TemplateBuilder")

    def consider_output(self):
        """
        Handles CF Output generation
        """
        if "output" in self.current_item.keys():
            if "description" in self.current_item.keys():
                description = self.current_item["description"]
            else:
                description = ""
            if self.current_item["output"]:
                self.template.add_output(
                    Output(
                        self.get_output_name(),
                        Value=Ref(self.get_resource_name()),
                        Description=description,
                    )
                )

    def get_resource_name(self):
        """
        Method to be used to generate Resource name in order to keep consistency across entire Sceptre controlled stack set.
        """
        return self.current_item["name"] + "Resource"

    def get_output_name(self):
        """
        Method to be used to generate Output name in order to keep consistency across entire Sceptre controlled stack set.
        """
        return self.current_item["name"] + "Output"

