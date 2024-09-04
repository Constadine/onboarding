import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os

def fetch_articles(url: str, output_filename: str) -> tuple[str, list]:
    # Ensure the directory structure exists
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    # Send the GET request to the API
    response = requests.get(url)
    
    # Check for a successful response
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        
        # Print the total number of results
        print(f"Total results found: {data.get('totalResults', 0)}")
        
        # Define the file name using the current date
        file_name = f"{output_filename}_{datetime.now().strftime('%Y%m%d')}.json"
        
        # Save the raw data
        with open(file_name, 'w') as f:
            print(f"Saving raw data to: {file_name}")
            json.dump(articles, f)
        
        return file_name, articles
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return []
