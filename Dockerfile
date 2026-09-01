# Using an official Python base image
FROM python:3.10-slim

LABEL AUTHOR='SachinK Training'
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (requirements.txt) and the source code
COPY requirements.txt requirements.txt
COPY temperature.py temperature.py

# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



