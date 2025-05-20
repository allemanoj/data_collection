import time

def run_scheduler(logger):
    ...
    while True:
        try:
            logger.info("Fetching XML data...")
            ...
            logger.info("Uploading to S3...")
            ...
            logger.info(" Completed cycle. Sleeping...\n")
            time.sleep(30)

        except Exception as e:
            logger.error(f"Error occurred: {str(e)}", exc_info=True)
            time.sleep(30)
