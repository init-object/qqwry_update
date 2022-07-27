FROM python:alpine3.16
RUN pip install qqwry-py3
WORKDIR /qqwry
COPY update.py update.py
ENTRYPOINT [ "python", "update.py" ]