FROM alpine:3.11

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="juniper-automation-examples"
LABEL maintainer="packetferret@gmail.com"
LABEL description="automation container"
LABEL license="GPLv2"
LABEL url="https://github.com/packetferret/juniper-automation-examples"
LABEL build-date="2020827"

### -------------------------------------------------
### Install system Package
### -------------------------------------------------
RUN apk --update --no-cache add \
      ca-certificates \
      git \
      libxml2 \
      libxml2-dev \
      libxslt \
      libxslt-dev \
      openssh-client \
      openssl \
      python3\
      rsync \
      sshpass

### -------------------------------------------------
### Install additional dependencies
### -------------------------------------------------
RUN apk --update add --virtual \
        .build-deps \
        python3-dev \
        libffi-dev \
        openssl-dev \
        build-base

### -------------------------------------------------
### Upgrade pip
### -------------------------------------------------
RUN pip3 install --upgrade \
        pip \
        cffi

### -------------------------------------------------
### Change directory to /home/tmp
### -------------------------------------------------
WORKDIR /home/tmp/files

### -------------------------------------------------
### Add and install python packages
### -------------------------------------------------
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip

### -------------------------------------------------
### Install Ansible Galaxy roles
### -------------------------------------------------
RUN ansible-galaxy install juniper.junos -p /opt/app-root/src/.ansible/roles

### -------------------------------------------------
### Copy local files to container
### -------------------------------------------------
COPY jsnapy.cfg /etc/jsnapy/jsnapy.cfg

### -------------------------------------------------
### Environmentals
### -------------------------------------------------
ENV HAPPY True
ENV SHELL /usr/bin/zsh
ENV ANSIBLE_CONFIG /home/tmp/files/ansible/ansible.cfg

### -------------------------------------------------
### Cleanup work
### -------------------------------------------------
RUN apk del .build-deps 
RUN rm -rf /var/cache/apk/*