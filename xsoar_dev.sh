#!/bin/bash

###
# This is a set of scripts to help with switching between XSOAR development instances.
# 
# The files should be saved to your ~/.xsoar_dev folder and your .bashrc or .zshrc file
# 	updated with the commands in the comments directly below this.
# 
# These scripts only require Python 3.x and pip to be installed. The Python script will
#   install any additional libraries required automatically.
# 
# If you have any questions or need assistance with installation/configuration please
# 	reach out to Ryan Fortress (rfortress@paloaltonetworks.com)
###


###
# Save the commands below to your ~/.bashrc (Linux) or ~/.zshrc (MacOS) and use `demisto-src`
# 	to run the script.
### 

# alias demisto-src="source ~/.xsoar_dev/xsoar_dev.sh"

# GREEN='\033[0;32m'
# END='\033[0m'

## If DEMISTO_BASE_URL isn't set, let the user know. Otherwise output the URL that is defined.
# if [ -z "$DEMIST_BASE_URL" ]
# then
#       printf "\n\nNo demisto-sdk enviroment is defined. Use ${GREEN}demisto-src${END} to select an environment.\n\n"
# else
#       printf "\n\nUsing ${GREEN}${DEMISTO_BASE_URL}${END} for demisto-sdk\n\n"
# fi

###
# End .bashrc or .zshrc section.
###


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