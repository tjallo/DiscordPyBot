FROM python:3
ADD . /
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]
