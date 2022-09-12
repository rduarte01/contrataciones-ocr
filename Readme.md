
docker build -t ocr-contrataciones .
docker run -v `pwd`/files:/app/files ocr-contrataciones

docker system prune -a