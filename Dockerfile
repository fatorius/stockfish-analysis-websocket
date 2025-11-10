FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y wget unzip && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/official-stockfish/Stockfish/releases/latest/download/stockfish-ubuntu-x86-64-avx2.tar \
    && tar -xf stockfish-ubuntu-x86-64-avx2.tar \
    && mv -T stockfish* /usr/local/bin/stockfish || mv stockfish /usr/local/bin/stockfish \
    && chmod +x /usr/local/bin/stockfish \
    && rm -rf stockfish-ubuntu-x86-64-avx2.tar

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]