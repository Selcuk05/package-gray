
from sdks.novavision.src.helper.package import PackageHelper
from components.PackageGray.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, PackageGrayExecutorOutputs, PackageGrayExecutorResponse, PackageGrayExecutor, OutputImage, OutputImage2, PackageGrayExecutorTwoOutputs, PackageGrayExecutorTwoResponse, PackageGrayExecutorTwo

# context = executors/PackageGrayExecutor.py => PackageGray
def build_response(context):
    outputImage = OutputImage(value=context.image)
    packageGrayExecutorOutputs = PackageGrayExecutorOutputs(outputImage=outputImage)
    packageGrayExecutorResponse = PackageGrayExecutorResponse(outputs=packageGrayExecutorOutputs)
    packageGrayExecutor = PackageGrayExecutor(value=packageGrayExecutorResponse)


    """    Outputs = PackageOutputs(outputImage=outputImage)
        packageResponse = PackageResponse(outputs=Outputs)
        packageExecutor = PackageExecutor(value=packageResponse)"""

    executor = ConfigExecutor(value=packageGrayExecutor)

    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)

    return packageModel

def build_response_two(context):
    outputImage = OutputImage(value=context.image1)
    outputImage2 = OutputImage2(value=context.image2)
    packageGrayExecutorTwoOutputs = PackageGrayExecutorTwoOutputs(outputImage=outputImage, outputImage2=outputImage2)
    packageGrayExecutorTwoResponse = PackageGrayExecutorTwoResponse(outputs=packageGrayExecutorTwoOutputs)
    packageGrayExecutorTwo = PackageGrayExecutorTwo(value=packageGrayExecutorTwoResponse)

    executor = ConfigExecutor(value=packageGrayExecutorTwo)

    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)

    return packageModel