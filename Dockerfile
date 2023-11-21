# Usa la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto en un entorno virtual
RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate && pip install --no-cache-dir -r requirements.txt"

# Copia el contenido del directorio actual al contenedor en /app
COPY . /app

# Expone el puerto 5000 para que pueda ser accedido desde fuera del contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicia el contenedor
CMD ["/bin/bash", "-c", "source venv/bin/activate && python manage.py migrate && python manage.py runserver 0.0.0.0:5000"]

