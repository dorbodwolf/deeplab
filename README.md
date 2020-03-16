# deeplab

## the scripts

```
python /volumes/massdata2/tianchi/models/research/deeplab/train.py \
    --logtostderr \
    --num_clones=1 \
    --training_number_of_steps=5000 \
    --train_split="train" \
    --model_variant="xception_71" \
    --atrous_rates=4 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --train_crop_size="513,513" \
    --train_batch_size=1 \
    --dataset="mydata" \
    --initialize_last_layer=False \
    --last_layers_contain_logits_only=True \
    --fine_tune_batch_norm=False \
    --tf_initial_checkpoint='/volumes/massdata2/tianchi/models/research/deeplab/backbone/train_fine/model.ckpt' \
    --train_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/rtfrecord'


python vis.py \
    --logtostderr \
    --vis_split="val" \
    --model_variant="xception_71" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --vis_crop_size="513,513" \
    --dataset="mydata" \
    --colormap_type="pascal" \
    --checkpoint_dir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --vis_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/vis/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/tfrecord/'



python /volumes/massdata2/tianchi/models/research/deeplab/eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_71" \
    --atrous_rates=6 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --vis_crop_size="513,513" \
    --dataset="mydata" \
    --checkpoint_dir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --eval_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/eval/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/rtfrecord/'


python /volumes/massdata2/tianchi/models/research/deeplab/export_model.py \
  --logtostderr \
  --checkpoint_path="/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/model.ckpt-5000" \
  --export_path="/volumes/massdata2/tianchi/datasets/" \
  --model_variant="xception_71" \
  --num_classes=2 \
  --crop_size=513 \
  --crop_size=513 \
  --inference_scales=1.0
     -------------------------------------------------------------------------

python /volumes/massdata2/tianchi/models/research/deeplab/train.py \
    --logtostderr \
    --num_clones=1 \
    --training_number_of_steps=20000 \
    --train_split="train" \
    --model_variant="mobilenet_v2" \
    --train_batch_size=2 \
    --dataset="mydata" \
    --train_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/tfrecord'



python /volumes/massdata2/tianchi/models/research/deeplab/train.py \
    --logtostderr \
    --num_clones=1 \
    --training_number_of_steps=10000 \
    --train_split="train" \
    --model_variant="mobilenet_v2" \
    --decoder_output_stride=4 \
    --train_crop_size="128,128" \
    --train_batch_size=4 \
    --dataset="mydata" \
    --fine_tune_batch_norm=False \
    --train_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/rtfrecord'


     -----------------------------
++++++++++++++++++++++++++++
python /volumes/massdata2/tianchi/models/research/deeplab/train.py \
    --logtostderr \
    --num_clones=1 \
    --training_number_of_steps=10000 \
    --train_split="train" \
    --model_variant="xception_71" \
    --atrous_rates=4 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --train_crop_size="321,321" \
    --train_batch_size=2 \
    --dataset="mydata" \
    --train_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/tfrecord'
     -----------------------------------------------------------------------


python /volumes/massdata2/tianchi/models/research/deeplab/train.py \
    --logtostderr \
    --num_clones=1 \
    --training_number_of_steps=20000 \
    --train_split="train" \
    --model_variant="mobilenet_v2" \
    --train_crop_size="256,256" \
    --train_batch_size=1 \
    --dataset="mydata" \
    --initialize_last_layer=False \
    --last_layers_contain_logits_only=True \
    --fine_tune_batch_norm=False \
    --tf_initial_checkpoint='/volumes/massdata2/tianchi/models/research/deeplab/backbone/deeplabv3_mnv2_cityscapes_train/model.ckpt'\
    --train_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/rtfrecord'


python /volumes/massdata2/tianchi/models/research/deeplab/eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="mobilenet_v2" \
    --eval_crop_size="256,256" \
    --dataset="mydata" \
    --initialize_last_layer=False \
    --last_layers_contain_logits_only=True \
    --fine_tune_batch_norm=False \
    --checkpoint_dir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --eval_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/eval/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/rtfrecord/'
```


号伟
```
python /volumes/massdata2/tianchi/models/research/deeplab/export_model.py
  --logtostderr
  --checkpoint_path="/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/model.ckpt-5000" \  
  --atrous_rates=4 \
  --atrous_rates=12 \
  --atrous_rates=18 \
  --output_stride=16 \
  --decoder_output_stride=4 \
  --export_path="/volumes/massdata2/tianchi/datasets/"
  --model_variant="xception_71"
  --num_classes=2
  --crop_size=513
  --crop_size=513 \ 
  --initialize_last_layer=False \
  --last_layers_contain_logits_only=True \
  --fine_tune_batch_norm=False \  
  --inference_scales=1.0
```


```
python /volumes/massdata2/tianchi/models/research/deeplab/train.py \
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
    --train_crop_size="513,513" \
    --train_batch_size=1 \
    --dataset="mydata" \
    --initialize_last_layer=False \
    --last_layers_contain_logits_only=True \
    --fine_tune_batch_norm=False \
    --tf_initial_checkpoint='/volumes/massdata2/tianchi/models/research/deeplab/backbone/train_fine/model.ckpt' \
    --train_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/lztfrecord'
```


```
python /volumes/massdata2/tianchi/models/research/deeplab/eval.py \
    --logtostderr \
    --eval_split="val" \
    --model_variant="xception_71" \
    --atrous_rates=4 \
    --atrous_rates=12 \
    --atrous_rates=18 \
    --output_stride=16 \
    --decoder_output_stride=4 \
    --eval_crop_size="512,512" \
    --dataset="mydata" \
    --initialize_last_layer=False \
    --last_layers_contain_logits_only=True \
    --checkpoint_dir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/train/' \
    --eval_logdir='/volumes/massdata2/tianchi/models/research/deeplab/exp/mydata_train/eval/' \
    --dataset_dir='/volumes/massdata2/tianchi/datasets/lztfrecord'
```