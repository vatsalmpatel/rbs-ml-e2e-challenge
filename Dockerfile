FROM python:3.7.9-slim

COPY ./app /app
COPY ./requirements.txt /requirements.txt
COPY ./yolo_signature.pt /yolo_signature.pt

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6 -y \
        build-essential \
        python3-dev \
        python3-setuptools \
    && apt-get remove -y --purge build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN python3 -m pip install -r requirements.txt

ENV PORT=8000
EXPOSE 8000

CMD ["python", "app/main.py"]