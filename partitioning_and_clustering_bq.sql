CREATE OR REPLACE EXTERNAL TABLE `damdezoomcamp.gldas_dataset.external_gldas_prcp`
OPTIONS (
  format = 'Parquet',
  uris = ['gs://damdezoomcamp-terra-bucket/gldas_prcp.parquet']
);

CREATE OR REPLACE TABLE `damdezoomcamp.gldas_dataset.prcp_daily_partitioned_clustered`
PARTITION BY DATE_TRUNC(datetime, YEAR)
CLUSTER BY month AS
SELECT * FROM `damdezoomcamp.gldas_dataset.prcp_daily`;