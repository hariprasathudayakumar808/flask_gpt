FROM python:3.9-slim

# Set the working directory

WORKDIR /my-app

# Copy the current directory contents into the container at /my-app

COPY . /my-app/

# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container

EXPOSE 5001

# Define environment variable

ENV FLASK_ENV=production

# Run app.py when the container launches

CMD ["python", "app.py"]