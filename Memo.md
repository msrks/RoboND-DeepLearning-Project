## Work on AWS

```
$ ssh -i "config/riki-aws-gpu.pem" ubuntu@<hogehoge>.amazonaws.com
$ jupyter notebook --ip='*' --port=8888 --no-browser
```

## Get Training Data by download

```
#train
$ wget https://s3-us-west-1.amazonaws.com/udacity-robotics/Deep+Learning+Data/Lab/train.zip
#valid
$ wget https://s3-us-west-1.amazonaws.com/udacity-robotics/Deep+Learning+Data/Lab/validation.zip
#train
$ wget https://s3-us-west-1.amazonaws.com/udacity-robotics/Deep+Learning+Data/Project/sample_evaluation_data.zip
```

## Record Training Data in Simulator

```
$ cd code
$ python preprocess_ims.py
$ cp -r processed_sim_data/train/images/ train/images/
$ cp -r processed_sim_data/train/masks/ train/masks/
```
