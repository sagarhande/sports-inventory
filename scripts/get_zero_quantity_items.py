import os
import json
import requests
import shutil
import time
from datetime import datetime, timedelta

API_URL = "http://localhost:8000/inventory/items?quantity=0"
INTERVAL = 60
DATA_FOLDER_PATH = "data"
DELETE_DATA_AFTER_DAYS = 1*24

def fetch_unavailable_items(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_data_to_file(data, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{directory}/unavailable_items_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Data saved to {filename}")

def manage_folders(base_path, today):
    x_days_ago = today - timedelta(hours=DELETE_DATA_AFTER_DAYS)
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        folder_date = datetime.strptime(folder_name, "%Y-%m-%d").date()

        if os.path.isdir(folder_path):
            if today > folder_date >= x_days_ago:
                zip_filename = f"{folder_path}.zip"
                shutil.make_archive(zip_filename.replace('.zip', ''), 'zip', folder_path)
                shutil.rmtree(folder_path)
                print(f"Zipped and removed old folder: {zip_filename}")

            # Delete folders older than 1 days
            if folder_date < x_days_ago:
                shutil.rmtree(folder_path)
                print(f"Deleted old folder: {folder_path}")

def main():
    while True:
        today = datetime.now().date()
        daily_directory = os.path.join(DATA_FOLDER_PATH, today.strftime("%Y-%m-%d"))
        print("Fetching unavailable items...")
        items = fetch_unavailable_items(API_URL)
        if items:
            save_data_to_file(items, daily_directory)
        else:
            print("No data to save.")
        manage_folders(DATA_FOLDER_PATH, today)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
