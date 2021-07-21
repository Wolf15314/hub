#FROM ubuntu:latest
FROM amazonlinux:latest
MAINTAINER Wolf 'ancyfer.w@gmail.com'
#RUN apt-get update -y
#RUN apt-get install -y python python3-pip python-dev build-essential
RUN yum install -y python python3-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["hello.py"]