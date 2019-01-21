Bootstrap: localimage
From: nvidia/8.0-cudnn7-devel

%runscript
    cd /home/nina/gnetree/pyca
    git checkout 9954dd5319efaa0ac5f58977e57acf004ad73ed7
    mkdir Build && cd Build
    ccmake swig..

%environment
    SREGISTRY_NVIDIA_USERNAME='$oauthtoken'
    export SREGISTRY_NVIDIA_USERNAME
    SREGISTRY_NVIDIA_TOKEN=ZDFkMTdiZ2dsM3U0bmIzMG5jYjBobWQ2Yjk6N2QwOGFlNTYtZDhhYy00Y2VjLThhMWItNGIwNGYyNmU4ZWEz
    export SREGISTRY_NVIDIA_TOKEN
    SREGISTRY_NVIDIA_BASE=nvcr.io
    export SREGISTRY_NVIDIA_BASE
    SWIG_DIR=/usr
    export SWIG_DIR
    SWIG_PATH=/usr/bin
    export SWIG_PATH
    SWIG_EXECUTABLE=/usr/bin/swig
    export SWIG_EXECUTABLE
    PATH=$PATH:$SWIG_PATH:/user/local/cuda/bin
    export PATH
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
    export LD_LIBRARY_PATH
    CUDA_HOME=/usr/local/cuda
    export CUDA_HOME
    PYTHONPATH=/home/nina/gnetree/quicksilver/code/library
    export PYTHONPATH
    LC_ALL=C
    export LC_ALL

%post
    apt-get update
    apt-get -y install git
    apt-get -y install cmake-curses-gui \
                       libboost-all-dev \
                       libfftw3-dev \
                       libghc-regex-pcre-dev \
                       libpcre3 \
                       libpcre3-dev \
                       openssh-server \
                       python2.7 \
                       python-matplotlib \
                       python-pip \
                       swig
    pip install https://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp27-cp27mu-linux_x86_64.whl
    pip install h5py scikit-image==0.14.0 matplotlib==2.2.3
