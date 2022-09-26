FROM python3:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
COPY . /ac-fullstack
WORKDIR  /ac-fullstack
CMD ["python","app.py"]
