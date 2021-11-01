FROM condaforge/miniforge3:latest

MAINTAINER Lei Fan "leifan89@gmail.com"

WORKDIR /app

COPY start.sh /app/start.sh
COPY model-service /app/model-service

RUN conda install Flask mypy pandas psycopg2 pyyaml scikit-learn

ENV FLASK_APP=model-service
ENV FLASK_ENV=development

CMD ["/app/start.sh"]
