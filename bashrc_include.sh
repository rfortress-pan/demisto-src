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
