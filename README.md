# CrossfitGames

## Description

This repository contains a collection of functions that allow you to collect data from the Crossfit Games leaderboard open API. You can use this repository to access structured data from the Crossfit Games open API for analysis.

It also shows how to use duckdb and dbt to write the files to a database and using dbt to transform the data to usable data models.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

Before starting work on this project, ensure you:

1. Create a virtual environment

   ```bash
   python3 -m venv crossfitgames-env
   ```
2. Activate the virtual environment.

   ```bash
   source crossfitgames-env/bin/activate
    ```  
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Installing the Project

To use the functions in the `src` directory, you must install the project as a Python package. This allows you to import the functions into your scripts or notebooks.

1. From the project's root directory, run the following command to install the package in editable mode:

   ```bash
   pip install -e .
   ```

2. Once installed, you can import the package in your Python scripts or notebooks as shown below:

   ```python
   from crossfitgames.api.api_calls import games_info_competitors

   # Example usage
   data = games_info_competitors(2024, 2)
   print(data)
   ```

This ensures that the `src` directory is properly recognized as a module and can be imported into any environment where the package is installed.

### Data Model

To include competitor names in your analysis, you need to join the following data:

- `games_info_competitors` or `games_info_competitors_multiple`
- `games_info_scores` or `games_info_scores_multiple`

## Improvements on the Roadmap

- Fixing data quality issues.
- Adding unit testing for transformation functions and improving overall data quality testing.
- Expanding functionality to include all competitions (e.g., regionals, sanctionals, the Open).
- Finishing the dbt models

## Project Structure

```
├── LICENSE
├── README.md          
├── data               <- Directory where api_call.py writes the data.
├── notebooks          <- Jupyter notebooks for demonstrating api_calls usage and exploratory data analysis (EDA).
├── requirements.txt   <- Dependencies for reproducing the analysis environment.
├── setup.py           <- Makes the project pip-installable (pip install -e .) so `src` can be imported.
├── src                <- Source code for this project.
│   ├── __init__.py    <- Makes `src` a Python module.
│   ├── crossfitgames  <- Scripts for downloading or generating data.
│   │   ├── utils      <- Transformation functions and demo scripts for reading and writing data.
│   │   ├── api        <- Main scripts for API calls and writing data.
```

---
