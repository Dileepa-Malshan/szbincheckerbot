FROM python:latest
 
WORKDIR /Binchecker
COPY bot.py .
 
RUN pip install -r requirements.txt
 
CMD ["python3","bot.py"]
