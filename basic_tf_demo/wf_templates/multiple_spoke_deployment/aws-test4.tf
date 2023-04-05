module "test4" {
  source  = "../modules/mc-spoke"
  name = "test4"
  cloud = "aws"
  region = "us-east-1"
  account = "aws-account"
  cidr = "10.0.1.0/24"
  transit_gw = "aws-use1-transit-gw"
  network_domain = "red"
  ha_gw = false
}

output "test4" {
  value = module.test4.vpc
}
