# Use the official Python image as a base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Install any dependencies
RUN pip install -r requirements.txt

# Expose the port that your app runs on
EXPOSE 5000

# Define the command to run your app
CMD ["python", "app.py"]
