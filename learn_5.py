from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53


with Diagram("Simple Web Service with DB Cluster", filename="my_diagram_learn5", outformat="jpg"):
    dns = Route53("dns")
    web = ECS("service")

    with Cluster("DB Cluster"):
        db_primary = RDS("primary")
        db_primary - [RDS("replica1"), RDS("replica2")]

    dns >> web >> db_primary