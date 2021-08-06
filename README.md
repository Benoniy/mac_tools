### What are these files?

* `change_proj <project>` - Runs `change_proj_internal` and then refreshes the shell

* `change_env` - Initiates a pyenv local <folder_name> allowing you to use venvs that use the names of your folders

* `de-quarantine <file>` - takes a file as an arg and de-quarantines it


Abstract tools:  

### change_proj_internal:

* `change_proj_internal` - A python script that changes your workspaces by creating and destroying symlinks to folders.  
* You should use `change_proj` instead because this wont work by itself with p10k


Setup:  
1. Add the following to your .zprofile to set where you will store your environments:  
   ```
   export CHNJ_PROJ_ROOT="<path to folder>"
   ```
2. If you want to specify folders outside of this root folder then you must use an environment variable in .zprofile:
   ```
   export CHNG_PROJ_<NAME>="<path to folder>"
   ```
3. The program creates a symlink from the current environment to `/usr/local/bin/chng_proj_current` so you have to add this dir to your PATH in .zprofile:
   ```
   export PATH="$PATH:/usr/local/bin/chnj_proj_current"
   ```
4. At this point you can use the script to change environments:
    * If you made a folder in the environment root folder then you use the name as an argument:
    	```
    	change_proj <folder name>
    	```
    * If you used an environment variable then you can use the <NAME> you specified:
    	```
    	change_proj <NAME>
    	```


How to add to p10k:
	
1. Add to .zprofile
	```
	source /usr/local/bin/chng_proj_current/env_details
	export CHNG_PROJ_ENV_NAME="$CHNG_PROJ_ENV_NAME"
	```
2. Add to .p10k.zsh:
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
