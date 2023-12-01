FROM python:3.9
WORKDIR /app
COPY /templates /app/templates/
COPY requirements.txt .
COPY app.py .
COPY app_test.py .
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt
RUN python3 -m unittest discover -p app_test.py


EXPOSE 5000
CMD python app.py
