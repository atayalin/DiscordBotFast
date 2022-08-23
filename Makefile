SHELL := /bin/bash

install: requirements.in
	python3 -m venv venv
	./venv/bin/pip install -r requirements.in

uninstall: venv
	rm -rf venv
	
run:
	./venv/bin/python3 main.py

build: venv
	./venv/bin/pip install -r requirements.in
	./venv/bin/python3 app.py	
