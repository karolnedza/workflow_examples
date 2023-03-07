module "use1-10-12-0-0-16" {
  source  = "../modules/mc-spoke"
  name = "use1-10-12-0-0-16"
  cloud = "aws"
  region = "us-east-1"
  account = "nsm"
  cidr = "10.12.0.0/16"
  transit_gw = "aws-use1-transit-gw"
  network_domain = "green"
  ha_gw = false
}

output "use1-10-12-0-0-16" {
  value = module.use1-10-12-0-0-16.vpc
}
