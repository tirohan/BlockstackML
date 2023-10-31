FROM python:3.8

WORKDIR /streamlit_app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501

# Run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py"]