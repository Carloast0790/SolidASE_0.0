input_text = """
---COMPOSITION---
Au 8
---COMPOSITION---
formula_units        1
dimension            3
volume_factor        1.0
tol_atomic_overlap   0.95

#ALGORITHM PARAMETERS:
algorithm            evolutive
nof_initpop          30

#Evolutive:
nof_matings          20    #No. of matings
nof_strains          5     #No. of strains
nof_xchange          5     #No. of atom exchanges

#NICHING PARAMETERS:
tol_similarity       0.95 #Tol for similarity
cutoff_energy        10.0  #Energy Cut-off

#HALT CRITERION:
#Stochastic:
nof_stages              3    #No. of Optimization Stages

#Evolutive:
nof_repeats             5     #No. of repeats
nof_stagnant            3     #No. of stagnant generations
nof_generations         10    #No. of generations

#THEORY LEVEL:
calculator              EMT
nof_processes           5    #Number of parallel local opts
"""
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import mainAlgorithm
    xopt_sort=mainAlgorithm(inputfile)
