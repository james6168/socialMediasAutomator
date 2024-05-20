# Use an official Python runtime as a parent image
FROM python:3.10 as builder

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PLAYWRIGHT_BROWSERS_PATH=/usr/bin/chromium-browser

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install playwright
RUN pip install playwright==1.43.0 && \
    playwright install --with-deps chromium

# Copy project
COPY . .

# Use a smaller parent image
FROM python:3.10-slim

# Install system dependencies in the final image
RUN apt-get update && apt-get install -y \
    libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 \
    libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 \
    libnss3 lsb-release xdg-utils libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy only the compiled python dependencies from the builder image
COPY --from=builder /usr/local /usr/local

# Copy the browsers from the builder image
COPY --from=builder /usr/bin/chromium-browser /usr/bin/chromium-browser

# Copy the application from the builder image
COPY --from=builder /app /app

# Set work directory
WORKDIR /app

# Run the application
CMD ["gunicorn", "main.wsgi:application"]