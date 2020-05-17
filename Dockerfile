
# Pull image
FROM python:3

# Setup working directory
WORKDIR /code

COPY requirements.txt /code

RUN pip3 install -r requirements.txt

COPY  . .

ENTRYPOINT [ "python3" ]

CMD [ "maanage.py", "runserver" ]

RUN python3 docker_complete.py