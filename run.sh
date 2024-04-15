#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW="\033[0;33m"
NC='\033[0m'

all_successful=true

# Navigate to the script's directory
cd "$(dirname "$0")" || exit

workspace_name=$(yq e '.workspace' config.yaml)
workspace_directory="${YELLOW}${workspace_name}-workspace${NC}"

echo -e "${YELLOW}[..]${NC} Workspace directory being set up: ${workspace_directory}"

run_script() {
    script_name=$1
    echo -e "\n${YELLOW}[\]${NC} Running ${YELLOW}$script_name...${NC}"
    python3 -u "$script_name.py"

    if [ $? -eq 0 ]; then
        echo -e "${GREEN}[+]${NC} $script_name completed."
    else
        echo -e "${RED}[-]${NC} $script_name failed."
        all_successful=false
    fi
}

# Run meta setup
run_script "meta"

# Run global plugins setup
run_script "global_plugins"

# Run service plugins setup
run_script "service_plugins"

if $all_successful; then
    echo -e "\n${GREEN}[+]${NC} All plugins processed."
    echo -e "${GREEN}[+]${NC} ${workspace_directory} is created successfully."
else
    echo -e "\n${RED}[!]${NC} One or more plugins failed to process."
    echo -e "${RED}[-]${NC} ${workspace_directory} setup was not completed."
fi
