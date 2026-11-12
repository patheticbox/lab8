FROM jenkins/jenkins:lts

USER root

# Python, pip, venv та утиліти
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv wget curl \
    && rm -rf /var/lib/apt/lists/*

# Google Chrome для Selenium (headless)
RUN wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update && apt-get install -y /tmp/chrome.deb \
    && rm -f /tmp/chrome.deb && rm -rf /var/lib/apt/lists/*

# Allure Commandline
ARG ALLURE_VERSION=2.32.0
RUN curl -o allure.tgz -Ls https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz \
    && tar -zxf allure.tgz -C /opt/ \
    && ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure \
    && rm -f allure.tgz

USER jenkins
