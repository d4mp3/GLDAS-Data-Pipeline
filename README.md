## Problem Statement
The primary problem addressed by this project is retrieving precipitation data for the city of Warsaw from the NASA Global Land Data Assimilation System (GLDAS) API. The GLDAS provides valuable datasets for various geographical locations, including precipitation data, which is crucial for numerous applications, including climate studies, water resource management, and agricultural planning.

Additionally, the project aims to create dashboard presenting precipitation data for the years 2013-2023. The dashboard will provide insightful visualizations to facilitate better understanding and analysis of precipitation patterns over the specified period.

## Project Overview
The project involves orchestrating the execution of data pipelines to retrieve, process, and store precipitation data from the GLDAS API. These data pipelines will operate on daily and monthly cycles, ensuring the availability of up-to-date and aggregated data for analysis and visualization purposes. The ultimate goal is to store the processed data on the Google Cloud Platform for efficient storage, retrieval, and analysis, culminating in the creation of interactive dashboards.

## Implementation Approach
1. **Jupyter Notebook**: Include a Jupyter Notebook presenting a simpler version of data retrieval from the GLDAS API and visualization of the retrieved data using charts. This notebook serves as a demonstration of the data retrieval and visualization process for educational and exploratory purposes.
2. **Data Retrieval**: Utilize the GLDAS API to fetch precipitation data specifically for the city of Warsaw.
3. **Data Processing**: Orchestrate data pipelines to process the retrieved data on daily and monthly intervals.
4. **Data Storage**: Store processed data on the Google Cloud Platform, leveraging the advantages of cloud storage for scalability, reliability, and accessibility.
5. **Data Analysis**: Employ BigQuery script to create partitioned and clustered tables in BigQuery. This optimization strategy, utilizing columns such as datetime and month, aims to enhance query performance and reduce overall cloud computing costs.
6. **Dashboard Creation**: Utilize Metabase, an open-source business intelligence tool, to create interactive dashboards for visualizing the precipitation data. These dashboards will provide insights into precipitation patterns from 2013 to 2023, facilitating data-driven decision-making and analysis.

## Technologies Used
- **NASA GLDAS API**: Source for precipitation data retrieval.
- **Google Cloud Platform (GCP)**: Cloud infrastructure for data storage and analysis.
- **Google Cloud Storage**: Provides scalable and durable object storage for storing processed data and other project artifacts.
- **BigQuery**: Google's fully managed, serverless data warehouse for querying and analyzing large datasets.
- **Terraform**: Infrastructure as code tool used for provisioning and managing cloud resources.
- **Mage**: Workflow management platform for orchestrating complex data pipelines.
- **Metabase**: Open-source business intelligence tool for creating interactive dashboards and visualizations.

## Acknowledgments

This project relies on the following Python libraries and their dependencies:

- **requests**: Used for making HTTP requests to the NASA GLDAS API to retrieve precipitation data.
- **pandas**: Utilized for data manipulation and analysis, facilitating efficient handling of the retrieved precipitation data.
- **numpy**: Essential for numerical computing tasks, employed for various data processing operations.
- **datetime**: Python's built-in datetime module is utilized for date and time manipulation, particularly in organizing and analyzing temporal data.
- **urllib**: Provides utility functions for working with URLs, used for encoding query parameters for API requests.

## Reproducibility

### Pre-Requisites
1. Terraform client installation: https://www.terraform.io/downloads
2. Cloud Provider account: https://console.cloud.google.com/

### Infra
1. Create google service account with following permissions: **Storage Admin, BigQuery Admin and Compute Admin**.
2. Generate **service account key** and put it in your host.
3. Set variables for your gcp project in **variables.tf** file

After these steps initialize tf in folder of the repo:
```
terraform init
```

and then run
```
terraform init
```

All steps were performed according to [first module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp) of the data engineering zoomcamp course. If you have any problems, you will find help there.
 
 
