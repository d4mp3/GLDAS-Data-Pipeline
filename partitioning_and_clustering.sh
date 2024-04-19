#!/bin/bash

# Create external table
bq mk \
--external_table_definition=gs://damdezoomcamp-terra-bucket/gldas_prcp.parquet \
--table damdezoomcamp:gldas_dataset.external_gldas_prcp

# Create partitioned and clustered table
bq mk \
--time_partitioning_type=DAY \
--time_partitioning_field=datetime \
--clustering_fields=month \
--schema './schema.json' \
--table damdezoomcamp:gldas_dataset.prcp_daily_partitioned_clustered
