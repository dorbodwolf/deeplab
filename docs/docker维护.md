# docker用户组设置
添加名为docker的组，将deyu添加进这个组，这样做在操作docker时就不需要sudo了

# docker设置随系统启动
大多数linux发行版使用systemd管理服务随系统boot而启动的权限，Ubuntu18也不例外  
`deyu@AIStation:~$ sudo systemctl enable docker`  
`deyu@AIStation:~$ sudo systemctl restart docker`


# docker存储迁移
docker默认安装在系统盘上，由于系统盘存储空间有限，长远看很难满足docker存储的需要，所以需要迁移到8T廉价盘上。

## 挂载8T廉价盘
参考 https://blog.csdn.net/ybdesire/article/details/79145180  
`sudo mount -t ext4 /dev/sdb1 /HNCGDATA/`

## 将docker存储迁移到廉价盘


# 将容器打包成docker镜像
首先要明白容器中生成的writable container layer与镜像初始layer的关系  
![不同容器有各自的可写容器层](https://docs.docker.com/storage/storagedriver/images/sharing-layers.jpg])  
