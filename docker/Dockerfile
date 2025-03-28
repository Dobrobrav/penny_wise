FROM python:3.13

# these dependencies are for selenium
RUN apt update && apt install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    gnupg \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    xdg-utils \
    chromium \
    chromium-driver

COPY /conf /usr/src/conf
WORKDIR /usr/src
RUN pip install -r conf/requirements.txt -c conf/constraints.txt

COPY /docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
WORKDIR /usr/src/app
ENTRYPOINT ["/entrypoint.sh"]
