FROM python:3.13.2-slim-bullseye

RUN apt update -y -q \
    && apt install -y -q --no-install-recommends \
    build-essential \
    freetds-bin \
    krb5-user \
    ldap-utils \
    libffi6 \
    libsasl2-2 \
    libsasl2-modules \
    libssl1.1 \
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
RUN pip install --upgrade pip
RUN pip install -U --no-cache-dir psycopg2-binary

ADD main.py /app/

WORKDIR /app/