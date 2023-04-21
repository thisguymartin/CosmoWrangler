#!/usr/bin/env python3

import os
import fire
import logging

from search_hound_ai.search_hound_lib import SearchHoundLib

def ValidateEnv():
    openai_api_key = os.getenv('OPENAI_API_KEY')

    if openai_api_key == '' or openai_api_key == None:
        logging.error("OPENAI_API_KEY is not set")
        exit(1)


def main():
    ValidateEnv()
    fire.Fire(SearchHoundLib, name='search-hound')

if __name__ == '__main__':
    main()