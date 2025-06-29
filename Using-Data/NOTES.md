## URIs

Azure Machine Learning accesses data through **uniform resource identifiers** (URIs). 

They can be 
- **Datastores**
- **Data assets**
within the workspace. 

Datastores are references to existing storage accounts, e.g., Azure Blob Storage or Azure Data Lake Storage. They are essentially abstractions of cloud data stores that encapsulate the information needed for connection.

## Access

URIs require a specific protocol to connect to the source. There are **three** of them supported in AML.
1. ```http(s)``` — for storage account or public location
2. ```abfs(s)``` — Azure data lake gen 2
3. ```azureml``` — Azure ML datastore


## Datastores 
### Authentication

During creation there are **two** methods
1. credential-based (account key, service principal etc.) or
2. identity-based (Microsoft EntraID, managed identity)

for authentication. 

### Types

AML provides support for many different datastores such as Azure Blob Storage, Azure File Share, Azure Data Lake (Gen 2).  

## Data assets

Data assets are references to already existing sources of data and their authentication methods as well as the metadata. Data assets can be 
- Public URLs
- Azure storage services
- local data.
Data assets can be shared, accessed and versioned easily. 

### Types

There are **three** basic types 
1. **URI file**
2. **URI folder**
3. **MLTable** (file, folder or structured data with reading instructions)

### Creation

In AML data assets are only stored as connection strings that specify the location of the data. Consequently, there are **four** connection methods
1. Local ```./<path>```
2. Azure Blob Storage ```wasbs://account_name.blob.core.windows.net/<container_name>/<folder>/<file>```
3. Azure Data Lake (Gen 2) storage ```abfss://<file-system>@<account-name>.dfs.core.windows.net/<folder>/<file>```
4. Datastore ```azureml://datastores/<datastore-name>/paths/<folder>/<file>```

