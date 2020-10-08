FROM python:latest

WORKDIR /usr/src/app

RUN pip install --no-cache-dir numpy sympy pandas requests bs4 matplotlib zeep
RUN pip install --no-cache-dir unidecode
RUN pip install progressbar2
ENV TZ=America/Fortaleza

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD [ "python", "./lattes_extractor.py" ]
