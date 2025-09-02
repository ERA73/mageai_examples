FROM mageai/mageai:0.9.76

WORKDIR /home/src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .