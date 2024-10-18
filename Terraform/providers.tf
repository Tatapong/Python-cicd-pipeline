provider "aws" {
  default_tags {
    tags = local.tags
  }
}

terraform {
  required_providers {
    aws = {
    }
  }

  required_version = ">= 1.4.2"
}