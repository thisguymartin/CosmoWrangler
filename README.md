# SearchHoundAI  🐕 

A CLI for GPT with a focus on simplicity and ease of use. For developer just wanting to use gpt in there command line.

PIP Package: [Search Hound AI](https://pypi.org/project/search-hound-ai/)

## Installation

Install the CLI globally using pip: 

```bash
pip install search-hound-ai
```

## Usage

The CLI provides several commands for different purposes:

### Chat with GPT

Start a conversation with pip:

```bash
hound
```

Need assistance run:

```bash
hound --help
```

To use hound command:

```bash
hound [search string]
```

### Ask GPT

Ask GPT a question about a specific file:

```bash
hound [...your question here]
```

Example:

```bash
hound "How to purge docker container and images?"
```

## Setting Environment Variables

Required Environment Variable:

* OPENAI_API_KEY

Run the following scripts to if you are using .zshrc

```bash
echo -n "Enter value for OPENAI_API_KEY: "
read env_value
echo "export OPENAI_API_KEY=$env_value" >> ~/.zshrc
source ~/.zshrc
echo "The OPENAI_API_KEY environment variable has been added to ~/.zshrc with value $env_value."

```

or bash

```bash
echo -n "Enter value for OPENAI_API_KEY: "
read env_value
echo "export OPENAI_API_KEY=$env_value" >> ~/.bashrc
source ~/.bashrc
echo "The OPENAI_API_KEY environment variable has been added to ~/.bashrc with value $env_value."
```

## Contributions

Contributions to the SearchHoundAI CLI tool are welcome and encouraged. Please refer to the repository's [CONTRIBUTING.md](http://contributing.md/) file for more information on how to contribute.
