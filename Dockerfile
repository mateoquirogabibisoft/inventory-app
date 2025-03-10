# Use a base Python image (version 3.9 in this case)
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependencies file to the container
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all application code to the container
COPY . .

# Expose the port where the application will run (5000)
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
