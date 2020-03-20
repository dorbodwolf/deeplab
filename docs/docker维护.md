# 安装后设置
## docker用户组设置
添加名为docker的组，将deyu添加进这个组，这样做在操作docker时就不需要sudo了

## docker设置随系统启动
大多数linux发行版使用systemd管理服务随系统boot而启动的权限，Ubuntu18也不例外  
`deyu@AIStation:~$ sudo systemctl enable docker`  
`deyu@AIStation:~$ sudo systemctl restart docker`

# docker日志管理
运行`docker logs tf1.14`可以查看其日志，日志包括STOUT STERR的信息，容器启动输出的jupyter访问地址信息也可以在这里方便找到。  


# docker存储管理
## 认识docker存储驱动
docker的存储驱动（storage driver）包括aufs、overlay、overlay2等类型，服务器上默认docker存储路径的驱动类型为overlay2.  

首先要明白容器中生成的writable container layer与镜像初始layer的关系。简单说，容器中的更改只会存在于容器的生命周期，当容器删除后所有更改也会消除。  
![不同容器有各自的可写容器层](https://docs.docker.com/storage/storagedriver/images/sharing-layers.jpg)  

查看容器的size，显示的是用户更改的大小，virtual size是用户更改+image原始大小，tf1.14容器用户添加size是接近14gb，而容器挂载的文件夹的大小恰好为14gb:  
```
deyu@AIStation:~$ docker ps -s
CONTAINER ID        IMAGE                                          COMMAND                  CREATED             STATUS              PORTS               NAMES               SIZE
351f5253fd30        tensorflow/tensorflow:1.14.0-gpu-py3-jupyter   "bash -c 'source /et…"   2 days ago          Up 20 minutes       8888/tcp            tf1.14              13.7GB (virtual 17.4GB)
```
```
deyu@AIStation:~$ du -h tianchi_buildings/ --max-depth=1
5.6G	tianchi_buildings/models-master
7.2G	tianchi_buildings/datasets
4.0K	tianchi_buildings/.empty
14G	tianchi_buildings/
```
可以说layer是docker的基本存储单元。在docker存储文件夹/var/lib/docker/overlay2中，不同镜像的共用layer只存储一次。  

docker容器中layer的管理采取copy on write的策略，即用户对原有层的修改会通过copy一个该层的副本来写入内容的方式执行，而不会破坏原有的layer。  

所以数据密集型的应用不建议把数据存放在容器内，而是通过挂载存储文件夹的方式来在容器之间共享数据。  

实际上，在存储位置上容器只是存储一个索引文件，而不会重复存储layers，这和虚拟机的做法一样，启动多个容器不会增加显著的额外存储消耗。  
```
deyu@AIStation:~/deepdivedocker/cow-test$ sudo du -h /var/lib/docker/containers/ --max-depth=1
44K	/var/lib/docker/containers/351f5253fd306fe2a2f58a59aa984b62cf1d9458165aabdb1ef6e4a420822323
48K	/var/lib/docker/containers/
```

## docker存储迁移
docker默认安装在系统盘上，由于系统盘存储空间有限，长远看很难满足docker存储的需要，所以需要迁移到8T廉价盘上。

### 挂载8T廉价盘
参考 https://blog.csdn.net/ybdesire/article/details/79145180  
`sudo mount -t ext4 /dev/sdb1 /HNCGDATA/`

### 将docker存储迁移到廉价盘
查看现有docker存储占用：  
```
deyu@AIStation:~$ sudo du -h /var/lib/docker --max-depth=1
128K	/var/lib/docker/containers
4.0K	/var/lib/docker/runtimes
20K	/var/lib/docker/plugins
20K	/var/lib/docker/builder
72K	/var/lib/docker/buildkit
4.0K	/var/lib/docker/trust
52K	/var/lib/docker/network
4.0K	/var/lib/docker/tmp
4.0K	/var/lib/docker/swarm
21M	/var/lib/docker/image
28K	/var/lib/docker/volumes
47G	/var/lib/docker/overlay2
47G	/var/lib/docker
```
迁移包括修改配置文件/etc/default/docker和建立软链两种方式，这里选择了第一种  
```
# Use DOCKER_OPTS to modify the daemon startup options. 
DOCKER_OPTS="--dns 8.8.8.8 --dns 8.8.4.4 -g /HNCGDATA/docker"
```

# 将容器打包成docker镜像

# 访问docker中的web服务