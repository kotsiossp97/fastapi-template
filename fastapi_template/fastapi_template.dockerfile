FROM python:latest

WORKDIR /fastapi/

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --upgrade -r requirements.txt

# Copy App
COPY . .

RUN chmod +x start.sh
ENV PYTHONPATH=/fastapi


EXPOSE 80
CMD [ "bash", "/fastapi/start.sh" ]

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
