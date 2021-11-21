FROM python:latest
 
WORKDIR /szbincheckerbot/Binchecker
COPY ./Binchecker
 
RUN pip install -r requirements.txt
 
CMD ["python3","bot.py"]
