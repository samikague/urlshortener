FROM python:3.13.2
WORKDIR /usr/urlshortener/
EXPOSE 8000
COPY ./ ./
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]