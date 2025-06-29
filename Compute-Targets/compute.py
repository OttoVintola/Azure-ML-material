from azure.ai.ml.entities import ComputeInstance, AmlCompute

ci_basic_name = "basic-computeinst-0706"

ci_basic = ComputeInstance(
            name=ci_basic_name,     # Needs to be unique across region!
            size="STANDARD_DS3_v2"
            )

ml_client.begin_create_or_update(ci_basic).result()


cluster_basic = AmlCompute(
                    name = "cpu-cluster",
                    type="amlcluster",
                    size="STANDARD_DS3_v2",
                    location="YOUR_REGION",
                    min_instances=0,
                    max_instances=2,
                    idle_time_before_scale_down=120,
                    tier="low_priority" # or "Dedicated"
                )

ml_client.begin_create_or_update(cluster_basic).result()

# Compute instances can be used while running a script as a command job
from azure.ai.ml import command

job = command(
        code="./src",
        command="python training.py",
        environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest",
        compute="cpu-cluster",
        display_name="train-with-cluster",
        experiment_name="training"
    )

returned_job = ml_client.create_or_update(job)
aml_url = returned_job.studio_url



