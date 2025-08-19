# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=babyshop.settings \
    PORT=8025

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY babyshop_app/ /app/

# Create media directory for file uploads
RUN mkdir -p /app/media

# Create migrations and migrate database
RUN python manage.py makemigrations
RUN python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8025 for the Django application
EXPOSE 8025

# Add non-root user for security
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8025"]
