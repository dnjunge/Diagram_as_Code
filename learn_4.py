from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


with Diagram("Grouped Workers", filename="my_diagram_learn4", outformat="jpg", direction="TB"):
    lb = ELB("load_balancer")
    db = RDS("events")
    lb >> [EC2("worker1"), 
           EC2("worker2"), 
           EC2("worker3"), 
           EC2("worker4"), 
           EC2("worker5")] >> db
