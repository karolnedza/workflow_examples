module "mc-spoke" {
  source  = "../modules/mc-spoke/aviatrix"
  name = var.vpc_name
  cloud = var.cloud[var.region]
  region = var.region
  account = var.account_name[var.region]
  cidr = var.vpc_cidr
  transit_gw = var.transit_gw[var.region]
  network_domain = var.network_domain
  ha_gw = false
}
