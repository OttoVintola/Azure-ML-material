
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()


"""
To create a ManagedOnlineEndpoint the following must be defined
    - name: (unique to Azure region)
    - auth_mode: "key" for key-based and "aml_token" 
                for AML token-based authentication
"""

from azure.ai.ml.entities import ManagedOnlineEndpoint

endpoint = ManagedOnlineEndpoint(
            name="YOUR_ENDPOINT_NAME",
            auth_mode="key",
            description="Online endpoint"
            )



"""
To create a blue (referring to blue/green MLOps practice) 
deployment 
    - Register model
    - Deploy to MOE
"""

from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# Registering 
model = Model(
        path="./model",
        type=AssetTypes.MLFLOW_MODEL,
        description="YOUR_DESCRIPTION"
        )

# Deployment
blue_deployment = ManagedOnlineEndpoint(
                    name="YOUR_DEPLOYMENT_NAME",
                    auth_mode="key",
                    endpoint_name="YOUR_ENDPOINT_NAME",
                    model=model,
                    instance_type="STANDARD_F4s_v2",
                    instance_count=1
                )

ml_client.online_endpoints.begin_create_or_update(blue_deployment).result()



"""
Custom models require an execution environment which is created
with the Environment class
"""

from azure.ai.ml.entities import Environment

env = Environment(
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04",
        conda_file="./src/conda.yml",
        name="ENV_NAME",
        description="Environment from Docker image and Conda env"
        )

# To deploy

blue_deployment = ManagedOnlineEndpoint(
                    name="YOUR_NAME",
                    endpoint_name="YOUR_ENDPOINT_NAME",
                    model=model,
                    environment="ENV_NAME",
                    code_configuration=CodeConfiguration(
                        code="./src", scoring_script="score.py"
                    ),
                    instance_type="Standard_DS2_v2",
                    instance_count=1
                )

ml_client.online_deployments.begin_create_or_update(blue_deployment).result()

