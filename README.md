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

After completing these steps, initialize Terraform in the repository folder:
```
terraform init
```

Then run:
```
terraform apply
```

All steps were performed according to [first module](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp) of the data engineering zoomcamp course. If you have any problems, you will find help there.
 
 ### Workflow Orchestration

Navigate to the Mage folder and paste your **creds.json** for the GCP service account. Then run
```
docker compose up -d
```
You may set the proper name or location for your key file in the Mage instance.
Use **io_config.yaml** file or **GOOGLE_APPLIACATION_CREDENTIALS** variable. 
For detailed instructions, refer to [Matts Palmer's tutorial](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration) in the course materials.
 
Afterward, go to localhost:6789 in your browser and run the pipelines (gldas_data_pipeline, transform_staged_gldas_to_daily, transform_staged_gldas_to_monthly).

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/2057d057-c725-405d-9682-1ce477ae2586)

You may run pipelines manually if an error occurs. To do so, go to **Pipelines -> SpecificPipeline -> Edit pipeline** and run the exporter block with all upstreams, as shown in the picture below:

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/38b4a0bd-006b-4b9c-ad8a-35d53a475930)

 ### Partitioning and clustering
Use the content of **partitioning_and_clustering_bq.sql** in your BigQueery project.
Ensure to **rename the project name** to the one you set in gcp and variables.tf

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/b56c3832-8092-4a79-9fec-1da97f253cf7)


### Creating Dashboard
To run metabase image, execute: 
```
docker run -d -p 3000:3000 --name metabase metabase/metabase
```

Enter **localhost:3000** in your browser and create an account using your GCP creds file. Then, make connection to BigQuery.
After completing these steps, you'll gain access to a user-friendly GUI where you can create dashboards.

You can create dashboards using questions or SQL queries. For detailed instructions, refer to the provided resources.

Creating by question:

![image](https://github.com/d4mp3/GLDAS-Data-Pipeline/assets/61472346/bdf3dc18-59ea-44fd-b341-c730f36b3f55)

For creating of pie chart use SQL query method included in **metabase_precipitation_days_query.sql**

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

You can use the Jupyter Notebook for a quick demo of the pipeline. Follow these steps to set up the environment:

create a virtualenv for packages
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

Navigate to the notebook How_to_Access_the_Hydrology_Data_Rods_Time_Series_API.ipynb and follow the provided instructions in the code.
Remember to set proper kernel in JupyterLab

The notebook can be found in the link posted below.
[How_to_Access_the_Hydrology_Data_Rods_Time_Series_API](https://github.com/d4mp3/GLDAS-Data-Pipeline/blob/main/How_to_Access_the_Hydrology_Data_Rods_Time_Series_API.ipynb)





