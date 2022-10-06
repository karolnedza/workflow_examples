module "mc-spoke" {
  source  = "terraform-aviatrix-modules/mc-spoke/aviatrix"
  name = var.name
  version = "1.3.0"
  cloud = var.cloud[var.region]
  region = var.region
  account = var.account_name[var.region]
  cidr = var.cidr
  transit_gw = var.transit_gw[var.region]
  network_domain = var.network_domain
  ha_gw = false
}
