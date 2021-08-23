VERSION = $$(git rev-parse HEAD)
NS = [DOCKER_REGISTRY]/[PROJECT-ID]
REPO = prod-{{cookiecutter.project_name}}

.PHONY: build-prod push-prod

build-prod:
	@docker build . -f ./docker/FalconDockerfile -t $(NS)/$(REPO):$(VERSION)
	@echo 'Tag built' $(NS)/$(REPO):$(VERSION)
	@echo "Don't forget to tag a numeric version"
	@echo '$$ docker tag '$(NS)/$(REPO):$(VERSION) $(NS)/$(REPO)':'

push-prod:
	@docker -- push $(NS)/$(REPO):$(VERSION)
	@echo 'Tag pushed' $(VERSION)
