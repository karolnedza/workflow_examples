Sample .tfvars inputs:

name           = "use1-10-10-0-0-16"
cidr           = "10.10.0.0/16"
region         = "us-east-1"
network_domain = "red"
ctrl_ip        = "52.3.72.231"

Required environment variable inputs:

AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AVIATRIX_PASSWORD
AVIATRIX_USERNAME

Testing for AWS us-east-1:

- Create an account with the name "aws-account" in the controller.
- Create an Aviatrix transit gw in us-east-1 with the name "aws-use1-transit-gw".
- Enable segmentation at MULTI-CLOUD TRANSIT > Segmentation > 1
- Create a domain name "red" at MULTI-CLOUD Transit > Segmentation > 2