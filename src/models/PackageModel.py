
from pydantic import Field, model_validator, validator
from typing import Any, List, Optional, Union, Literal, Dict
from sdks.novavision.src.base.model import Detection, Detections, File, Images, Package, Image, Inputs, Configs, Outputs, Param, Response, Request, Output, Input, Config

# region Input Output Types
AnyInput = Union[
    Image,
    File,
    Images,
    Detections,
    Detection,
    Input,
    Param
]

AnyOutput = Union[
    Image,
    File,
    Images,
    Detections,
    Detection,
    Output,
    Param
]


class InputData(Input):
    name: Literal["inputData"] = "inputData"
    value: Union[List[AnyInput], AnyInput]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, list):
            return "list"
        elif isinstance(value, dict):
            return "dict"
        return "object"

    class Config:
        title = "Data"


class OutputData(Output):
    name: Literal["outputData"] = "outputData"
    value: Union[List[AnyOutput], AnyOutput]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, list):
            return "list"
        elif isinstance(value, dict):
            return "dict"
        return "object"

    class Config:
        title = "Data"
# endregion


# region Inputs
class PresetInputs(Inputs):
    inputData: InputData


class CustomInputs(Inputs):
    inputData: InputData
# endregion

# region Outputs


class PresetOutputs(Inputs):
    outputData: OutputData


class CustomOutputs(Outputs):
    outputData: OutputData
# endregion

# region Request Configs
# region Preset Configs Fields


class ImageType(Config):
    name: Literal["ImageType"] = "ImageType"
    value: Literal["Image"] = "Image"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Image"


class DetectionType(Config):
    name: Literal["DetectionType"] = "DetectionType"
    value: Literal["Detection"] = "Detection"
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Detection"


class ExtractType(Config):
    name: Literal["ExtractType"] = "ExtractType"
    value: Union[ImageType, DetectionType]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Extract Type"
# endregion


class PresetConfigs(Configs):
    ExtractType: ExtractType

# region Custom Configs Fields


class ExtractFields(Config):
    name: Literal["ExtractFields"] = "ExtractFields"
    value: str = ""
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Extract Fields"
# endregion


class CustomConfigs(Configs):
    ExtractFields: ExtractFields
# endregion

# region Request


class PresetRequest(Request):
    inputs: Optional[PresetInputs]
    configs: PresetConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class CustomRequest(Request):
    inputs: Optional[CustomInputs]
    configs: CustomConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }
# endregion

# region Response


class PresetResponse(Response):
    outputs: PresetOutputs


class CustomResponse(Response):
    outputs: CustomOutputs
# endregion

# region Executor Conifgs


class PresetExecutor(Config):
    name: Literal["Preset"] = "Preset"
    value: Union[PresetRequest, PresetResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Preset"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class CustomExecutor(Config):
    name: Literal["Custom"] = "Custom"
    value: Union[CustomRequest, CustomResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Custom"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }
# endregion

# region Root Config


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[PresetExecutor, CustomExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["PropertyDefinition"] = "PropertyDefinition"
# endregion
