FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
COPY . /ac-fullstack
WORKDIR  /ac-fullstack
RUN chmod -R a+rwx /ac-fullstack/templates
CMD ["python","app.py"]
