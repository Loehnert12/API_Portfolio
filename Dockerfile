# Use official lightweight Python image
FROM python:3.11-slim
 
# Set working directory inside the container
WORKDIR /app
 
# Copy and install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the rest of the project
COPY app.py .
COPY .streamlit/ .streamlit/
COPY src/ src/
COPY utils/ utils/
 
# Expose Streamlit's default port
EXPOSE 8501
 
# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
