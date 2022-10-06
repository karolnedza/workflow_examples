provider "aviatrix" {
  # username = "admin"
  controller_ip = var.ctrl_ip
  # password = var.ctrl_password
}

terraform {
    required_providers {
      aviatrix = {
            source  = "aviatrixsystems/aviatrix"
            version = "2.23.0"
        }
    }
}
