input_text = """
---COMPOSITION---
Mg   1
Si   1
O    3
---COMPOSITION---
formula_units           4
dimension               3
symmetries             16-74
fixed_lattice          2.474 8.121 6.138 90.0 90.0 90.0
#custom_tolerances      Ti,Ti,1.2 Ti,O,1.3 O,O,1.2
#---TOLERANCES---
#Au Au 1.2
#Ag Ag 1.3
#Au Ag 1.2
#---TOLERANCES---
volume_factor           1.0
tol_atomic_overlap      0.95

#EVOLUTIVE PARAMETERS:
nof_initpop             10    #Initial Population
nof_matings             5     #Number of matings
nof_strains             5
nof_xchange             5

#NICHING PARAMETERS:
tol_similarity          0.95  #Tol for similarity
cutoff_energy           10.0  #Energy Cut-off
cutoff_population       8     #Max population size

#HALT CRITERION:
nof_generations         10    #Max generations
nof_repeats             5     #Max repeated isomers
nof_stagnant            5     #Max stagnant cycles

#THEORY LEVEL:
nof_processes           10    #Number of parallel local opts
calculator              GULP
path_exe                /home/carlos0790/installdir/bin/gulp
---GULP---
opti conjugate nosymmetry conv
switch_minimiser bfgs gnorm 0.01
vectors
LATTICEVECTORS
frac
COORDINATES
space
1
species
Mg 1.8
Si 2.4
O -1.4
lennard 12 6
Mg O  2.5 0.0 0.0 6.0
Mg Si 1.5 0.0 0.0 6.0
Si O  1.5 0.0 0.0 6.0
Mg Mg 1.5 0.0 0.0 6.0
Si O  1.5 0.0 0.0 6.0
O  O  2.5 0.0 0.0 6.0
buck
Mg O   806.915 0.291 2.346 0.0 10.0
Si O  1122.392 0.256 0.000 0.0 10.0
O O    792.329 0.362 31.58 0.0 10.0
Mg Mg  900.343 0.220 0.174 0.0 10.0
Mg Si 1536.282 0.185 0.000 0.0 10.0
Si Si 3516.558 0.150 0.000 0.0 10.0
maxcyc
800
switch rfo cycle 350
---GULP---
"""
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import genetic_algorithm
    xopt_sort=genetic_algorithm(inputfile)
