#! /bin/bash
# references:
# - https://github.com/nu11secur1ty/debian-snort-dev/blob/master/Dockerfile
# - https://gist.github.com/lukeswitz/08ea69ad6047c5f0bd2388476b2fd189
# - https://unix.stackexchange.com/questions/4186/what-is-usr-local-bin

# setup
mkdir build_snort
cd ./build_snort

# update system packages
sudo apt update -y && sudo apt upgrade -y

# required dependencies (libdaq)
git clone https://github.com/snort3/libdaq.git
cd libdaq
./bootstrap
./configure
make -j$(nproc)
sudo make install
sudo ldconfig
# sudo ln -s /usr/local/lib/libdaq.so.3 /lib/
cd ..

# other required dependencies
# TODO: build each of them from source also
# libdaq-dev
sudo apt install -y cmake \
                    gcc \
                    g++ \
                    build-essential \
                    libdumbnet-dev \
                    flex \
                    libhwloc-dev \
                    libluajit-5.1-dev \
                    luajit \
                    openssl \
                    libssl-dev \
                    libpcap-dev \
                    libpcre2-dev \
                    pkg-config \
                    zlib1g-dev

# optional dependencies
# bison, libnetfilter-queue-dev, libnghttp2-dev, autoconf, libtool
sudo apt install -y asciidoc \
                    cpputest \
                    dblatex \
                    libhyperscan-dev \
                    libunwind-dev \
                    liblzma-dev

# download snort
curl -o snort3.tar.gz -L https://api.github.com/repos/snort3/snort3/tarball/3.9.5.0

# compile and build snort
mkdir snort3
tar -xvzf snort3.tar.gz -C snort3 --strip-components=1
cd snort3
export my_path=/usr/local/snort
./configure_cmake.sh --prefix=$my_path
cd build
make -j $(nproc)
sudo make install

# check and test snort
# TODO: maybe change alias to $PATH environment variable
echo "alias snort='/usr/local/snort/bin/snort'" >> ~/.bash_aliases
. ~/.bash_aliases
snort -V

# TODO: configure snort
