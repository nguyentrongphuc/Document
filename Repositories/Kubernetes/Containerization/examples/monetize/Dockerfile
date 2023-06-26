FROM python:3.7.2-slim

# copy the requirements file into the image
#COPY ./requirements.txt /app/requirements.txt

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
#RUN pip install flask

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]