#!/usr/bin/env bash

# Check for the lock file, if it exists, we know this vagrant VM has already been
# provisioned and we simply want to reload everything

lockfile=~/install-python3.lock

if [ -e "$lockfile" ]; then
    # Reload steps
    echo "Reload detected, refreshing env"


    # Cat-ing out the requirements txt to make sure it's populated
    echo "Will install these pip dependencies: \n"
    cat ~/requirements.txt
    sleep 10


    # Run pip install on requirements to pick up new packages
    ~/python3_env/bin/pip install -r ~/deployment/requirements.txt
else
    # Setup the env
    virtualenv -p /usr/bin/python3  ~/python3_env/

    # Cat-ing out the requirements txt to make sure it's populated
    echo "Will install these pip dependencies: \n"
    cat ~/deployment/requirements.txt
    sleep 10

    # Upgrade pip
    ~/python3_env/bin/pip install --upgrade

    # Pip install the requirements
    ~/python3_env/bin/pip install -r ~/deployment/requirements.txt

    # Make this env activate on log in
    echo "source ~/python3_env/bin/activate" >> ~/.profile

    # Place the lockfile
    touch ~/install-python3.lock
    echo "Python 3 setup complete"
fi
