terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "eu-central-1"
}

variable "bucket_name" {
  type = string
  description = "Globally unique S3 bucket name"
}

resource "aws_s3_bucket" "portfolio_data" {
  bucket = var.bucket_name
}

output "bucket_name" {
  value = aws_s3_bucket.portfolio_data.bucket
}
