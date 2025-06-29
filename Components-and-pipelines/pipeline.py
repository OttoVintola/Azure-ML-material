# import required libraries
from azure.identity import DefaultAzureCredential

from azure.ai.ml import MLClient
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import load_component

@pipeline()
def my_pipeline():
    # Load components
    component1 = load_component(source="path/to/component1.yml")
    component2 = load_component(source="path/to/component2.yml")

    # Use components in the pipeline
    step1 = component1(param1="value1", param2="value2")
    step2 = component2(input_data=step1.outputs.output_data)

    return {
        "output_data": step2.outputs.output_data,
        "output_metric": step2.outputs.output_metric
    }