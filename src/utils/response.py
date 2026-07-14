
from sdks.novavision.src.helper.package import PackageHelper
from components.PropertyDefinition.src.models.PackageModel import ConfigExecutor, CustomExecutor, CustomOutputs, CustomResponse, OutputData, PackageConfigs, PackageModel, PresetExecutor, PresetOutputs, PresetResponse


def build_response_preset(context):
    outputData = OutputData(value=context.inputData)
    Outputs = PresetOutputs(outputData=outputData)
    packageResponse = PresetResponse(outputs=Outputs)
    packageExecutor = PresetExecutor(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel,
                            packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel


def build_response_custom(context):
    outputData = OutputData(value=context.inputData)
    Outputs = CustomOutputs(outputData=outputData)
    packageResponse = CustomResponse(outputs=Outputs)
    packageExecutor = CustomExecutor(value=packageResponse)
    executor = ConfigExecutor(value=packageExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel,
                            packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
