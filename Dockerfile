# =============================================================================
# SageCoders Laravel — Production image
# PHP 8.3 + Node 20 + Composer 2 + extensions Laravel
# Single-stage for simplicity (test project). For prod, consider splitting
# frontend build into a separate node stage to slim the final image.
# =============================================================================
FROM php:8.3-cli-bookworm

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        curl \
        unzip \
        libpng-dev \
        libonig-dev \
        libxml2-dev \
        libzip-dev \
        libicu-dev \
        default-mysql-client \
        ca-certificates \
        gnupg \
    && rm -rf /var/lib/apt/lists/*

# PHP extensions required by Laravel + Filament + Inertia SSR-ready
RUN docker-php-ext-install -j$(nproc) \
        pdo \
        pdo_mysql \
        mbstring \
        xml \
        zip \
        bcmath \
        gd \
        intl \
        opcache

# Composer (multi-stage copy from official image)
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Node.js 20 LTS
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/* \
    && node -v && npm -v

# OPcache config tuned for Laravel
RUN { \
        echo 'memory_consumption=128'; \
        echo 'interned_strings_buffer=16'; \
        echo 'max_accelerated_files=10000'; \
        echo 'revalidate_freq=2'; \
        echo 'opcache_fast_shutdown=1'; \
        echo 'opcache_enable=1'; \
        echo 'opcache_enable_cli=0'; \
    } > /usr/local/etc/php/conf.d/opcache.ini

# Working dir
WORKDIR /var/www/html

# ----- Layer caching: deps first, code after -----
COPY composer.json composer.lock ./
RUN composer install \
        --no-dev \
        --no-scripts \
        --no-autoloader \
        --no-interaction \
        --prefer-dist

COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund

# ----- App code -----
COPY . .

RUN composer dump-autoload --optimize --no-dev \
    && npm run build \
    && php artisan package:discover --ansi || true

# Laravel dirs need to be writable
RUN mkdir -p storage/framework/{cache,sessions,views} storage/logs bootstrap/cache \
    && chown -R www-data:www-data storage bootstrap/cache \
    && chmod -R 775 storage bootstrap/cache

EXPOSE 8000

# Entrypoint: run migrations then serve
CMD ["sh", "-c", "php artisan migrate --force --no-interaction && php artisan config:cache && php artisan route:cache && php artisan view:cache && php artisan serve --host=0.0.0.0 --port=8000"]
