PROJECT_NAME ?= text_analyzer
VERSION = $(shell python3 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= alksglk
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)


.PHONY: setup-venv setup clean-pyc clean-test test mypy lint docs check

all:
	@echo "make devenv		- Create & setup development virtual environment"
	@echo "make checks		- Run tests and Check code with pylint and mypy"
	@echo "make lint		- Check code with pylint"
	@echo "make mypy		- Check code with mypy"
	@echo "make clean		- Remove files created by distutils"
	@echo "make test		- Run tests"
	@echo "make sdist		- Make source distribution"
	@echo "make docker		- Build a docker image"
	@echo "make upload		- Upload docker image to the registry"
	@exit 0



devenv: clean
	rm -rf env
	python3.9 -m venv env
	env/bin/pip install -U pip
	env/bin/pip install -Ue '.[dev]'

setup:
	DOCKER_BUILDKIT=1 docker build -t dev -f Dockerfile .

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*
	find . -name '.pytest_cache' -exec rm -fr {} +

clean: clean-pyc clean-test
	find . -name '.my_cache' -exec rm -fr {} +
	rm -rf logs/

test: clean
	. env/bin/activate && pytest tests --cov=text_analyzer --cov-report=term-missing --cov-fail-under 85

mypy:
	. env/bin/activate && mypy text_analyzer

lint:
	. env/bin/activate && pylint text_analyzer -j 4 --reports=y

checks: test lint mypy clean

sdist: clean
	python3 setup.py sdist

docker: sdist
	docker build --target=api -t $(PROJECT_NAME):$(VERSION) .

upload: docker
	docker tag $(PROJECT_NAME):$(VERSION) $(REGISTRY_IMAGE):$(VERSION)
	docker tag $(PROJECT_NAME):$(VERSION) $(REGISTRY_IMAGE):latest
	docker push $(REGISTRY_IMAGE):$(VERSION)
	docker push $(REGISTRY_IMAGE):latest
