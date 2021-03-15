IMG ?= mohik/crudjango
TAG ?= latest

run:
	kopf run crud_operator.py --standalone --all-namespaces

docker-build:
	docker build . -t ${IMG}:${TAG}

docker-push:
	docker push ${IMG}:${TAG}

docker: docker-build docker-push
