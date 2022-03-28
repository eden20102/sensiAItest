![Sensi Logo and Tagline](https://user-images.githubusercontent.com/44435512/160245386-7acfec1f-bb12-400a-b8d6-71d81b46ace4.png)



#How folders are built
  
  #1-In the CSV folder is the first question in Python
  
  
  #2-In the docker folder is the second question (Dockerizing as Service) including the executable file
  
  
  #3-The Answers folder contains the answers to question No. 3, including the amendment


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






![aws-ecs-fargate](https://user-images.githubusercontent.com/44435512/160479042-9145506b-81d2-4b9c-b090-05d8e4970097.png)

#bonus question#
```
  1) git clone for project
  2) Install terraform (sudo apt install terraform)
  3) Enter the AWS Access Key ID AND secret Key Into a folder ["$HOME/.aws/credentials"] OR By command   "aws configure"
  4) Enter command terraform init
  5) Enter command terraform apply
```
