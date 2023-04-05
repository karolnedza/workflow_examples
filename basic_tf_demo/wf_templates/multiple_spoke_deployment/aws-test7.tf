module "test7" {
  source  = "../modules/mc-spoke"
  name = "test7"
  cloud = "aws"
  region = "us-east-1"
  account = "aws-account"
  cidr = "10.1.0.0/16"
  transit_gw = "aws-use1-transit-gw"
  network_domain = "red"
  ha_gw = false
}

output "test7" {
  value = module.test7.vpc
}
