import boto3

ec2=boto3.client("ec2",region_name="us-east-1")

all_regions=ec2.describe_regions()

list_of_regions=[]

for each_reg in all_regions["Regions"]:

    list_of_regions.append(each_reg["RegionName"])

print("List of EC2 Instances")

print("{:11} {:20} {:8}".format("Region","Instance ID","State"))

for each_reg in list_of_regions:
    ec2_ob=boto3.resource("ec2",region_name=each_reg)

    for each_in in ec2_ob.instances.all():

        print("{:11} {:20} {:8}".format(each_reg,each_in.id,each_in.state["Name"]))
