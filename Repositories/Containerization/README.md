# Containers vs. Virtual Machines

![image](images/vs_container.png)


## Benefits of using Containers versus VMs
There are several benefits of using Containers over VMs:

- Size: Containers are much smaller than Virtual Machines (VM) and run as isolated processes versus virtualized hardware. VMs can be in GBs while containers are in MBs.
- Speed: Virtual Machines can be slow to boot and take minutes to launch. A container can spawn much more quickly typically in seconds.
- Composability: Containers are designed to be programmatically built and are defined as source code. Virtual Machines are often replicas of a conventional computer system.

![image](images/deployment.png)


## What is Docker?
- Docker is the most popular open-sourced container runtime tool that helps to build, test, and run containers. It is both a container system and a company.

- Using Docker, you can create containers with both Linux and Windows kernels, although Windows containers are only available if you are running a Windows machine. In either case (Linux/Windows), you will have to install Docker on your local machine. **Installing Docker means installing ** Docker Desktop, a command-line utility.

### How to install Docker Desktop?
Installing Docker means installing Docker Desktop, a command-line utility. There are installers available for all the major operating systems: Linux, OSX, and Windows. You can find installers at either of the below links which are part of the official Docker documentation:

- [Get Docker](https://docs.docker.com/get-docker/)
- [Docker Desktop overview](https://docs.docker.com/desktop/)
- [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)

### Verify the Docker installation
You can run either of the following commands in your Mac terminal / WSL terminal:


```python

# to check the version
docker version
# to verify that Docker can pull and run images (we will talk more about images next)
docker run hello-world 
```

### Optional - Create a container to learn more about Docker
You can try the following command that will fetch an image and then create and run a container.

docker run -d -p 80:80 docker/getting-started
We will learn more in detail about the command above, but for now, it fetches an image docker/getting-started and creates and runs a container. You can access this container using http://localhost:80 in your browser. See a snapshot below:

![image](images/snap17.png)


# References
