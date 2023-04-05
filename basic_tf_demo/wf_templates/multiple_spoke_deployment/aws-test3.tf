module "test3" {
  source  = "../modules/mc-spoke"
  name = "test3"
  cloud = "aws"
  region = "us-east-1"
  account = "aws-account"
  cidr = "10.0.0.0/24"
  transit_gw = "aws-use1-transit-gw"
  network_domain = "red"
  ha_gw = false
}

output "test3" {
  value = module.test3.vpc
}
