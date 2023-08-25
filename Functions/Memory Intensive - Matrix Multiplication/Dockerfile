# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the function code to the container
COPY function.py .

# Expose the port for the HTTP server 
EXPOSE 8080

# Command to start the HTTP server 
CMD ["python", "function.py"]
