# Customize docker image

Let's say, we want to run fastapi application inside docker and expose the api port to accessible from another pc.

This is file helloworld.py
```
from fastapi import FastAPI
import uvicorn

@app.get("/hello")
def hello()
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
```

* Create file requirements.txt, this file contains which python lib should be installed.
```
fastapi
uvicorn
```

* Create docker file dockerfile
```
# use base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /testapi

# Copy dependency list
COPY requirements.txt 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI code
COPY helloworld.py .

# Expose FastAPI port
EXPOSE 9000

# Command to run helloworld.py
CMD ["python", "helloworld.py"]

```

* Build the image
```
docker build -t helloworld-app .
```
Output:
```
[+] Building 12.6s (10/10) FINISHED                                               docker:desktop-linux
 => [internal] load build definition from dockerfile                                              0.0s
 => => transferring dockerfile: 428B                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                               0.1s
 => [internal] load .dockerignore                                                                 0.0s
 => => transferring context: 2B                                                                   0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:e97cf9a2e84d604941d9902f00616db7466ff30  0.2s
 => => resolve docker.io/library/python:3.12-slim@sha256:e97cf9a2e84d604941d9902f00616db7466ff30  0.1s
 => [internal] load build context                                                                 0.1s
 => => transferring context: 290B                                                                 0.0s
 => [2/5] WORKDIR /testapi                                                                        0.1s
 => [3/5] COPY requirements.txt .                                                                 0.1s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                      9.1s
 => [5/5] COPY helloworld.py .                                                                    0.1s
 => exporting to image                                                                            2.9s
 => => exporting layers                                                                           1.7s
 => => exporting manifest sha256:988d2de5bb964b6f038d2debe57d22a184ce8f8129852e69e263f578d9be231  0.0s
 => => exporting config sha256:9e7c8a68f65022a517f8f1fbbc1f5c3e1f621ec44791277286f72bd000ec1f16   0.0s
 => => exporting attestation manifest sha256:203559eb6b8174c4edba6c3cecee57566df2898a22b73d23ee8  0.0s
 => => exporting manifest list sha256:5d4d6a3e4c6c59b0cba6054f35038ba5faabd49a36e10bbff117b4b4a2  0.0s
 => => naming to docker.io/library/helloworld-app:latest                                          0.0s
 => => unpacking to docker.io/library/helloworld-app:latest                                       0.9s
```

* Verify the image is in our docker repositories:
```
docker images
```
Output:
```
REPOSITORY       TAG         IMAGE ID       CREATED              SIZE
helloworld-app   latest      5d4d6a3e4c6c   About a minute ago   212MB
python           3.12-slim   e97cf9a2e84d   2 weeks ago          177MB
```

* Run docker image
```
docker run -d -p 9000:9000 helloworld-app
```
Port setting 9000:9000 means internal docker port is 9000 and mapped to port 9000 on host. 
```
-p <host_port>:<container_port>
```
The first section is host port and second section is container port.
Example, if container port is 9000 and we want host port using 9100, it become 9100:9000

Verify the container is running:
```
docker ps
```
Output:
```
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                         NAMES
af3e839917ca   helloworld-app   "python helloworld.py"   2 minutes ago   Up 2 minutes   0.0.0.0:9000->9000/tcp, [::]:9000->9000/tcp   unruffled_saha
```

Call from browser http://localhost:9000/hello

