# 安装docker
以及nvidia-docker toolkits

# 修改docker国内源
在阿里云开放云原生平台找到对应系统
您可以通过修改daemon配置文件/etc/docker/daemon.json来使用加速器
```
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://gcz02461.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

# 拉取tf 1.14 GPU版本的docker官方镜像
`deyu@AIStation:/home/hncg$ sudo docker pull tensorflow/tensorflow:1.14.0-gpu-py3-jupyter`

# 创建镜像

WARNING: You are running this container as root, which can cause new files in
mounted volumes to be created as the root user on your host machine.

To avoid this, run the container by specifying your user's userid:

`$ docker run -u $(id -u):$(id -g) args...`


`sudo docker run -it  --rm --name 'tf1.14' -u 1001  -v /home/deyu/tianchi_buildings:/data  --gpus all tensorflow/tensorflow:1.14.0-gpu-py3-jupyter`

# 测试GPU可用性
```
import tensorflow as tf
print('GPU',tf.test.is_gpu_available())
```