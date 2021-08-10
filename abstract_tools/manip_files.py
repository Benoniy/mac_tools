#!/usr/bin/python3

import logging as log
import os
import shutil

# Delete a folder / file
def del_dir(path):
	if os.path.isdir(path):
		log.info(f"Deleting destination directory: {path}")
		shutil.rmtree(path)
	
	if os.path.isfile(path):
		log.info(f"Deleting malformed destination file: {path}")
		os.remove(path)


# Generates the env_details file that I use for integration with p10k
def gen_details(path, name):
	log.info(f"Generating .env_details file: {path}/.env_details")
	f = open(path + "/.env_details", "w")
	f.write(f'CHNG_PROJ_ENV_NAME="{name}"')
	f.close()


# Check if a folder exists, if not return 'None'
def get_folder(path, folder_name):
	src_path = path + '/' + folder_name
	if os.path.exists(src_path):
		return src_path
	return "None"

