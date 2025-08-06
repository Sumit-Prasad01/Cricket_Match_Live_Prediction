import requests
import json
import os
import sys
from exception.exception import CricketMatchException

class FetchData:
    def __init__(self, url, header):
        self.url = url
        self.header = header

    
    def fetch_and_save(self, filename='live_score.json'):
        try:
            r = requests.get(self.url, self.header)
            r.raise_for_status()
            data = r.json()

            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)

            print(f"Data successfully saved to {filename}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
        except Exception as e:
            raise CricketMatchException(e,sys)