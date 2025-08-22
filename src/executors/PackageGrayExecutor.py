"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.PackageGray.src.utils.response import build_response
from components.PackageGray.src.models.PackageModel import PackageModel

CV2_COLOR_MAP = {
    "COLOR_BGR2GRAY": cv2.COLOR_BGR2GRAY,
    "COLOR_GRAY2BGR": cv2.COLOR_GRAY2BGR,
}

# executor class and file name change
class PackageGray(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.rotation_degree = self.request.get_param("Degree")
        self.keep_side = self.request.get_param("KeepSide")
        self.color_conversion = self.request.get_param("ColorConversion")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def grayscale(self, img):
        conversion = CV2_COLOR_MAP[self.color_conversion]
        return cv2.cvtColor(img, conversion)

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)

        img.value = self.grayscale(img)

        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()