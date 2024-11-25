# Reference: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Variable for the OpenAPI specification path
OPENAPI_SPEC=./openapi_specification/openapi.json
OPENAPI_SPEC_URL=https://app.test.fieldmanager.io/api/location/openapi.json

# Install the required library using pipx
install:  ## Install openapi-python-client using pipx
	pipx install openapi-python-client --include-deps
	openapi-python-client --install-completion

# Install jq
install_jq:  ## Install jq command-line tool
	@which jq > /dev/null && echo "jq is already installed." || { \
	  echo "Installing jq..."; \
	  if [ "$$(uname)" = "Linux" ]; then \
	    sudo apt-get update && sudo apt-get install -y jq; \
	  elif [ "$$(uname)" = "Darwin" ]; then \
	    brew install jq; \
	  else \
	    echo "Please install jq manually."; \
	  fi \
	}

# Clear the log file
clear_log:  ## Delete the log file if it exists
	@rm -f logs/log logs/versions

# Download the OpenAPI specification
download_openapi:  ## Download the OpenAPI specification
	@echo "Downloading OpenAPI specification..."
	@curl -s $(OPENAPI_SPEC_URL) > $(OPENAPI_SPEC)

format_openapi: download_openapi  ## Format the OpenAPI specification
	@echo "Formatting OpenAPI specification..."
	@npx prettier --write $(OPENAPI_SPEC)

# Get the version from openapi.json and save to logs/versions
get_version:  ## Get the version from openapi.json and save to logs/versions
	@echo "Fetching version from $(OPENAPI_SPEC)..."
	@VERSION=$$(jq -r '.info.version' $(OPENAPI_SPEC)) && \
	echo "Field Manager Data API version: $$VERSION" > logs/versions

# Run the openapi-python-client generate command
generate: clear_log get_version  ## Generate API client from OpenAPI spec
	@echo "Generating API client..."
	openapi-python-client generate --path $(OPENAPI_SPEC) --overwrite --custom-template-path=templates --config config.yaml >> logs/log 2>&1
	openapi-python-client --version >> logs/versions 2>&1

# A shortcut to install dependencies and then generate the client
all: install install_jq generate  ## Install dependencies and generate client
