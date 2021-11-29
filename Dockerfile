FROM hscleandro/prophet

ADD . /app

WORKDIR /app/src

RUN pip install -r requirements.txt

ENTRYPOINT python3 app.py

EXPOSE 8080
