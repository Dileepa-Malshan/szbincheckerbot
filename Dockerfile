FROM python:latest
 
WORKDIR /binchecker
COPY . /binchecker
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["bot.py"]
