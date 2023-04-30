#!/bin/bash

# Prompt user for environment variable value
read -p "Enter value for OPENAI_API_KEY: " env_value

# Add environment variable to .bashrc file
echo "export $env_var=$env_value" >> ~/.bashrc

# Reload .bashrc file
source ~/.bashrc

# Print message to console
echo "The $env_var environment variable has been added to ~/.bashrc with value $env_value."
