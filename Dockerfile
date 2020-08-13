FROM ubuntu:20.04
RUN apt-get update && apt-get install -yq \
    python3 \
    python3-pip

RUN python3 -mpip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY tba /srv/tba
WORKDIR /srv
