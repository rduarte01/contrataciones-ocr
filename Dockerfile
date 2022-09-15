FROM ubuntu:20.04

#COPY libgomp.so.1 /usr/lib
ENV PY=America/Asuncion \
    DEBIAN_FRONTEND=noninteractive

# Install python3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && apt-get install -y ocrmypdf \
  && apt-get install -y poppler-utils \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && pip3 install pdf2image \
  && pip3 install python-dateutil 
  
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN apt-get install -y libgl1

WORKDIR /app

#RUN python3 -m venv /app/opt/venv

#ENV PATH="/opt/venv"

#RUN apk add ocrmypdf
#RUN apk add --no-cache tesseract-ocr


#RUN apt install -y libgl1-mesa-glx


COPY requirements.txt /app
#RUN /opt/venv/bin/python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD [ "python3", "./main.py" ]