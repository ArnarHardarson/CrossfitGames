# Assuming the function file_to_duckdb is defined above
from files_to_duckdb import file_to_duckdb

# Parameters
database = "crossfitgames"
file_and_table = [["games_info_scores_multiple_20250101_135456.csv", "scores"], ["games_info_competitor_multiple_20250101_135306.csv","competitors"]]
schema = "bronze_layer"

# Call the function
for combo in file_and_table:
  file_name = combo[0]
  table_name = combo[1]
  file_to_duckdb(database, file_name, schema, table_name) 
