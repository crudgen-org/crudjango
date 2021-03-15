FROM python:3.7

WORKDIR /

COPY requirements.txt /requirements.txt 

RUN pip install -r requirements.txt

COPY crud_operator.py /crud_operator.py 

CMD kopf run /crud_operator.py --standalone --all-namespaces
