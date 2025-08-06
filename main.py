import logging
import os
import sys
from dotenv import load_dotenv, find_dotenv
from components.data_fetcher import FetchData
from logger.log_setup import setup_logging
from exception.exception import CricketMatchException

setup_logging()
logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())
url_for_score = os.environ.get('LIVE_SCORE_API')
headers = os.environ.get('headers')

if __name__ == "__main__":
    try:

        if url_for_score and headers:
            logger.info("Starting the data fetching process.")
            
            score_data_fetcher = FetchData(url_for_score, headers)
            score_data_fetcher.fetch_and_save('live_score.json')
            
            logger.info("Data fetching process finished successfully.")
        else:
            logger.error("LIVE SCORE API environment variable is not set. Please check your .env file.")

    except Exception as e:
           raise CricketMatchException(e,sys)