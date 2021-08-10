#!/usr/bin/python3

import logging as log
import os

# Check to see if the environment variable requested exists
def get_env_var(env_prefix, env_arg):
	src_path = os.getenv(f"{env_prefix}{env_arg}")
	return src_path