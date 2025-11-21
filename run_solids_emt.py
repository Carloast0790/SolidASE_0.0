input_text = """
---COMPOSITION---
Al 10
---COMPOSITION---
formula_units        1          #The number of atoms in composition are multiplied by this number
dimension            3          #Solids can handle 2- and 3-dimensional crystals
volume_factor        1.0        #The volume factor of the unit cell
tol_atomic_overlap   0.95       #The minimum distance between atoms is 95% the sum of their radii

#ALGORITHM PARAMETERS:
algorithm            evolutive  #stochastic -> Stochastic algorithm, evolutive-> Evolutive Algorithm
nof_initpop          10         #Size of the initial population of crystals

#Evolutive:
nof_matings          20         #Number of matings
nof_strains          6          #Number of strains
nof_xchange          0          #Number of atom exchanges

#NICHING PARAMETERS:
tol_similarity       0.96       #Tol for similarity
cutoff_energy        2.0        #Energy Cut-off
cutoff_population    10         #Number of final candidates

#HALT CRITERION:
#Stochastic:
nof_stages              2       #Number of Optimization Stages when using the Stochastich algorithm

#Evolutive:
nof_repeats             10       #Breaks the process if the same structures are repeated 5 times
nof_stagnant            5       #If the best 3 solutions are iteratively located, the process stops
nof_generations         30       #Number of generations

#THEORY LEVEL:
calculator              EMT     #Available calculators: EMT, VASP, GULP
nof_processes           10       #Number of parallel local opts
"""
#Execution of main code
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import mainAlgorithm
    xopt_sort=mainAlgorithm(inputfile)
