# TODO: ADD IMPORTS
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

try:
    credential = DefaultAzureCredential()
    # Check if given credential can get token successfully.
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:
    # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
    credential = InteractiveBrowserCredential()

from azure.ai.ml import MLClient
ml_client = MLClient.from_config(credential=credentials)

credentials = AccountKeyConfiguration(account_key="YOU_ACCOUNT_KEY")


# Creating a AzureBlobDatastore with credential-based authentication
blob_datastore = AzureBlobDatastore(
                    name="YOUR_NAME",
                    description="YOUR_DESCRIPTION",
                    account_name="MYTESTBLOBSTORE", # Must be together without spaces or hyphens
                    container_name="MY_CONTAINER_NAME",
                    credentials=creds
                )

ml_client.create_or_update(blob_datastore)



# Creating a URI folder asset
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

YOUR_PATH = '<path>'

URI_file = Data(
                path=YOUR_PATH,
                type=AssetTypes.URI_FOLDER,
                description="YOUR_DESCRIPTION"
                name="YOUR_NAME",
                version="VERSION-NUMBER" # Number stored as string
            )

ml_client.data.create_or_update(URI_file)


# Creating an MLTable data asset. 
# MLTable is nice since the schema for reading the data is included in a separate file.
# Thus, only the reading schema has to be modified—instead of all the scripts using it—if there are changes to the data.
# Automated ML only accepts MLTable
# The creation code is the same as above, except the type is changed to AssetTypes.MLTABLE

MLTABLE = Data(
            path=YOUR_PATH,
            type=AssetTypes.MLTABLE,
            description="YOUR_DESCRIPTION",
            name="YOUR_NAME",
            version="VERSION-NUMBER"
)

ml_client.data.create_or_update(MLTABLE)








