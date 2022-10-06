variable "name" {}

variable "cidr" {}

variable "cloud" {
  type        = map(string)
  default     = {
    "eu-central-1" = "aws",
    "us-east-1" =   "aws",
    "West Europe" = "azure"
  }
}

variable "region" {}

variable "account_name" {
  type        = map(string)
  default     = {
    "eu-central-1" = "aws-account",
    "us-east-1" =   "aws-account",
    "West Europe" = "azure-account-sec"
  }
}

# variable "ctrl_password" {}

variable "ctrl_ip" {
  default = ""
}

variable "network_domain" {}


variable "transit_gw" {
  type        = map(string)
  default     = {
    "eu-central-1" = "aws-euc1-transit-gw",
    "us-east-1"    = "aws-use1-transit-gw",
    "West Europe"  = "az-euw-transit-gw"
  }
}
