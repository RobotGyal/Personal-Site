
# Pull image
FROM python:3

ENV PYTHONUNBUFFERED 1

# Setup working directory
WORKDIR /code

# Move requirements file into working directory in conatiner
COPY ./requirements.txt /code

# Setup working directory
WORKDIR /code

# Install requirements in the working directory
RUN pip3 install -r requirements.txt