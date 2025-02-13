FROM python:3.13.2-slim-bullseye

RUN apt update -y -q \
    && apt install -y -q --no-install-recommends \
    build-essential \
    freetds-bin \
    locales \
    lsb-release \
    sasl2-bin \
    sqlite3 \
    unixodbc \
    postgresql-client-common \
    postgresql-client\
    gcc \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

ADD requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -U --no-cache-dir psycopg2-binary
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python3 init.py", "create"]
