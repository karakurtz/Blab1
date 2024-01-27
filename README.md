https://ll1.onrender.com

## ДЛЯ ЗАПУСКУ У СЕБЕ:

1. Клонувати файли репозиторія;
```
git clone https://github.com/karakurtz/Blab1.git
```
2. Віртуальне середовища:
```
python3 -m venv venv
```
3. Активувати:
```
source ./venv/bin/activate
```
4. Скачати залежності проекта:
```
pip install -r requirements.txt
```
5. Build with Dockerfile:
```
docker build --build-arg PORT=<your port> . -t <image_name>:latest
```
6. Run with Dockerfile:
```
docker run -it --rm --network=host -e PORT=<your port> <image_name>:latest
```
7. Build with Docker_compose:
```
docker-compose build
```
8. Run with Docker_compose:
```
docker-compose up
```
