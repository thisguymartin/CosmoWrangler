#!/bin/zsh

# Prompt user for environment variable value
echo -n "Enter value for OPENAI_API_KEY: "
read env_value

# Add environment variable to .zshrc file
echo "export $env_var=$env_value" >> ~/.zshrc

# Reload .zshrc file
source ~/.zshrc

# Print message to console
echo "The $env_var environment variable has been added to ~/.zshrc with value $env_value."
