input_text = """
---COMPOSITION---
Ti   1
O    2
---COMPOSITION---
algorithm               evolutive
formula_units           4
dimension               3
# symmetries              16-74
# fixed_lattice           2.474 8.121 6.138 90.0 90.0 90.0
# ---TOLERANCES---
# Mg Mg 2.4
# Mg Si 2.4
# Mg O  1.75
# Si Si 2.4
# Si O  1.6
# O  O  2.4
# ---TOLERANCES---
volume_factor           1.0
tol_atomic_overlap      0.95

#ALGORITHM PARAMETERS:
nof_initpop             10    #Initial Population
nof_matings             20    #No. of matings
nof_strains             5     #No. of strains
nof_xchange             5     #No. of atom exchanges

#NICHING PARAMETERS:
tol_similarity          0.95 #Tol for similarity
cutoff_energy           10.0  #Energy Cut-off

#HALT CRITERION:
nof_stages              3     #No. of Optimization Stages
nof_repeats             5     #No. of repeats
nof_stagnant            3     #No. of stagnant generations
nof_generations         10    #No. of generations

#THEORY LEVEL:
calculator              GULP
nof_processes           10    #Number of parallel local opts
path_exe                /home/fili/installdir/bin/gulp

---GULP---
opti conj conp
switch_minimiser bfgs gnorm 0.5
vectors
LATTICEVECTORS
frac
COORDINATES
species
Ti  2.196
O  -1.098
buck
Ti Ti 31120.1 0.1540 5.25  15
O  O  11782.7 0.2340 30.22 15
Ti O  16957.5 0.1940 12.59 15
lennard 12 6
Ti Ti   1   0 15
O  O    1   0 15
Ti O    1   0 15
---GULP---

# ---GULP---
# opti conjugate nosymmetry conp
# switch_minimiser bfgs gnorm 0.01
# pressure 100 GPa
# vectors
# LATTICEVECTORS
# frac
# COORDINATES
# space
# 1
# species
# Mg  2.0
# Al  3.0
# O  -2.0
# lennard 12 6
# Mg O   1.50 0.00 0.00 6.0
# Al O   1.50 0.00 0.00 6.0
# O O    1.50 0.00 0.00 6.0
# Mg Mg  1.50 0.00 0.00 6.0
# Mg Al  1.50 0.00 0.00 6.0
# Al Al  1.50 0.00 0.00 6.0
# buck
# Mg O 1428.5 0.2945 0.0 0.0 7.0
# Al O 1114.9 0.3118 0.0 0.0 7.0
# O O  2023.8 0.2674 0.0 0.0 7.0
# maxcyc 850
# switch rfo 0.010
# ---GULP---
# ---GULP---
# opti conjugate nosymmetry conv
# switch_minimiser bfgs gnorm 0.01
# vectors
# LATTICEVECTORS
# frac
# COORDINATES
# space
# 1
# species
# Mg 1.8
# Si 2.4
# O -1.4
# lennard 12 6
# Mg O  2.5 0.0 0.0 6.0
# Mg Si 1.5 0.0 0.0 6.0
# Si O  1.5 0.0 0.0 6.0
# Mg Mg 1.5 0.0 0.0 6.0
# Si O  1.5 0.0 0.0 6.0
# O  O  2.5 0.0 0.0 6.0
# buck
# Mg O   806.915 0.291 2.346 0.0 10.0
# Si O  1122.392 0.256 0.000 0.0 10.0
# O O    792.329 0.362 31.58 0.0 10.0
# Mg Mg  900.343 0.220 0.174 0.0 10.0
# Mg Si 1536.282 0.185 0.000 0.0 10.0
# Si Si 3516.558 0.150 0.000 0.0 10.0
# maxcyc
# 800
# switch rfo cycle 350
# ---GULP---
"""
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import mainAlgorithm
    xopt_sort=mainAlgorithm(inputfile)
