FROM python:3.7.4
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5100
CMD [ "python", "server.py" ]