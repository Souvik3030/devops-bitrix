FROM php:8.1-fpm

# Install required packages
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    libzip-dev \
    && docker-php-ext-install mysqli pdo pdo_mysql zip

WORKDIR /var/www/html

# Copy installed Bitrix files into image
COPY bitrix/www /var/www/html

# Set permissions
RUN chown -R www-data:www-data /var/www/html

EXPOSE 9000
