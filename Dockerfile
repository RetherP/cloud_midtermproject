FROM python:3.11.9
WORKDIR /app
ADD . /app
RUN pip install flask
EXPOSE 80
CMD ["python", "app.py"]