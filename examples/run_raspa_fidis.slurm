#!/bin/bash -l
#SBATCH --time=1:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

export RASPA_DIR=/home/ongari/aiida-database/data/raspa
export DYLD_LIBRARY_PATH=/work/lsmo/aiida-lsmo-codes/lib/raspa_fidis
export LD_LIBRARY_PATH=/work/lsmo/aiida-lsmo-codes/lib/raspa_fidis

/work/lsmo/aiida-lsmo-codes/simulate_fidis
