
# Pull image
FROM python:3

ENV PYTHONUNBUFFERED 1

# Setup working directory
WORKDIR /code


COPY requirements.txt /code

RUN pip3 install -r requirements.txt

# COPY  . .

# EXPOSE 8000


# ENTRYPOINT [ "python3" ]

# CMD [ "manage.py", "runserver" ]

# RUN python3 docker_complete.py

# docker build -t robotgyal/personal-site .
# docker run -d -p 8000:8000 robotgyal/personal-site