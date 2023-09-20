FROM python:3.8-slim

# Install the required packages
RUN pip install google-cloud-logging

# Copy your Python script into the container
COPY log_to_gcp.py /log_to_gcp.py

CMD ["python", "/log_to_gcp.py"]