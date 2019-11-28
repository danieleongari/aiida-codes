#!/bin/bash

full_path=$(realpath $0)
AIIDA_CODE_DIR=$(dirname $full_path)/..

export RASPA_DIR=$AIIDA_CODE_DIR/data/raspa
export DYLD_LIBRARY_PATH=$AIIDA_CODE_DIR/lib/raspa_4467e14_ubu18
export LD_LIBRARY_PATH=$AIIDA_CODE_DIR/lib/raspa_4467e14_ubu18

$AIIDA_CODE_DIR/bin/simulate_4467e14_ubu18

# If not working, possibly some library is in a different place or missing.
# Please open an issue at https://github.com/lsmo-epfl/aiida-lsmo-codes/issues
