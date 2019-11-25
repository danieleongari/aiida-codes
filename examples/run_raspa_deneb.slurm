#!/bin/bash -l
#SBATCH --time=1:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1

#SBATCH --partition=serial

export RASPA_DIR=/home/ongari/aiida-database/data/raspa
export DYLD_LIBRARY_PATH=/work/lsmo/aiida-lsmo-codes/lib/raspa_deneb
export LD_LIBRARY_PATH=/work/lsmo/aiida-lsmo-codes/lib/raspa_deneb

/work/lsmo/aiida-lsmo-codes/simulate_deneb
