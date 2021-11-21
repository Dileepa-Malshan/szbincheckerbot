FROM python:latest
 
WORKDIR /Binchecker
COPY . /Binchecker
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["bot.py"]
