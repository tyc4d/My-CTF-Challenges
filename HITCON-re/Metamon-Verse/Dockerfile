FROM ubuntu:20.04

EXPOSE 80/tcp

RUN apt update && apt install -y libcurl4-openssl-dev openssl libssl-dev python3 python3-pip nfs-common
RUN apt install iputils-ping -y
RUN pip3 install pycurl flask certifi

COPY app/                 /app
COPY files/readflag       /readflag
COPY files/flag           /flag
COPY files/entrypoint.sh  /

WORKDIR /app/
CMD ["/entrypoint.sh"]