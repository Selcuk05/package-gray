"""
It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), "../../../../"))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.PackageGray.src.utils.response import build_response_two
from components.PackageGray.src.models.PackageModel import PackageModel


# executor class and file name change
class PackageGrayExecutorTwo(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.font_size = self.request.get_param("FontSize")
        self.thickness = self.request.get_param("Thickness")

        self.image1 = self.request.get_param("inputImage1")
        self.image2 = self.request.get_param("inputImage2")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def normalize_images(self, img1, img2):
        if img1.dtype != img2.dtype:
            img1 = img1.astype(np.uint8)
            img2 = img2.astype(np.uint8)

        h1, w1 = img1.shape[:2]
        h2, w2 = img2.shape[:2]

        if len(img1.shape) != len(img2.shape):
            if len(img1.shape) == 2 and len(img2.shape) == 3:
                img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
            elif len(img1.shape) == 3 and len(img2.shape) == 2:
                img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

        if h1 != h2:
            target_height = min(h1, h2)
            if h1 > target_height:
                new_w1 = int(w1 * (target_height / h1))
                img1 = cv2.resize(img1, (new_w1, target_height))
            if h2 > target_height:
                new_w2 = int(w2 * (target_height / h2))
                img2 = cv2.resize(img2, (new_w2, target_height))

        return img1, img2

    def merge_imgs(self, img1, img2):
        try:
            img1_norm, img2_norm = self.normalize_images(img1, img2)

            if img1_norm.shape[0] != img2_norm.shape[0]:
                raise ValueError(
                    f"Image heights don't match: {img1_norm.shape[0]} vs {img2_norm.shape[0]}"
                )

            if img1_norm.dtype != img2_norm.dtype:
                raise ValueError(
                    f"Image dtypes don't match: {img1_norm.dtype} vs {img2_norm.dtype}"
                )

            if len(img1_norm.shape) != len(img2_norm.shape):
                raise ValueError(
                    f"Image dimensions don't match: {len(img1_norm.shape)} vs {len(img2_norm.shape)}"
                )

            return cv2.hconcat([img1_norm, img2_norm])

        except Exception as e:
            print(f"Error in merge_imgs: {str(e)}")
            print(f"img1 shape: {img1.shape}, dtype: {img1.dtype}")
            print(f"img2 shape: {img2.shape}, dtype: {img2.dtype}")
            raise

    def apply_text(self, img):
        try:
            font_size = self.font_size
            thickness = int(self.thickness[-1])  # NOTE: cant find another way :D
            text = "MERGED"
            font = cv2.FONT_HERSHEY_SIMPLEX

            height, width = img.shape[:2]
            (text_width, text_height), baseline = cv2.getTextSize(
                text, font, font_size, thickness
            )

            x = (width - text_width) // 2
            y = (height + text_height) // 2

            cv2.putText(
                img,
                text,
                (x, y),
                font,
                font_size,
                (255, 255, 255),
                thickness,
                cv2.LINE_AA,
            )
            return img
        except Exception as e:
            print(f"Error in apply_text: {str(e)}")
            return img

    def run(self):
        try:
            img1 = Image.get_frame(img=self.image1, redis_db=self.redis_db)
            img2 = Image.get_frame(img=self.image2, redis_db=self.redis_db)

            if img1 is None or img1.value is None:
                raise ValueError("Failed to retrieve image1 from Redis")
            if img2 is None or img2.value is None:
                raise ValueError("Failed to retrieve image2 from Redis")

            print(f"Image1 shape: {img1.value.shape}, dtype: {img1.value.dtype}")
            print(f"Image2 shape: {img2.value.shape}, dtype: {img2.value.dtype}")

            merged_img = self.merge_imgs(img1.value, img2.value)

            merged_img = self.apply_text(merged_img)

            img1.value = merged_img

            self.image1 = Image.set_frame(
                img=img1, package_uID=self.uID, redis_db=self.redis_db
            )  # for video view
            self.image2 = Image.set_frame(
                img=img1, package_uID=self.uID, redis_db=self.redis_db
            )  # for file save

            packageModel = build_response_two(context=self)
            return packageModel

        except Exception as e:
            print(f"Error in PackageGrayExecutorTwo.run(): {str(e)}")
            raise


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
