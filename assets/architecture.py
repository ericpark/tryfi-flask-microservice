from diagrams import Diagram, Cluster
from diagrams.programming.framework import Flask, GraphQL

from diagrams.onprem.container import Docker
from diagrams.onprem.database import Postgresql
from diagrams.onprem.analytics import Metabase, Dbt
from diagrams.custom import Custom

with Diagram("Puptool Overview", show=True, direction="LR"):

    airbyte = Custom("Airbyte", "airbyte.png")

    with Cluster("Docker"):
        docker = Docker("Synology")
        with Cluster("App"):
            app = Flask("App")

    app << GraphQL("TryFi") 
    airbyte >> docker >> app >> Dbt("dbt") >> Postgresql("db") >> Metabase("Metabase Dashboard")
