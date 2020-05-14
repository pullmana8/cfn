from troposphere import Template
from troposphere.ec2 import VPC

def vpc(sceptre_user_data):
    """AWS VPC CloudFormation Template"""
    t = Template()
    t.add_resource(VPC(
        "VirtualPrivateCloud",
        CidrBlock=sceptre_user_data["cidr_block"]
    ))
    return t.to_yaml()

def sceptre_handler(sceptre_user_date):
    return vpc(sceptre_user_date)
