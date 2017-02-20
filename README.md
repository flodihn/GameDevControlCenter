# GameDevControlCenter
A web and latex based control center for managing game development.

# Setup
Clone this repository wherever you like, for example:

    /home/<user>/GameDevControlCenter

## gdd_conf.py
Configure the gdd_conf.py so it can find the paths to your client and server source repositories, if there is no seperate server repository, just use the client and leave the SERVER_SOURCE_DIR variable empty.
Note that the path to the location of the GDD must be specified:

- GDD_DIR - Path to the git repository wher the GDD is located.
- GDD_FILE - This is the main latex file, without the .tex extension. If not latex is used, any text format would work as long as the they contain the right markups.

## web_conf.py
Configure to fit your project:
- GAME_NAME - Name of your game (duh)
- GDD_LINK - The location of the generated GDD in pdf format. HINT: The gdd_to_pdf.py scripts generates this file.
- PROJECT STAGE - Set this to either PROTOTYPE, ALPHA, BETA or RELEASED depending what status your project is currenlty in.
- HOOK_PASSWD - Should have been used for using git web hooks, but never got around to implemented it.

## Markup
- \feature{My Feature} - Use this in the GDD to markup existing features.
- \ImplementedFeature{My Feature} - Use this in the the source repository to markup a feature as implemented.

These markups can be changed in the gdcc_conf.py if another format is preferred.

# Crontab
A script like this could be created to updated the documenation matrix and automatically generate a new GDD.
```
    eval `ssh-agent`
    function cleanup {
        /bin/kill $SSH_AGENT_PID
    }
    trap cleanup EXIT
    ssh-add

    /home/user/GameDevControlCenter/matrix_update.py && /home/user/GameDevControlCenter/gdd_to_pdf.py
```
Note that this script depends on the default ssh key in ~/.ssh/id_rsa is no password and can be used to pull both the source and documentation repositories. If another key is used provide correct path to ssh-add, for example:

    ...
    trap cleanup EXIT
    ssh-add /home/user/.ssh/my_other_key.rsa
    ...
