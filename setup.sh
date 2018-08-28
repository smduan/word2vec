#!/bin/sh

cd ./data
#下载训练数据，若是wget下载较慢可以前往下面url自行下载。
#然后将数据放在data目录下
wget http://mattmahoney.net/dc/text8.zip

pip install tensorflow
pip install numpy
