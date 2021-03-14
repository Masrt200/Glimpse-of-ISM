FROM ubuntu:latest

RUN apt-get update && apt-get install -y\
	vsftpd \
	systemctl

RUN mkdir -p /var/ftp/pub
RUN chown nobody:nogroup /var/ftp/pub
RUN echo "vsftpd test file" | tee /var/ftp/pub/test.txt
RUN systemctl restart vsftpd

EXPOSE 21