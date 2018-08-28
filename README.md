本项目是tensorflow word2vec示例程序。

第一步 执行安装相关环境和数据下载的脚本  
$sh setup.sh  

第二步 确保数据下载之后，执行word2vec.py  
$python word2vec.py

程序执行过程中可以使用tensorboard可视化相关参数变化，执行下列命令  
$ tensorboard --logdir ./log/  
上面命令必须在程序主目录中执行，因为tensorboard指定的是相对路径。然后在浏览器中输入tensorboard提示的url。一般为http://localhost:6006
