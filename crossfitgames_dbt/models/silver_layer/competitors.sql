WITH transformed_data AS (
    SELECT DISTINCT
      competitorId,
      competitorName,
      {{ add_audit_columns() }}  -- Calls the macro here
    FROM {{ source('crossfitgames', 'competitors') }}
)
SELECT * FROM transformed_data
