FROM ubuntu:latest

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
  

WORKDIR /app

#RUN python3 -m venv /app/opt/venv

#ENV PATH="/opt/venv"

#RUN apk add ocrmypdf
#RUN apk add --no-cache tesseract-ocr

COPY requirements.txt /app
#RUN /opt/venv/bin/python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD [ "python3", "./main.py" ]