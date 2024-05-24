# Wybieramy bazowy obraz z Pythonem
FROM python:3.9-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik requirements.txt do kontenera
COPY requirements.txt .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy pozostałe pliki aplikacji do kontenera
COPY . .

# Ustawiamy komendę, która ma być wykonana przy starcie kontenera
CMD ["python", "main.py"]
