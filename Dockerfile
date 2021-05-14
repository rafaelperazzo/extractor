FROM python:latest

WORKDIR /usr/src/app

RUN pip install --no-cache-dir requests zeep

ENV TZ=America/Fortaleza

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD [ "python", "./lattes_extractor.py" ]
