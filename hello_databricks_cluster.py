from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi
import os

# Tạo đối tượng ApiClient
api_client = ApiClient(
    host=os.getenv("DATABRICKS_HOST"), token=os.getenv("DATABRICKS_TOKEN")
)

# Tạo đối tượng ClusterApi
clusters_api = ClusterApi(api_client)

# Lấy danh sách các clusters
clusters_list = clusters_api.list_clusters()

# In tên và ID của từng cluster
print("Cluster name, Cluster ID")
for cluster in clusters_list["clusters"]:
    print(cluster["cluster_name"], cluster["cluster_id"])
