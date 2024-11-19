# Reference: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

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
	rm -f logs/log
	rm -f logs/versions

# Get the version from openapi.json
get_version:  ## Get the version from openapi.json
	@jq -r '.info.version' ./openapi_specification/openapi.json

# Run the openapi-python-client generate command
generate: clear_log  ## Generate API client from OpenAPI spec
	@echo "Generating API client..."
	@VERSION=$(make get_version) && echo Field Manager Data API VERSION:  > ./logs/versions 2>&1
	openapi-python-client --version >> ./logs/versions 2>&1
	openapi-python-client generate --path ./openapi_specification/openapi.json --overwrite > ./logs/log 2>&1

# A shortcut to install dependencies and then generate the client
all: install generate  ## Install dependencies and generate client
