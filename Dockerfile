FROM ubuntu:18.04
MAINTAINER thusharaj "thushara.k.jayakody@icloud.com"

RUN mkdir -p /networkautomation
WORKDIR /networkautomation
COPY . .

RUN apt-get install python -y
RUN apt-get --yes --force-yes install python-pip
RUN pip install cryptography
RUN pip install -r Buildjobpipfile.txt

ENTRYPOINT [ "python" ]

CMD [ "networkautomation/corelayerswitchvlansconfnetmiko.py" ]
