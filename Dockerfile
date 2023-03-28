FROM python:3.8-slim-buster


# Install pip requirements
RUN pip install --upgrade openai
RUN pip install flask
RUN pip install flask-restful
RUN pip install gunicorn

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1" ,"--threads", "8", "--timeout", "0" ,"app:app"]


