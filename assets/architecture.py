from diagrams import Diagram, Cluster
from diagrams.programming.framework import Flask, GraphQL

from diagrams.onprem.container import Docker
from diagrams.onprem.database import Postgresql
from diagrams.onprem.analytics import Metabase, Dbt
from diagrams.custom import Custom

with Diagram("Puptool Overview", show=True, direction="LR"):

    airbyte = Custom("Airbyte", "airbyte.png")

    with Cluster("TryFi-Flask-Microservice"):
        docker = Docker("NAS")
        with Cluster(""):
            app = Flask("API")

    app << GraphQL("TryFi") 
    docker - app >>  airbyte >> Dbt("transformation") >> Postgresql("Data Mart") >> Metabase("Metabase Dashboard")

# Instructions to generate: 
#
# source env/bin/activate
# pip install diagrams 
# python architecture.py