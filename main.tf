terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.21.0"
    }
  }
}


provider "google" {
  credentials = "./.keys/creds.json"
  project     = "gldas-417901" // fill this with appropriate project id
  region      = "us-central1"
}


resource "google_storage_bucket" "gldas-bucket" {
  name          = "gldas-417901-terra-bucket"
  location      = "US"
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}