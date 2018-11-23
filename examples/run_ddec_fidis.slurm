#!/bin/bash -l
#SBATCH --time=1:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
## SBATCH --partition=debug
#### Gacrux/Skylake nodes
##SBATCH --constraint=s6g1
#### Fidis/Broadwell nodes
##BATCH --constraint=E5v4

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

echo "Remember to name the cube file you want to use: valence_density.cube"

cat > job_control.txt << EOF
<net charge>
0.0
</net charge>

<charge type>
DDEC6 
</charge type>

<compute BOs>
.false.
</compute BOs>

<periodicity along A, B, and C vectors>
.true.
.true.
.true.
</periodicity along A, B, and C vectors>

<atomic densities directory complete path>
/home/ongari/aiida-database/data/chargemol_09_26_2017/atomic_densities/
</atomic densities directory complete path>

<input filename>
valence_density
</input filename>

<number of core electrons>
1  0
2  0
3  0
4  0
5  2
6  2 
7  2
8  2
9  2
10 2
11 2
12 2
13 10
14 10
15 10
16 10
17 10
18 10
19 10
20 10
</number of core electrons>
EOF

date_start=$(date +%s)
/home/ongari/aiida-codes/Chargemol_09_26_2017_fidis
date_end=$(date +%s)
time_run=$((date_end-date_start))
echo "Total run time: $time_run seconds"
