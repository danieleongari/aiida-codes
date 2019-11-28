#!/bin/bash -l
#SBATCH --time=1:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

#SBATCH --partition=serial

AIIDA_CODE_DIR="/work/lsmo/aiida-lsmo-codes"
export RASPA_DIR=$AIIDA_CODE_DIR/data/raspa
export DYLD_LIBRARY_PATH=$AIIDA_CODE_DIR/lib/raspa_4467e14_deneb
export LD_LIBRARY_PATH=$AIIDA_CODE_DIR/lib/raspa_4467e14_deneb

$AIIDA_CODE_DIR/bin/simulate_4467e14_deneb
