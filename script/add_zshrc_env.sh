#!/bin/zsh

echo -n "Enter value for OPENAI_API_KEY: "
read env_value
echo "export OPENAI_API_KEY=$env_value" >> ~/.zshrc
source ~/.zshrc
echo "The OPENAI_API_KEY environment variable has been added to ~/.zshrc with value $env_value."
