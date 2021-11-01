FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PATH="/home/newsboardapi/.local/bin:${PATH}" \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update &&\
    apt-get -y install python3-psycopg2 &&\
    useradd -m newsboardapi

USER newsboardapi

WORKDIR /home/newsboardapi

COPY --chown=newsboardapi:newsboardapi newsboard newsboard
COPY --chown=newsboardapi:newsboardapi api api
COPY --chown=newsboardapi:newsboardapi requirements.txt requirements.txt
COPY --chown=newsboardapi:newsboardapi manage.py manage.py
COPY --chown=newsboardapi:newsboardapi Procfile Procfile

RUN pip install --no-cache-dir --user -r requirements.txt

CMD ["python", "./manage.py", "runserver", "0.0.0.0:${PORT}"]
