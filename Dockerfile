# Dockerfile
FROM python:3.10

# Configura el directorio de trabajo en el contenedor
WORKDIR /code

# Copia el archivo de requisitos
COPY requirements.txt /code/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo en el contenedor
COPY . /code/

# Expone el puerto 8000 para el servidor de Django
EXPOSE 8000
