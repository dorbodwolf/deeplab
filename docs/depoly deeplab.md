# Deeplab V3+

## 1.	深度学习环境部署完成
数据增强
https://blog.csdn.net/qq_29133371/article/details/54927266

## 2.	Convert to tfrecord
制作tfrecord之前，需要有指引文件将数据集分类成训练/测试/验证集。  
制作指引文件，需要将之前生成的原始图片和灰度图分别放在两个文件夹下：`/volumes/massdata2/tianchi/dataset/lzimage和/volumes/massdata2/tianchi/dataset/lzlable`，两个文件夹下的文件是一一对应的，文件名相同。并在文件夹`/volumes/massdata2/tianchi/dataset/lzindex/`下创建3个txt文件：  
*	train.txt：所有训练集的文件名  
*	trainval.txt：所有验证集的文件名  
*	val.txt：所有测试集的文件名  
*   split_val_train.sh: 划分训练集和验证集  
然后利用build_voc2012_data.py转换成tfrecord格式，cmd输入指令：  

```
python ./build_voc2012_data.py \
  --image_folder="/volumes/massdata2/tianchi/dataset/lzimage" \
  --semantic_segmentation_folder="/volumes/massdata2/tianchi/dataset/lzlable" \
  --list_folder="/volumes/massdata2/tianchi/dataset/ lzindex /" \
  --image_format="jpg" \
  --output_dir="/volumes/massdata2/tianchi/dataset /lztfrecord"
```

## 3.	模型训练

```
python /volumes/massdata2/tianchi/models/research/deeplab/train.py \     --logtostderr \     --num_clones=1 \     --training_number_of_steps=5000 \     --train_split="train" \     --model_variant="xception_71" \     --atrous_rates=4 \     --atrous_rates=12 \     --atrous_rates=18 \     --output_stride=16 \     --decoder_output_stride=4 \     --train_crop_size="513,513" \     --train_batch_size=1 \     --dataset="mydata" \     --initialize_last_layer=False \     --last_layers_contain_logits_only=True \     --fine_tune_batch_norm=False \     --tf_initial_checkpoint='/volumes/massdata2/tianchi/models/research/deeplab/backbone/train_fine/model.ckpt' \     --train_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \     --dataset_dir='/volumes/massdata2/tianchi/datasets/rtfrecord'
```

## 4.	模型预测

```
python /volumes/massdata2/tianchi/models/research/deeplab/predict.py ${folder}/${fname}_${ox}_${oy}.tif ${folder}/；
```

