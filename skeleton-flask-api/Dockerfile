FROM python:3.10.4

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m" , "flask", "--debug", "run", "--host=0.0.0.0"]