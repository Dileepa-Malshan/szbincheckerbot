FROM python:latest
 
WORKDIR /root/szbincheckerbot/

RUN pip install -r requirements.txt
 
CMD ["python3","Binchecker/bot.py"]
