FROM python
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 3001
ENTRYPOINT ["python3","run.py"]