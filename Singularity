Bootstrap: docker
From: nvidia/cuda:8.0-cudnn7-devel

%setup
     cp -R /home/nina/gnetree $SINGULARITY_ROOTFS/gnetree

%environment
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64
    export LD_LIBRARY_PATH
    CUDA_HOME=/usr/local/cuda
    export CUDA_HOME
    PYTHONPATH=/root/quicksilver/code/library:/root/quicksilver/3rd_party_software/pyca/build/python_module
    export PYTHONPATH
    LC_ALL=C
    export LC_ALL

%post
    apt update
    apt -y install git
    apt -y install build-essential \
                       cmake-curses-gui \
                       libboost-all-dev \
                       libfftw3-dev \
                       libghc-regex-pcre-dev \
                       libpcre3 \
                       libpcre3-dev \
                       openssh-server \
                       python-matplotlib \
                       python-pip \
                       python2.7 \
                       swig

    # Pytorch
    pip install https://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp27-cp27mu-linux_x86_64.whl
    pip install h5py numpy==1.15.0 scikit-image==0.14.0 matplotlib==2.2.3

    # Install ITK
    cd $HOME
    wget https://sourceforge.net/projects/itk/files/itk/4.13/InsightToolkit-4.13.1.tar.gz/download
    tar -zxvf download
    cd InsightToolkit-4.13.1
    mkdir build && cd build
    cmake ..
    make -j10
    make install

    # Install pyca
    cd $HOME
    test ! -d quicksilver && git clone https://github.com/johmathe/quicksilver.git
    cd quicksilver/3rd_party_software/pyca/
    mkdir build && cd build
    cmake .. -DCMAKE_LIBRARY_PATH=/usr/local/cuda/lib64/stubs
    make -j10
    apt -y install vim
