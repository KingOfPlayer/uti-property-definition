
from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config

class DataInput(Input):
    name: Literal["dataInput"] = "dataInput"
    value: Union[List[Input],Input]
    type: str = "object"

    class Config:
        title = "Data"

class DataOutput(Output):
    name: Literal["dataOutput"] = "dataOutput"
    value: Union[List[Output],Output]
    type: str = "object"

    class Config:
        title = "Data"

# region Inputs
class PresetInputs(Inputs):
    dataInput: DataInput

class CustomInputs(Inputs):
    dataOutput: DataOutput
# endregion

# region Outputs
class PresetOutputs(Inputs):
    dataInput: DataInput

class CustomOutputs(Outputs):
    dataOutput: DataOutput
# endregion

# region Request Configs
# region Request Configs Fields

# endregion
class PresetConfigs(Configs):
    pass

class CustomConfigs(Configs):
    pass
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
# endregion

class CustomExecutor(Config):
    name: Literal["Custom"] = "Custom"
    value: Union[CustomRequest, CustomResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Custom"
        json_schema_extra = {
            "target": {
                "value": 1
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
        json_schema_extra = {
            "target": "value"
        }

class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["PropertyDefinition"] = "PropertyDefinition"
# endregion
