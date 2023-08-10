#!/bin/bash

clear

# Where the script files are located
DEV_PATH="${HOME}/.xsoar_dev"

# Name of the Python script
DEV_PY="xsoar_dev.py"

# JSON file with the site details
SITES_FILE="sites.json"

# Get the contents of the Python script
PYCMD=$(cat ${DEV_PATH}/${DEV_PY})

# Run the Python script
python -c "${PYCMD}" "${DEV_PATH}" "${SITES_FILE}" $1

# The Python script creates an environment file. Source it.
source ${DEV_PATH}/tmp.env

# Remove the environment file.
# rm ${DEV_PATH}/tmp.env

GREEN='\033[0;32m'
END='\033[0m'

printf "Using ${GREEN}${DEMISTO_BASE_URL}${END} for demisto-sdk\n\n"