#!/bin/bash

SCRIPT_DIR=`dirname "${BASH_SOURCE[0]}"`
if [ ! -e "$SCRIPT_DIR/serverstop.sh" ]; then
    SCRIPT_DIR=$SCRIPT_DIR/scripts
fi

source "$SCRIPT_DIR/serverstop.sh"
# PJK 20/03/2015
# source "$SCRIPT_DIR/cronstop.sh"
