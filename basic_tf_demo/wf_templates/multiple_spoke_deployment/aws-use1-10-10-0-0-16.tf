module "use1-10-10-0-0-16" {
  source  = "../modules/mc-spoke"
  name = "use1-10-10-0-0-16"
  cloud = "aws"
  region = "us-east-1"
  account = "aws-account"
  cidr = "10.10.0.0/16"
  transit_gw = "aws-use1-transit-gw"
  network_domain = "red"
  ha_gw = false
}

output "use1-10-10-0-0-16" {
  value = module.use1-10-10-0-0-16.vpc
}
