FROM python:3.12-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7001
ENTRYPOINT [ "python"]
CMD [ "mymicroservice.py" ]
 
