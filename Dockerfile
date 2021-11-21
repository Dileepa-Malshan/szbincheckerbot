FROM python:latest
 
WORKDIR /usr/local/bin
COPY bot.py .
 
RUN pip install -r requirements.txt
 
CMD ["python3","bot.py"]
