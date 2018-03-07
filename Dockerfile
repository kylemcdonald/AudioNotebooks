FROM python:2-jessie

RUN echo "deb http://deb.debian.org/debian jessie main contrib non-free" > /etc/apt/sources.list
RUN echo "deb-src http://deb.debian.org/debian jessie main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://deb.debian.org/debian jessie-updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://deb.debian.org/debian jessie-updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://security.debian.org/debian-security/ jessie/updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://security.debian.org/debian-security/ jessie/updates main contrib non-free" >> /etc/apt/sources.list

RUN apt-get update -y
RUN apt-get install -y libsamplerate0 libsamplerate0-dev

RUN pip install numpy
RUN pip install scikits.samplerate

WORKDIR /AudioNotebooks

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD /bin/bash

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root