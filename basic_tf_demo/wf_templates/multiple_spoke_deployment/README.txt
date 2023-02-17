Description:

This example supports day 1 and day 2 deployment of spoke VPC 
in the same account folder.

Prerequisite:

- pip install jinja-cli

Sample VPC config.json inputs:

cat config.json 
{
    "cloud": "aws",
    "account_name": "aws-account",
    "transit_gw_name": "aws-use1-transit-gw",
    "vpc_id": "use1-10-10-0-0-16",
    "vpc_name": "use1-10-10-0-0-16",
    "cidr": "10.10.0.0/16",
    "region": "us-east-1",
    "network_domain": "red",
    "ctrl_ip": "52.3.72.231"
}

Generate the following tf files using config.json:

- jinja -d config.json main.tf.tmpl > aws-use1-10-10-0-0-16.tf
- jinja -d config.json providers.tf.tmpl > providers.tf

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

S3:

terraform init \
    -backend-config="key=deploy_avx_spoke_gw_12345668999.tfstate" \
    -backend-config="region=us-east-1" \
    -backend-config="bucket=solution-terraform-state-205987878622"