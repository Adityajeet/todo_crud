# Use the official Python image from the Docker Hub
FROM python:3.11.7

# Set environment variables to prevent Python from writing pyc files to disk
# and to buffer output for easier debugging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev default-libmysqlclient-dev libmariadb-dev-compat \
    && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the port that the Django app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
