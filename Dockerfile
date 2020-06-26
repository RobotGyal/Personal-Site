
# Pull image
FROM python:3

# Set environment variable
ENV PYTHONUNBUFFERED 1

# Setup working directory
WORKDIR /code

# Move django app folder into working directory in conatiner
COPY ./personal_site/ /code

# Move requirements file into working directory in conatiner
COPY requirements.txt /code

# Install requirements in the working directory
RUN pip3 install -r requirements.txt
