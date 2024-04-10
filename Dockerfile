FROM ubuntu:latest
RUN apt-get update -y; apt-get install fortune-mod cowsay netcat -y

RUN mkdir /opt/wisecow
COPY ./wisecow.sh /opt/wisecow
RUN ln -s /usr/games/cowsay /usr/bin/cowsay ; ln -s /usr/games/fortune /usr/bin/fortune
EXPOSE 4499
CMD ["sh","/opt/wisecow/wisecow.sh"]


