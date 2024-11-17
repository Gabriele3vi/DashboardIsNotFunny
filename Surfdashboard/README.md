Computer programming project work

## Group components 
- Bianca Sofia De Buzzaccarini - bianca-sofia.DE-BUZZACCARINI@etu.univ-amu.fr
- Gabriele Trevisan - gabriele.trevisan@etu.univ-amu.fr
- Bastien Givry  - bastien.givry@etu.univ-amu.fr

# Surf Dashboard

An interactive dashboard for analyzing and visualizing surf data, built using **R Markdown** with **flexdashboard** and **Python** for data scraping. This project integrates R and Python seamlessly, enabling efficient data retrieval and visualization.

---

## Features

- Scrapes surf data from a user-specified URL or defaults to a predefined surf report URL.
- Processes and visualizes data interactively using **plotly**.
- Computes the best day and hour within the best day for surfing based on sea quality metrics.
- Dynamically integrates a Python script for data scraping, with optional support for custom virtual environments.

---

## Requirements

### R Requirements
- R version 4.0 or later
- R packages:
  - `flexdashboard`
  - `tidyverse`
  - `plotly`
  - `lubridate`
  - `DT`
  - `here`
  - `reticulate`

### Python Requirements
- Python version 3.8 or later
- Python packages:
  - `pandas`
  - `requests`
  - `beautifulsoup4`

## Setup
You can create a virtual env for this project : 
- Create a virutal env using Windows or Linux/MacOS commands
- Activate the virtual env
- Once the new venv is active, install the required Python libraries by running in the project folder "Surf_project/": 
pip install -r surf_scrap/requirements.txt
- Ensure the required R packages are installed by running in R or RStudio :
install.packages(c("flexdashboard", "tidyverse", "plotly", "lubridate", "DT", "here", "reticulate"))

If you choose not to set up a virtual environment, ensure Python is installed and the required libraries are globally available:
- pandas
- requests
- beautifulsoup4

## Use 
- Open Surfdashboard.Rmd in RStudio
- If you created a virtual env, or want to use an existing one, specify the Python executable in the R Markdown file in the "python_env" variable
- If no virtual environment is specified (python_env <- NULL), the system’s default Python interpreter will be used.
- If you want to customize the Python script inputs from the Rmd file :  
url_input: The URL to scrape data from (default: https://www.surf-report.com/meteo-surf/lacanau-s1043.html).
export_path: The directory to save the scraped data (default: "meteo_surf_data/meteo_surf_data.csv").
- Render the R Markdown file to generate the interactive dashboard 