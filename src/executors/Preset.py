"""
    It is one of the preprocessing components in which the image is rotated.
"""

from components.PropertyDefinition.src.models.PackageModel import PackageModel
from components.PropertyDefinition.src.utils.response import build_response_custom
from sdks.novavision.src.helper.executor import Executor
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.media.image import Image
import os
import cv2
import sys
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))


class Custom(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.inputData = self.request.get_param("inputData")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        value = self.inputData
        print(type(value))
        if isinstance(value, (list, dict)):
            print(json.dumps(value, indent=2, default=str))
        else:
            print(value)
        packageModel = build_response_custom(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
