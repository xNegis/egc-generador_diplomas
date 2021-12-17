FROM python:3.9.2-alpine
WORKDIR /code
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN apk add --no-cache \
        xvfb \
        ttf-dejavu ttf-droid ttf-freefont ttf-liberation \
wkhtmltopdf \
    ;
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]