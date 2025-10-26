# Pull docker

* To pull python 3.12 docker image:
```
docker pull python:3.12-slim
```
Output:
```
3.12-slim: Pulling from library/python
38513bd72563: Pull complete
f2a111092025: Pull complete
d2876f169c02: Pull complete
79f2dc6dd7d8: Pull complete
Digest: sha256:e97cf9a2e84d604941d9902f00616db7466ff302af4b1c3c67fb7c522efa8ed9
Status: Downloaded newer image for python:3.12-slim
docker.io/library/python:3.12-slim
```

* Verify docker images
```
docker images
```
Output:
```
REPOSITORY   TAG         IMAGE ID       CREATED       SIZE
python       3.12-slim   e97cf9a2e84d   2 weeks ago   177MB
```

* Run container from images
```
docker run -it python:3.12-slim bash
```
It instruct to run docker from image python:3.12-slim in interactive mode and start a bash shell.
Output:
```
root@41174d65884c:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@41174d65884c:/# python
Python 3.12.12 (main, Oct 21 2025, 02:11:22) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

* Remove docker images
To remove docker images, check if a container use that images. If it available stop and remove the container first.

If we delete the image, it will show error message:
```
Error response from daemon: conflict: unable to delete python:3.12-slim (must be forced) - container 41174d65884c is using its referenced image e97cf9a2e84d
```

Show containers:
```
docker ps -a
```
Output:
```
CONTAINER ID   IMAGE              COMMAND   CREATED         STATUS         PORTS     NAMES
6a2828654e23   python:3.12-slim   "bash"    4 minutes ago   Up 4 minutes             trusting_antonelli
41174d65884c   python:3.12-slim   "bash"    9 minutes ago   Up 9 minutes             condescending_chandrasekhar
```

To stop container
```
docker stop <container id>
# or
docker stop <names>
```
Example:
```
docker stop 6a2828654e23
docker stop condescending_chandrasekhar
```

Verify with `docker ps -a`
```
CONTAINER ID   IMAGE              COMMAND   CREATED          STATUS                        PORTS     NAMES
6a2828654e23   python:3.12-slim   "bash"    11 minutes ago   Exited (137) 2 minutes ago              trusting_antonelli
41174d65884c   python:3.12-slim   "bash"    16 minutes ago   Exited (137) 13 seconds ago             condescending_chandrasekhar
```
The status is Exited.

After container stopped, delete the container:
```
docker rm <continer id>
# or
docker rm <container name>
```
Example:
```
docker rm 6a2828654e23
docker rm condescending_chandrasekhar
```

Finally delete the images:
```
docker rmi python:3.12-slim
```
Output:
```
Untagged: python:3.12-slim
Deleted: sha256:e97cf9a2e84d604941d9902f00616db7466ff302af4b1c3c67fb7c522efa8ed9
```


