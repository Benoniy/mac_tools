### What are these files?

* `change_proj <project>` - Runs `change_proj_internal` and then refreshes the shell

* `change_env` - Initiates a pyenv local <folder_name> allowing you to use venvs that use the names of your folders

* `de-quarantine <file>` - takes a file as an arg and de-quarantines it


Abstract tools:  

* `change_proj_internal` - A python script that changes your workspaces by creating and destroying symlinks to folders specified by environment variables.
	* Define environment variables in the format `export CHNG_PROJ_<NAME>="<path to folder>"` in .zprofile
	* If a file exist you can pass this script <NAME> and it will create a symlink
	* It symlinks to `/usr/local/bin/chng_proj_current`
	* It has p10k support:
		* Add to .zprofile
		```
		source /usr/local/bin/chng_proj_current/env_details
		export CHNG_PROJ_ENV_NAME="$CHNG_PROJ_ENV_NAME"
		```
		* Add to .p10k.zsh:
		```
		 function prompt_custom() {
    	   p10k segment -b 1 -f 3 -t "${CHNG_PROJ_ENV_NAME//\%/%%}"
  		 }

  		 function instant_prompt_custom() {
    	   prompt_custom
		 }
		 typeset -g POWERLEVEL9K_CUSTOM_FOREGROUND=233
 		 typeset -g POWERLEVEL9K_CUSTOM_BACKGROUND=1
		
		```
