from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import (
    Package,
    Image,
    Inputs,
    Configs,
    Outputs,
    Response,
    Request,
    Output,
    Input,
    Config,
)


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class ColorBGR2GRAY(Config):
    name: Literal["ColorBGR2GRAY"] = "ColorBGR2GRAY"
    value: Literal["COLOR_BGR2GRAY"] = "COLOR_BGR2GRAY"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "BGR => GRAY"


class ColorGRAY2BGR(Config):
    name: Literal["ColorGRAY2BGR"] = "ColorGRAY2BGR"
    value: Literal["COLOR_GRAY2BGR"] = "COLOR_GRAY2BGR"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "GRAY => BGR"


class ColorConversion(Config):
    name: Literal["ColorConversion"] = "ColorConversion"
    value: Union[ColorBGR2GRAY, ColorGRAY2BGR]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    restart: Literal[True] = True

    class Config:
        title = "Color Conversion"


class KeepSideFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class KeepSideTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class KeepSideBBox(Config):
    """
    Rotate image without catting off sides.
    """

    name: Literal["KeepSide"] = "KeepSide"
    value: Union[KeepSideTrue, KeepSideFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Keep Sides"


class Degree(Config):
    """
    Positive angles specify counterclockwise rotation while negative angles indicate clockwise rotation.
    """

    name: Literal["Degree"] = "Degree"
    value: int = Field(ge=-359.0, le=359.0, default=0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[-359, 359]"] = "[-359, 359]"

    class Config:
        title = "Angle"


class PackageGrayExecutorInputs(Inputs):
    inputImage: InputImage


class PackageGrayExecutorConfigs(Configs):
    degree: Degree
    drawBBox: KeepSideBBox
    colorConversion: ColorConversion


class PackageGrayExecutorOutputs(Outputs):
    outputImage: OutputImage


class PackageGrayExecutorRequest(Request):
    inputs: Optional[PackageGrayExecutorInputs]
    configs: PackageGrayExecutorConfigs

    class Config:
        json_schema_extra = {"target": "configs"}


class PackageGrayExecutorResponse(Response):
    outputs: PackageGrayExecutorOutputs


### PACKAGE GRAY EXECUTOR 1
class PackageGrayExecutor(Config):
    name: Literal["PackageGrayExecutor"] = "PackageGrayExecutor"
    value: Union[PackageGrayExecutorRequest, PackageGrayExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "PackageGray"
        json_schema_extra = {"target": {"value": 0}}


#############################################3


class InputImage1(Input):
    name: Literal["inputImage1"] = "inputImage1"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image 1"


class InputImage2(Input):
    name: Literal["inputImage2"] = "inputImage2"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image 2"


class OutputImage2(Output):
    name: Literal["outputImage2"] = "outputImage2"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image 2"


class FontSize(Config):
    name: Literal["FontSize"] = "FontSize"
    value: int = Field(ge=0, le=40, default=15)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[0, 40]"] = "[0, 40]"

    class Config:
        title = "Font Size"


### dependent dropdown thickness
class Thickness1(Config):
    name: Literal["Thickness1"] = "Thickness1"
    value: Literal[1] = 1
    type: Literal["int"] = "int"
    field: Literal["option"] = "option"

    class Config:
        title = "1"


class Thickness2(Config):
    name: Literal["Thickness2"] = "Thickness2"
    value: Literal[2] = 2
    type: Literal["int"] = "int"
    field: Literal["option"] = "option"

    class Config:
        title = "2"


class Thickness3(Config):
    name: Literal["Thickness3"] = "Thickness3"
    value: Literal[3] = 3
    type: Literal["int"] = "int"
    field: Literal["option"] = "option"

    class Config:
        title = "3"


class Thickness(Config):
    name: Literal["Thickness"] = "Thickness"
    value: Union[Thickness1, Thickness2, Thickness3]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    restart: Literal[True] = True

    class Config:
        title = "Thickness"


class PackageGrayExecutorTwoInputs(Inputs):
    inputImage1: InputImage1
    inputImage2: InputImage2


class PackageGrayExecutorTwoConfigs(Configs):
    fontSize: FontSize
    thickness: Thickness


class PackageGrayExecutorTwoOutputs(Outputs):
    outputImage: OutputImage
    outputImage2: OutputImage2


class PackageGrayExecutorTwoRequest(Request):
    inputs: Optional[PackageGrayExecutorTwoInputs]
    configs: PackageGrayExecutorTwoConfigs

    class Config:
        json_schema_extra = {"target": "configs"}


class PackageGrayExecutorTwoResponse(Response):
    outputs: PackageGrayExecutorTwoOutputs


### PACKAGE GRAY EXECUTOR 2
class PackageGrayExecutorTwo(Config):
    name: Literal["PackageGrayExecutorTwo"] = "PackageGrayExecutorTwo"
    value: Union[PackageGrayExecutorTwoRequest, PackageGrayExecutorTwoResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "PackageGray2"
        json_schema_extra = {"target": {"value": 0}}


###########################################


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[PackageGrayExecutor, PackageGrayExecutorTwo]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"
        """json_schema_extra = {
            "target": "value"
        }"""  # no json schema on multi executor


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["PackageGray"] = "PackageGray"
