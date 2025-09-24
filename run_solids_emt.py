input_text = """
---COMPOSITION---
Au 2
Ag 2
---COMPOSITION---
formula_units        2
dimension            3
algorithm            evolutive
#symmetries          16-74
#fixed_lattice       2.474 8.121 6.138 90.0 90.0 90.0
#custom_tolerances   Ti,Ti,1.2 Ti,O,1.3 O,O,1.2
#---TOLERANCES---
#Au Au 1.2
#Ag Ag 1.3
#Au Ag 1.2
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
nof_processes           1    #Number of parallel local opts
"""
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import mainAlgorithm
    xopt_sort=mainAlgorithm(inputfile)
