FROM python:3.11-slim
RUN pip install flask mysql-connector-python
WORKDIR /app
COPY app.py app.py
EXPOSE 5000
CMD ["python3", "app.py"]
