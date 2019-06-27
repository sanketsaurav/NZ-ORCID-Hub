#!/usr/bin/env bash

# Install deepsource CLI
curl https://deepsource.io/cli | bash

# Report coverage artifact to the 'test-coverage' analyzer
./bin/deepsource report --analyzer test-coverage --key python --value-file ./coverage.xml
