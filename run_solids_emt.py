input_text = """
---COMPOSITION---
Au 2
Ag 2
---COMPOSITION---
formula_units        2
dimension            3
algorithm            stochastich
#symmetries          16-74
#fixed_lattice       2.474 8.121 6.138 90.0 90.0 90.0
#---TOLERANCES---
#Au Au 2.8
#Ag Ag 2.8
#Au Ag 2.7
#---TOLERANCES---
volume_factor           1.0
tol_atomic_overlap      0.95

#ALGORITHM PARAMETERS:
nof_initpop             30    #Initial Population

#NICHING PARAMETERS:
tol_similarity          0.95 #Tol for similarity
cutoff_energy           10.0  #Energy Cut-off

#HALT CRITERION:
nof_stages              3    #No. of Optimization Stages

#THEORY LEVEL:
calculator              EMT
nof_processes           5    #Number of parallel local opts
"""
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import mainAlgorithm
    xopt_sort=mainAlgorithm(inputfile)
