SHELL := /usr/bin/env bash
.DEFAULT_GOAL := help
.PHONY: help ansible build python shell

DOCKER_IMG = packetferret/juniper-automation
DOCKER_TAG = 0.0.1

help:
	@echo ''
	@echo 'Makefile will help us build with the following commands'
	@echo '		make ansible				places you in a shell with all of the ansible goodies'
	@echo '		make build				build the container image'
	@echo '		make python				places you in a shell with all of the python goodies'
	@echo '		make shell				places you in a shell with all of the shell goodies'

build:
	docker build -t $(DOCKER_IMG):$(DOCKER_TAG) tools/

ansible:
	docker run -it \
	--rm \
	-v $(PWD)/examples/ansible/:/home/tmp/files \
	-w /home/tmp/files/ \
	$(DOCKER_IMG):$(DOCKER_TAG) sh

python:
	docker run -it \
	--rm \
	-v $(PWD)/examples/python/:/home/tmp/files \
	-w /home/tmp/files/ \
	$(DOCKER_IMG):$(DOCKER_TAG) sh

shell:
	docker run -it \
	--rm \
	-v $(PWD)/examples/shell/:/home/tmp/files \
	-w /home/tmp/files/ \
	$(DOCKER_IMG):$(DOCKER_TAG) sh
