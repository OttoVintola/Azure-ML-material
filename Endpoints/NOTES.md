In AML online endpoints permit the deployment of ML models. 

## Managed online endpoint

Sending data to an ```HTTPS``` endpoint activates the scoring script and returns the **inference**. 

In AML there are two kinds of online endpoints
1. **Managed online endpoints** (AML managed infrastructure)
2. **Kubernetes online endpoints** (Kubernetes cluster)

For number (1) the VM type and scaling settings need to be defined!

## Requirements for deployment

1. **Model assets** (e.g. pickle file or registered model)
2. **Scoring script** (loads the model)
3. **Environment** (necessary packages)
4. **Compute config** (compute size, type and scaling settings)

From the preceding, deployments are a set of resources to host a model and inference on incoming data.

## MLflow and endpoints

AML *automatically* creates the scoring script and environment when deploying an MLflow model to a *managed online endpoint*. 

**Requirements**
1. ```MLmodel``` file which describes the usage and loading of the model
2. Compute config (```instance_type``` and ```instance_count```)


## Custom models

This requires
- **Model files** or **registered model**
- **Scoring script**
- Execution **environment**

Furthermore, the scoring script has to have ```init()``` and ```run()``` functions. The initialization is executed everytime the endpoint is invoked and running generates inference data.

To create an environment a ```conda.yml``` or ```Dockerfile``` is required.

Example of a conda.yml file 

```YML
name: basic-env-cpu
channels: 
    - conda-forge
dependencies:
    - python==3.7
    - scikit-learn
    - torch==2.1.1
    - pandas
    ...
```




