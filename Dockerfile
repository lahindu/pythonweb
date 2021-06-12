FROM python:3.8
WORKDIR /usr/src/app
COPY main.py main.py
CMD [ "python", "./main.py" ]
