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


`sudo docker run -it  --rm --name 'deeplab' -u 1001 -v /home/deyu/tianchi_buildings:/data  --gpus all tensorflow/tensorflow:1.14.0-gpu-py3-jupyter`

# 测试GPU可用性
```
import tensorflow as tf
print('GPU',tf.test.is_gpu_available())
```

# 更新阿里apt镜像安装vim，gdal
vim /etc/apt/sources.list
参考https://blog.csdn.net/f156207495/article/details/88563632
apt update
apt install vim
apt install gdal-bin python-gdal python3-gdal libgdal-dev

# datasets数据更新
./clip_train.sh lanzhou_img_RGB.tif lzimage/
./clip_train.sh lanzhou_building_footprints.tif lzlabel/

ls *.png|cut -d. -f1>../all.txt
python split_all.py 1168 80 数据切分代码

# 生成tfrecord数据集
python /data/models-master/research/deeplab/datasets/build_voc2012_data.py \
  --image_folder="/data/datasets/lzimage" \
  --semantic_segmentation_folder="/data/datasets/lzlabel" \
  --list_folder="/data/datasets/lzindex/" \
  --image_format="png" \
  --output_dir="/data/datasets/lztfrecord"

# 模型训练
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

python /data/models-master/research/deeplab/train.py \
  --logtostderr \
  --num_clones=1 \
  --training_number_of_steps=5000 \
  --train_split="train" \
  --model_variant="xception_71" \
  --atrous_rates=4 \
  --atrous_rates=12 \
  --atrous_rates=18 \
  --output_stride=16 \
  --decoder_output_stride=4 \
  --train_crop_size="512,512" \
  --train_batch_size=1 \
  --dataset="mydata" \
  --initialize_last_layer=False \
  --last_layers_contain_logits_only=True \
  --fine_tune_batch_norm=False \
  --tf_initial_checkpoint='/data/models-master/research/deeplab/backbone/train_fine/model.ckpt' \
  --train_logdir='/data/models-master/research/deeplab/exp/mydata_train/lztrain/' \
  --dataset_dir='/data/datasets/lztfrecord'
