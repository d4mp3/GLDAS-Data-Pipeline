SELECT
  'True' AS `precipitation`,
  COUNT(*) AS `days`
FROM
  (SELECT
    `year`,
    `prcp`
  FROM
    `gldas_dataset.prcp_daily_partitioned_clustered`
  WHERE
    `year` = 2023
  ) AS subquery
WHERE
  `prcp` > 0.0

UNION ALL

SELECT
  'False' AS `precipitation`,
  COUNT(*) AS `days`
FROM
  `gldas_dataset.prcp_daily_partitioned_clustered`
WHERE
  `year` = 2023
  AND `prcp` = 0.0;