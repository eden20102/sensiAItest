# how to run app
```
pip install -r requirements.txt
python3 main.py
```

# How to run docker image

1. Install docker https://docs.docker.com/engine/install/
2. Build the image and run it
```
cd docker/
docker build -t app .
docker run app
```