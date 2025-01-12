
WITH transformed_data AS (
    SELECT DISTINCT
      rank
    FROM crossfitgames.main.scores
)
SELECT * FROM transformed_data