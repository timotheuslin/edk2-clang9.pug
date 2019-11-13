# ArmVirtPkg.pug
Build EDK2 packages using CLANG9/LLVM9

## Prerequisites:
1. Python 3.6.0+
2. git 2.19.0+


## Generic prerequisites for the UDK build:
1. nasm (2.0 or above)
2. iasl (version 2018xxxx or newer)
3. MSVC(Windows) or Xcode(Mac) or GCC(Open-source Posix)
4. build-essential uuid-dev (Posix)
5. pip2 install future (Python 2.7.x)
6. motc (Xcode)
7. iPug (a Python package, installed through pip)
0. Reference:
    - [Liming Gao's Guide for CLANG9 Tools Chain](https://github.com/tianocore/tianocore.github.io/wiki/CLANG9-Tools-Chain)
    - [Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting%20Started%20with%20EDK%20II) 
    - [Xcode Build](https://github.com/tianocore/tianocore.github.io/wiki/Xcode)


## Tool installation
1. Debian-Based Linux:
    - `sudo apt update`
    - `sudo apt install nasm iasl build-essential uuid-dev`
    - `pip install ipug --user`
    - `wget http://releases.llvm.org/9.0.0/clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz`
    - `tar -xvf clang+llvm-9.0.0-x86_64-linux-gnu-ubuntu-18.04.tar.xz` (under the home directory)

## Build:
1. `git clone https://github.com/timotheuslin/edk2-clang9.pug.git`
2. In the command console, change-directory to **edk2-clang9.pug**.
3. To build "OvmfPkg/OvmfPkgX64.dsc", run `./project.py` or `py project.py` or `python3 project.py`
