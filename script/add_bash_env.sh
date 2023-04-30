#!/bin/bash

echo -n "Enter value for OPENAI_API_KEY: "
read env_value

# Add environment variable to .bashrc file
echo "export OPENAI_API_KEY=$env_value" >> ~/.bashrc

# Reload .bashrc file
source ~/.bashrc

# Print message to console
echo "The OPENAI_API_KEY environment variable has been added to ~/.bashrc with value $env_value."
