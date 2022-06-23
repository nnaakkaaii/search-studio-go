.PHONY: gen-api
gen-api:
	go install github.com/deepmap/oapi-codegen/cmd/oapi-codegen@v1.11.0
	oapi-codegen --config config/oapi-codegen/server.yaml ./spec/openapi.yaml
