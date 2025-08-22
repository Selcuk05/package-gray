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
from components.PackageGray.src.utils.response import build_response_two
from components.PackageGray.src.models.PackageModel import PackageModel

# executor class and file name change
class PackageGrayTwo(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.font_size = self.request.get_param('FontSize')

        self.image1 = self.request.get_param("inputImage1")
        self.image2 = self.request.get_param("inputImage2")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def merge_imgs(self, img1, img2):
        return cv2.hconcat([img1, img2])

    def apply_text(self, img):
        cv2.putText(
            img,
            "MERGED",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            self.font_size,
            (255, 255, 255),
            2,
            cv2.LINE_AA
        )
        return img

    def run(self):
        img1 = Image.get_frame(img=self.image1, redis_db=self.redis_db)
        img2 = Image.get_frame(img=self.image2, redis_db=self.redis_db)

        img1.value = self.merge_imgs(img1.value, img2.value)
        img1.value = self.apply_text(img1.value)

        self.image1 = Image.set_frame(img=img1, package_uID=self.uID, redis_db=self.redis_db) # for video view
        self.image2 = Image.set_frame(img=img1, package_uID=self.uID, redis_db=self.redis_db) # for file save
        packageModel = build_response_two(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()