# Kivy-Build-Generator for Docker

Project created to facilitate app generation using the Kivy/KivyMD Python library.

Based on version: KivyMD 2.0.1.dev0

**The docker hub image already contains all the necessary dependencies to generate the apk. :** https://hub.docker.com/r/palominhahub/kivy-build-develop

* You must have docker installed on your machine: https://docs.docker.com/install/

* The buildozer library is already installed by default.

* The Dockerfile does not contain the Android dependencies installed by default, you need to build and install manually.

* p4a.branch = master replaced by p4a.branch = develop due to compatibility with the new version of KivyMD.

## Installation

* Clone this repository and build the image:
```bash
$ docker build -t <your-name>/kivy-build-develop .
```
```bash
$ docker build --no-cache -t <your-name>/kivy-build-develop .
```
## Usage:

**It is necessary to enter the directory of your kivy/kivyMD project to execute the commands below.**

* Command to generate buildozer.spec file:
```bash
$ docker container run --rm -it -v $PWD:/home/app/ <your-name>/kivy-build-develop python3 -m buildozer init
```

* Start a Android/debug build with:
```bash
$ docker container run --rm -it -v $PWD:/home/app/ <your-name>/kivy-build-develop python3 -m buildozer -v android debug
```

* At the end, you should have an APK or AAB file in the bin/ directory.

* Any questions about deploy or how to generate the release with buildozer, check the official documentation: https://buildozer.readthedocs.io/en/latest/index.html
## Authors

- [@palominhadev](https://github.com/palominhadev)


## Reference

 - [queirozt/buildozer](https://hub.docker.com/r/queirozt/buildozer)
 - [kivy-buildozer-docker](https://github.com/jedie/kivy-buildozer-docker/blob/master/Dockerfile)
- [buildozer’s documentation](https://buildozer.readthedocs.io/en/latest/)