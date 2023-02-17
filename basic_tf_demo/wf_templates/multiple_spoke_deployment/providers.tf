provider "aviatrix" {
  # username = "admin"
  controller_ip = "52.3.72.231"
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
