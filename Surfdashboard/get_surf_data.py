import argparse
from surf_scrap import scrap_surf_data

def main():
    parser = argparse.ArgumentParser(description="Scrape surf data and save to CSV.")
    parser.add_argument(
        "--url_input", 
        type=str, 
        default="https://www.surf-report.com/meteo-surf/lacanau-s1043.html", 
        help="The URL of the surf report page."
    )
    parser.add_argument(
        "--export_path", 
        type=str, 
        default=None, 
        help="Path to save the exported CSV. Default is the current working directory."
    )
    args = parser.parse_args()

    # Call the function with the provided arguments
    scrap_surf_data(url_input=args.url_input, export_path=args.export_path)

if __name__ == "__main__":
    main()
