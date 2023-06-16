FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN pip3 install requests
RUN pip3 install pytest
RUN pip3 install jsonschema

ENV BASE_URL=https://jsonplaceholder.typicode.com

CMD ["pytest", "./test.py"]
