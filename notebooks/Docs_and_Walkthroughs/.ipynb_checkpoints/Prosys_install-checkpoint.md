# Introduction

This is going to walk through installing Prosys OPC UA simulator. The packages
provided where rpm's so they will be installed on Fedora. The goal of this doc
is to understand the dependancies of the OPCUA simulator.

# TL;DR

Sometimes we just want move quickly. Using a fresh install of Fedora 
(In this case Fedora 26) run the following:

```
sudo yum install -y \
   /lib/ld-linux.so.2 \
   libX11.i686 \
   libXext.i686 \
   libXi.i686 \
   libXrender.i686 \
   libXtst.i686 \
   ld-linux.so.2 \ 
   libasound.so.2 \ 
   libXv.so.1 \ 
   libXss.so.1 \ 
   libQtDBus.so.4 \ 
   libQtGui.so.4
   
wget https://www.prosysopc.com/opcua/apps/JavaServer/dist/2.3.2-146/prosys-opc-ua-simulation-server-2.3.2-146.x86_64.rpm
   
sudo rmp -i prosys-opc-ua-simulation-server-2.3.2-146.x86_64.rpm
```

# Initial attempt to install

```
➜  ~ sudo rmp -i prosys-opc-ua-simulation-server-2.3.2-146.x86_64.rpm 
sudo: rmp: command not found
➜  ~ sudo rpm -i prosys-opc-ua-simulation-server-2.3.2-146.x86_64.rpm
error: Failed dependencies:
        ld-linux.so.2 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libX11.so.6 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libXext.so.6 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libXi.so.6 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libXrender.so.1 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libXtst.so.6 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libasound.so.2 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libc.so.6 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libdl.so.2 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libgcc_s.so.1 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libm.so.6 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libpthread.so.0 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
        libthread_db.so.1 is needed by prosys-opc-ua-simulation-server-2.3.2-146.x86_64
```

## Libraries Required

* ld-linux.so.2

* libX11.so.6

* libXext.so.6

* libXi.so.6

* libXrender.so.1

* libXtst.so.6

* libasound.so.2

* libc.so.6

* libdl.so.2

* libgcc_s.so.1

* libgcc_s.so.1

* libm.so.6

* libpthread.so.0

* libthread_db.so.1

## Installed the following libraries:

`yum install /lib/ld-linux.so.2`

`yum install libX11.i686`

`yum install libXext.i686`

`yum install libXi.i686`

`yum install libXrender.i686`

`yum install libXtst.i686`

This is a little heavy handed:
`yum install ld-linux.so.2 libasound.so.2 libXv.so.1 libXss.so.1 libQtDBus.so.4 libQtGui.so.4`


After all of that the installation succeeded.