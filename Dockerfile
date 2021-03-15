FROM docker:dind

WORKDIR /

ENV PYTHONUNBUFFERED=1
RUN apk --no-cache add --update alpine-sdk python3 python3-dev && ln -sf python3 /usr/bin/python
RUN python -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools wheel

COPY requirements.txt /requirements.txt 
RUN pip3 install -r requirements.txt

COPY entrypoint.sh entrypoint.sh

COPY crud_operator.py /crud_operator.py 

CMD sh entrypoint.sh
