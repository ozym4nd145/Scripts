sudo -E apt-get update
sudo -E apt-get upgrade
sudo apt-get remove x264 libx264-dev

sudo -E apt-get install build-essential checkinstall cmake pkg-config yasm gfortran git
sudo -E apt-get install libjpeg8-dev libjasper-dev libpng12-dev
# If you are using Ubuntu 14.04
sudo -E apt-get install libtiff4-dev
# If you are using Ubuntu 16.04
# sudo apt-get install libtiff5-dev
sudo -E apt-get install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
sudo -E apt-get install libxine2-dev libv4l-dev
sudo -E apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo -E apt-get install libqt4-dev libgtk2.0-dev libtbb-dev
sudo -E apt-get install libatlas-base-dev
sudo -E apt-get install libfaac-dev libmp3lame-dev libtheora-dev
sudo -E apt-get install libvorbis-dev libxvidcore-dev
sudo -E apt-get install libopencore-amrnb-dev libopencore-amrwb-dev
sudo -E apt-get install x264 v4l-utils

## Optional
sudo -E apt-get install libprotobuf-dev protobuf-compiler
sudo -E apt-get install libgoogle-glog-dev libgflags-dev
sudo -E apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

#Install python libs
sudo -E apt-get install python-dev python-pip python3-dev python3-pip
sudo -E -H pip2 install -U pip numpy
sudo -E -H pip3 install -U pip numpy

git clone https://github.com/opencv/opencv.git
cd opencv 
git checkout 2b44c0b6493726c465152e1db82cd8e65944d0db 
cd ..

git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout abf44fcccfe2f281b7442dac243e37b7f436d961
cd ..

cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D WITH_TBB=ON \
      -D WITH_V4L=ON \
      -D WITH_QT=ON \
      -D WITH_OPENGL=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..

# find out number of CPU cores in your machine
nproc
# substitute 4 by output of nproc
make -j4
sudo make install
sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig


