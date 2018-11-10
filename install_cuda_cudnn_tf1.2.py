#coding:utf-8

'''
本脚本是提供ubuntu18.4系统搭建深度学习tensorflow_gpu-1.12环境
版本配套关系
1，nvidia驱动384
2，cuda 9.1
3, cudnn 7.1.3
4, tensorflow_gpu 1.12
5, numpy 1.13.0

'''


import os

def PreInstall():

    os.system("sudo apt-get install -y python-pip")
    os.system("sudo apt-get install -y git")
    os.system("sudo apt-get install -y wget")
    os.system("sudo pip install bdist_wheel")
    os.system("sudo pip install setuptools")
    os.system("sudo pip install easydict protobuf pydot")
    os.system("sudo apt-get install -y graphviz libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler libopenblas-dev liblapack-dev libatlas-base-dev libgflags-dev libgoogle-glog-dev liblmdb-dev python-tk python-numpy python-scipy python-matplotlib python-sklearn python-skimage python-h5py python-protobuf python-leveldb python-networkx python-nose python-pandas python-gflags")
    os.system("sudo apt-get install -y --no-install-recommends libboost-all-dev")

def InstallDriver():

    os.system("sudo add-apt-repository ppa:xorg-edgers/ppa")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y nvidia-384")



    pass



if __name__=="__main__":
    pass
