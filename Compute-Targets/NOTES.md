## Types of compute

Data science often requires access to compute resources beyond local development environments. Thus, AML provides
- Compute instances (lightweight, for *experimentation*)
- Compute clusters (multi-node clusters with autoscaling, parallel distribution of workloads)
- Kubernetes clusters: (more control, self-managed AKS)
- Attached compute: attach Azure VMs or Azure Databricks clusters
- Serverless compute: on-demand compute

**Clusters** are mainly used for pipeline jobs from Designer, Automated ML or running a script as a job, whereas compute instances are for notebooks or other VM experimentation.


