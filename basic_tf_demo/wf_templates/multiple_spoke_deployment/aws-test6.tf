module "test6" {
  source  = "../modules/mc-spoke"
  name = "test6"
  cloud = "aws"
  region = "us-east-1"
  account = "aws-account"
  cidr = "10.0.1.0/24"
  transit_gw = "aws-use1-transit-gw"
  network_domain = "red"
  ha_gw = false
}

output "test6" {
  value = module.test6.vpc
}
