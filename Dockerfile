FROM python:latest
 
WORKDIR /root/szbincheckerbot/

RUN pip install -r /root/szbincheckerbot/requirements.txt
 
CMD ["python3","Binchecker/bot.py"]
