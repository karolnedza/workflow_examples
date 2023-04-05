provider "aviatrix" {
  # username = "admin"
  controller_ip = "18.192.136.69"
  # password = var.ctrl_password
}

terraform {
    required_providers {
      aviatrix = {
            source  = "aviatrixsystems/aviatrix"
            version = "=3.0.0"
        }
    }
}
