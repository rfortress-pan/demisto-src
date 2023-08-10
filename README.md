This is a collection of scripts to facilitate quickly switching between multiple XSOAR development environments. It supports XSOAR 6 and XSOAR 8.  

## Requirements

- Linux / MacOS
 - Python 3
 - Pip

## Configuration

1. Save the scripts to your `~/.xsoar_dev` folder
		
		git pull https://github.com/rfortress-pan/demisto-src.git ~/.xsoar_dev

2. Add the following commands to your `~/.bashrc` (Linux) or `~/.zshrc` (MacOS) files

		alias demisto-src="source ~/.xsoar_dev/xsoar_dev.sh"

		export GREEN='\033[0;32m'
		export RED='\033[0;31m'
		export END='\033[0m'

		FILE=~/.xsoar_dev/xsoar_dev.env
		if test -f "$FILE"
		then
		    source $FILE
		fi

		if [ -z "$DEMISTO_BASE_URL" ]
		then
		      printf "\n ${RED}！${END}No demisto-sdk enviroment is defined. Use ${GREEN}demisto-src${END} to select an environment.\n\n"
		else
		      printf "\n ${GREEN}✔${END} Using ${GREEN}${DEMISTO_DEV_NAME}${END} for demisto-sdk\n\n"
		fi

3. Load the commands (only required the first time you install).

		# For linux
		source ~/.bashrc

		# For MacOS
		source ~/.zshrc

4. Add a new XSOAR development environment

		demisto-src add

5. Remove the sample development environment (`rem`, `remove`, `del`, or `delete`)

		demist-src rem

6. Select your development environment

		demisto-src

7. Get the details of the currently selected development environment (`info`, `det` or `details`)

		demisto-src info