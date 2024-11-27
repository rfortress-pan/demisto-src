#!/bin/bash

clear

# Check to see which version of python is installed
if command -v python3 >/dev/null 2>&1; then
    PY="python3"
elif command -v python >/dev/null 2>&1; then
    PY="python"
else
    echo "${RED}!!{$END} Neither python nor python3 is installed." >&2
    exit 1
fi

# Check to see which version of pip is installed
if command -v pip3 >/dev/null 2>&1; then
    PIP="pip3"
elif command -v pip >/dev/null 2>&1; then
    PIP="pip"
else
    echo "${RED}!!{$END} PIP is not installed. Try running ${GREEEN}pip${END} or ${GREEN}pip3${END} and it should give instructions on how to install it." >&2
    exit 1
fi

# Where the script files are located
DEV_PATH="${HOME}/.xsoar_dev"

# Name of the Python script
DEV_PY="xsoar_dev.py"

# JSON file with the site details
SITES_FILE="sites.json"

# Get the contents of the Python script
PYCMD=$(cat ${DEV_PATH}/${DEV_PY})

# Run the Python script
${PY} -c "${PYCMD}" "${DEV_PATH}" "${SITES_FILE}" $1

# The Python script creates an environment file. Source it.
source ${DEV_PATH}/xsoar_dev.env

printf "\n ${GREEN}✔${END} Using ${GREEN}${DEMISTO_DEV_NAME}${END} for demisto-sdk\n\n"
