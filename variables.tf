variable "credentials" {
  description = "My Credentials"
  default     = "./.keys/creds.json"
}

variable "project" {
  description = "Project"
  default     = "damdezoomcamp"
}

variable "region" {
  description = "Region"
  default     = "europe-north1"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuerry Dataset Name"
  default     = "gldas_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "damdezoomcamp-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
