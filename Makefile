# Reference: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Install the required library using pipx
install:  ## Install openapi-python-client using pipx
	pipx install openapi-python-client --include-deps
	openapi-python-client --install-completion

# Clear the log file
clear_log:  ## Delete the log file if it exists
	rm -f logs/log

# Run the openapi-python-client generate command
generate: clear_log  ## Generate API client from OpenAPI spec
	openapi-python-client generate --path ./openapi_specification/openapi.json --overwrite > ./logs/log 2>&1

# A shortcut to install dependencies and then generate the client
all: install generate  ## Install dependencies and generate client
