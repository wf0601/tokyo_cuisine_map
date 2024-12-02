# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the data preparation script
RUN python data_preparation.py

# Make port 5003 available to the world outside this container
EXPOSE 5004

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]