from google.cloud import logging

def log_message():
    # Instantiates a client
    client = logging.Client()

    # The name of the log to write to
    logger = client.logger('my-custom-log')  # You can choose any name

    # Log with the desired severity
    logger.log_struct(
        {"message": "This is an ERROR message for GCP logs"},
        severity="ERROR",
    )

if __name__ == "__main__":
    log_message()
