import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrap_surf_data(url_input="https://www.surf-report.com/meteo-surf/lacanau-s1043.html", export_path=None):
    """
    Scrapes surf meteo data from the specified URL from this website "https://www.surf-report.com/meteo-surf/" and saves it as a CSV file.
    
    :param url_input: The URL of the meteo surf report page to scrape. Default is set to a specific Lacanau page.
                       Example: "https://www.surf-report.com/meteo-surf/lacanau-s1043.html".
    :type url_input: str, optional
    :param export_path: The folder path to save the CSV file. 
                         If not provided, a default folder will be created in the current working directory.
    :type export_path: str, optional
    :return: None
    :raises Exception: If there is an error while exporting the data to a CSV file, an error message will be printed.

    Example:
    - scrap_surf_data("https://www.surf-report.com/meteo-surf/lacanau-s1043.html", "/path/to/save")
    - This will scrape the surf data from the given URL and save it as "meteo_surf_data.csv" in the specified path.
    """
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    headers = {'User-Agent': user_agent}
    
    page = requests.get(url_input, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser') 
    
    forecast_tab = soup.find_all('div', class_='forecast-tab')

    data_collected = {}

    for tab in forecast_tab:
        date = tab.find("div", class_='title').find("b").text
        time = tab.find_all('div', class_='cell date with-border') 
        waves = tab.find_all("div", class_="cell large waves with-border") 
        wind_speed = tab.find_all("div", class_="cell large-bis-bis with-border")
        wind_direction = tab.find_all("div", class_="wind img")
        temperature = tab.find_all("div", class_="micro temp")

        times_list = [el.text.strip() for el in time]
        waves_list = [el.text.strip() for el in waves]
        wind_speed_list = [el.text.strip() for el in wind_speed]
        wind_direction_list = [el.find('img')['alt'].strip() for el in wind_direction]
        temperature_list = [el.text.strip() for el in temperature]
    
        data_collected[date] = {
            'hour': times_list,
            'waves_size': waves_list,
            'wind_speed': wind_speed_list,
            'wind_direction': wind_direction_list,
            'temperature': temperature_list
        }
    
    flattened_data = []

    for day, values in data_collected.items():
        for i in range(len(values['hour'])):
            flattened_data.append({
                'day': day,
                'hour': values['hour'][i],
                'waves_size': values['waves_size'][i],
                'wind_speed': values['wind_speed'][i],
                'wind_direction': values['wind_direction'][i],
                'temperature': values['temperature'][i]
            })

    # Create the DataFrame
    df = pd.DataFrame(flattened_data)

    # If no export path is provided, create a default folder in the current working directory
    if export_path is None:
        default_dir = os.path.join(os.getcwd(), 'meteo_surf_data')
        os.makedirs(default_dir, exist_ok=True)
        export_path = default_dir
    
    full_export_path = os.path.join(export_path, 'meteo_surf_data.csv')
    
    try:
        df.to_csv(full_export_path, index=False)
        # print(f"Data saved into csv file to {full_export_path}")
    except Exception as e:
        print(f"Error during the exporting process: {e}")

    return