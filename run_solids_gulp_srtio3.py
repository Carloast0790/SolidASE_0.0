input_text = """
---COMPOSITION---
Sr   1
Ti   1
O    3
---COMPOSITION---
formula_units           10
dimension               3
number_of_xtals         5
#symmetries             16-74
#fixed_lattice          2.474 8.121 6.138 90.0 90.0 90.0
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
path_exe                /Users/fortiz/installdir/bin/gulp
---GULP---
opti conjugate nosymmetry conp
switch_minimiser bfgs gnorm 0.01
vectors
LATTICEVECTORS
frac
COORDINATES
space
1
species
Sr 2.00
Ti 4.00
O -2.00
lennard 12 6
Sr Sr 1.0 0.0 0. 6.0
Sr Ti 1.0 0.0 0. 6.0
Sr O  2.0 0.0 0. 6.0
Ti Ti 1.0 0.0 0. 6.0
Ti O  2.0 0.0 0. 6.0 
O  O  2.0 0.0 0. 6.0 
buck
Sr Sr 9949.1  0.2446 0.0 0. 8.0
Sr Ti 12708.1 0.2191 0.0 0. 8.0
Sr O  1805.2  0.3250 0.0 0. 8.0
Ti Ti 16963.1 0.1847 0.0 0. 8.0
Ti O  845.0   0.3770 0.0 0. 8.0
O  O  22746.3 0.1490 0.0 0. 8.0
maxcyc 1500
---GULP---
"""
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import genetic_algorithm
    xopt_sort=genetic_algorithm(inputfile)
