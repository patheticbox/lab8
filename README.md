# Lab 8: Jenkins CI/CD для Behave + Selenium

## Запуск Jenkins у Docker
    docker build -t my-jenkins .
    docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --name jenkins my-jenkins
    docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

Далі: http://localhost:8080 -> Install suggested plugins -> встановити плагін **Allure** (Manage Jenkins -> Plugins).
Manage Jenkins -> Tools -> Allure Commandline -> Add: Name `allure`, зняти "Install automatically", Home `/opt/allure-2.32.0`.

## Pipeline job
New Item -> Pipeline -> Pipeline script from SCM -> Git (URL репозиторію, гілка `*/main`) -> Script Path `Jenkinsfile` -> Save -> Build Now.

## Локальний запуск
    pip install -r requirements.txt
    behave
    python -m pylint --disable=C,R features pages
