# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos e instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Copia el script wait-for-it.sh al contenedor
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Expón el puerto en el que la aplicación escuchará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "/wait-for-it.sh", "db:5432"]
