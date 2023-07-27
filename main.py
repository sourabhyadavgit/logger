# main.py

from logger import setup_logger



def main():
    
    logger_endpoint1 = setup_logger('api.endpoint1', "C:/Users/saura/OneDrive/Desktop/Project/work-related/endpoint1.log")
    logger_endpoint2 = setup_logger('api.endpoint2', "C:/Users/saura/OneDrive/Desktop/Project/work-related/endpoint2.log")
    # Now you can use the loggers to log messages specific to each endpoint
    logger_endpoint1.info('This is a message from endpoint 1')
    logger_endpoint2.info('This is a message from endpoint 2')
    #logger.info("Starting the main program.")
    #logger.info("Exiting the main program.")
    logger_endpoint1.debug('This is a debug message')
    logger_endpoint1.info('This is an info message')
    logger_endpoint1.warning('This is a warning message')
    logger_endpoint2.error('This is an error message')
    logger_endpoint2.critical('This is a critical message')


if __name__ == "__main__":
    main()
