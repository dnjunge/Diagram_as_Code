from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3

# graph_attr={
#     "fontsize": "45",
#     "bgcolor": "transparent"
# }

with Diagram("Simple Diagram", filename="my_diagram_learn2", outformat="jpg" ):#, graph_attr=graph_attr):
    ELB("load_balancer") >> EC2("web") >> RDS("userdb") >> S3("store")
    ELB("load_balancer") >> EC2("web") >> RDS("userdb") << EC2("stat")
    (ELB("load_balancer") >> EC2("web")) - EC2("web") >> RDS("userdb")