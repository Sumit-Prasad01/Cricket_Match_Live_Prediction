import sys
import logging 
from logger.log_setup import setup_logging 


class CricketMatchException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        _, _, exc_tb = error_details.exc_info()
        
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))
        
if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        logger.info("Entering the try block.")
        a = 1/0
        print("This will not be printed.", a)
    except Exception as e:
        logger.error(f"Caught an exception: {e}")
        raise CricketMatchException(e, sys)


        