# Usa una imagen base de Python oficial.
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias.
# Esta es una buena práctica para que Docker pueda usar el caché.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de tu aplicación al contenedor.
COPY . .

# Expone el puerto por el que se comunicará el servicio.
EXPOSE 8000

# El comando que se ejecutará cuando el contenedor se inicie.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]