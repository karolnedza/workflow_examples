provider "aviatrix" {
  # username = "admin"
  controller_ip = "35.161.94.163"
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
