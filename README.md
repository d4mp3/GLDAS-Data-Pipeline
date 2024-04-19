## Problem Statement
The primary problem addressed by this project is retrieving precipitation data for the city of Warsaw from the NASA Global Land Data Assimilation System (GLDAS) API. The GLDAS provides valuable datasets for various geographical locations, including precipitation data, which is crucial for numerous applications, including climate studies, water resource management, and agricultural planning.

Additionally, the project aims to create dashboard presenting precipitation data for the years 2013-2023. The dashboard will provide insightful visualizations to facilitate better understanding and analysis of precipitation patterns over the specified period.

## Project Overview
The project involves orchestrating the execution of data pipelines to retrieve, process, and store precipitation data from the GLDAS API. These data pipelines will operate on daily and monthly cycles, ensuring the availability of up-to-date and aggregated data for analysis and visualization purposes. The ultimate goal is to store the processed data on the Google Cloud Platform for efficient storage, retrieval, and analysis, culminating in the creation of interactive dashboards.

## Data Pipeline
The data pipeline operates on a batch processing model, handling both daily and monthly frequencies seamlessly.

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
terraform apply
```

All steps were performed according to [first module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp) of the data engineering zoomcamp course. If you have any problems, you will find help there.
 
 ### Workflow Orchestration

Enter mage folder and paste into it your **creds.json** for gcp service account. Then run
```
docker compose up -d
```
You might set proper name or location for your key file in mage instance. You can use **io_config.yaml** file or use use **GOOGLE_APPLIACATION_CREDENTIALS** variable. 
All these instructions you can find with great [Matt's Palmer tutorial](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration)

After all go to **localhost:6789** in your browser and run pipelines (gldas_data_pipeline, transform_staged_gldas_to_daily, transform_staged_gldas_to_monthly)

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/2057d057-c725-405d-9682-1ce477ae2586)

You may run pipelines manually if there is an error.
To run pipeline manually go to **Pipelines -> SpecificPipeline -> Edit pipeline** and run exporter block with all upstreams like in the picture below

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/38b4a0bd-006b-4b9c-ad8a-35d53a475930)

 ### Partitioning and clustering
Use content of **partitioning_and_clustering_bq.sql** in your big queery project.
you should **rename the project name** to the one you set in gcp and variables.tf

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/b56c3832-8092-4a79-9fec-1da97f253cf7)


### Creating Dashboard
To run metabase image execute 
```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

Enter **localhost:3000** in browser and create account using your GCP creds file and make connection to BigQuery.
After all you will get access to nice GUI where you can create dashboards.

Creating by question:

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/bdf3dc18-59ea-44fd-b341-c730f36b3f55)

For creating of pie chart use sql query method included in **metabase_precipitation_days_query.sql**

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/5559c9bb-8df5-4cba-acd0-c89dc7875875)

To stop container use
```
docker stop metabase
```
or if you want to start execute
```
docker start metabase
```

## Dashboard
Dashboard showcasing Warsaw's precipitation data through four insightful charts.
You can find dashboard in **gldas_prcp_warsaw.pdf** file. 

Dashboard includes 4 charts:
1. The daily partitioned clustered precipitation, summed by year.
2. The daily partitioned clustered precipitation, summed by month for the year 2023.
3. The daily partitioned clustered precipitation, averaged by year and auto-binned by month, for years 2013-2023.
4. The number of days with precipitation specifically for the year 2023.

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/ce1ab3ad-05e1-4705-bb73-17317c4ef904)


## Quick access to data by JupyterNotebook

You can you JupyterNotebook if needed to use quick demo of pipeline.
Follow these steps to creating env for Jupyter

create virtualenv for packages
```
python3 -m venv .venv
```

activate venv
```
source .venv/bin/activate
```

install requirements
```
pip install -r requirements.txt
```

run jupyter
```
jupyter notebook
```

enter notebook **How_to_Access_the_Hydrology_Data_Rods_Time_Series_API.ipynb** via jupyter and follow the code.

[Notebook How_to_Access_the_Hydrology_Data_Rods_Time_Series_API](https://github.com/d4mp3/GLDAS-Data-Pipeline/blob/main/How_to_Access_the_Hydrology_Data_Rods_Time_Series_API.ipynb)





