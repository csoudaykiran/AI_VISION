# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python files to the working directory
COPY custom_face_detection.py .
COPY image_storage.py .

# Copy the images folder to the working directory
COPY images/ ./images/

# Set the command to run your Python script
CMD ["python", "custom_face_detection.py"]
