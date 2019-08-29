# python-findall-instances
Python script to find all(All region) Running/Stopped ec2-instances using boto3

---
### Prerequisite:
1. Install python, boto3 library
2. Create a programamtic user with neccessary policies.
3. Configure aws-cli
---
boto3 Documentation [link](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
---
---
```sh
listallec2.py
```
####  Script
```sh
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
```
---
#### Output
---
```sh
$ python3 listallec2.py
List of EC2 Instances
Region      Instance ID          State
us-east-1   i-07c8225c9af5549b7  stopped
us-east-1   i-05ad5b9535727a124  running
us-east-1   i-04182256e1705b901  stopped
```
 
