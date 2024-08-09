# Usa una imagen base de Python
FROM python:3.12.3-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt y lo instala
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el contenido de tu aplicación en el contenedor
COPY . .

# Expone el puerto que usará la aplicación Flask
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0"]
