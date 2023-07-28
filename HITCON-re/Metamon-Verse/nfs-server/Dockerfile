FROM ubuntu:latest

RUN apt-get update && apt-get install -y nfs-kernel-server supervisor

RUN mkdir -p /data
RUN echo "/data *(rw,sync,no_subtree_check,no_root_squash)" >> /etc/exports

EXPOSE 2049

RUN mkdir -p /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
