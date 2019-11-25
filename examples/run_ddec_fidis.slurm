#!/bin/bash -l
#SBATCH --time=1:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=28
#### Gacrux/Skylake nodes (better to use this and have more memory!)
#SBATCH --constraint=s6g1
#### Fidis/Broadwell nodes
##SBATCH --constraint=E5v4

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Rename your cube file in "valence_density.cube" (this won't work if you have multiple .cube files!)
if [ ! -f valence_density.cube ]; then
    cp *.cube valence_density.cube
fi

# Create "job_control.txt" with the CORE (BC: NOT valence) electrons for standard PBE pseudos (except for Mg-q2 instead of -q10)
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
12 10
13 10
14 10
15 10
16 10
17 10
18 10
19 10
20 10
21 10
22 10
23 10
24 10
25 10
26 10
27 10
28 10
29 18
30 18
31 18
32 28
33 28
34 28
35 28
36 28
37 28
38 28
39 28
40 28
41 28
42 28
43 28
44 28
45 36
46 28
47 36
48 36
49 36
50 46
51 46
52 46
53 46
54 46
55 46
56 46
57 46
58 46
59 46
60 46
61 46
62 46
63 46
64 46
65 46
66 46
67 46
68 46
69 46
70 46
71 46
72 60
73 60
74 60
75 60
76 60
77 60
78 60
79 68
80 68
81 68
82 78
83 78
84 78
85 78
86 78
</number of core electrons>
EOF

date_start=$(date +%s)
/work/lsmo/aiida-lsmo-codes/Chargemol_09_26_2017_fidis
date_end=$(date +%s)
time_run=$((date_end-date_start))
echo "Total run time: $time_run seconds"
