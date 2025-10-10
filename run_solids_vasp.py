input_text = """
---COMPOSITION---
C  2
---COMPOSITION---
formula_units           4
dimension               3
#symmetries              16-74
volume_factor           1.0
tol_atomic_overlap      0.95
algorithm               evolutive

#EVOLUTIVE PARAMETERS:
nof_initpop             15    #Initial Population
nof_matings             12     #Number of matings
nof_strains             3
nof_xchange             0

#NICHING PARAMETERS:
tol_similarity          0.95  #Tol for similarity
cutoff_energy           2.0  #Energy Cut-off
cutoff_population       8     #Max population size

#HALT CRITERION:
nof_generations         10    #Max generations
nof_repeats             5     #Max repeated isomers
nof_stagnant            5     #Max stagnant cycles

#THEORY LEVEL:
nof_processes           6    #Number of parallel local opts
calculator              VASP
nof_parcalcs            7

---VASP---
#!/bin/bash
set -e
export ONEAPI_ROOT=$HOME/intel/oneapi
#Library libimf.so E.G. for Ubuntu
export LD_LIBRARY_PATH=$ONEAPI_ROOT/compiler/2025.1/lib:$LD_LIBRARY_PATH
# Intel MPI
export PATH=$ONEAPI_ROOT/mpi/latest/bin:$PATH
export LD_LIBRARY_PATH=$ONEAPI_ROOT/mpi/latest/lib:$LD_LIBRARY_PATH
# Intel MKL
export LD_LIBRARY_PATH=$ONEAPI_ROOT/mkl/latest/lib/intel64:$LD_LIBRARY_PATH
export LIBRARY_PATH=$ONEAPI_ROOT/mkl/latest/lib/intel64:$LIBRARY_PATH
export CPATH=$ONEAPI_ROOT/mkl/latest/include:$CPATH
# Executables
export exe_mpirun=$ONEAPI_ROOT/mpi/latest/bin/mpirun
export exe_vasp=$HOME/vasp544/vasp.5.4.4/bin/vasp_std
#Unlimited stack adjustment
ulimit -s unlimited
# DEFINE SCRATCH and DIR_ACTUAL
export SCRATCH=$HOME/SCRATCH/fortiz
export basename={basename}
export TMPDIR=$SCRATCH/$basename
mkdir -p $SCRATCH
mkdir -p $TMPDIR
DIR_ACTUAL=$(pwd)
# PREPARE FILES and RUN VASP
cp INCAR KPOINTS POTCAR $TMPDIR
cp $basename\_POSCAR.vasp $TMPDIR/POSCAR
cd $TMPDIR
$exe_mpirun -np 4 $exe_vasp > $DIR_ACTUAL/$basename.out
# RETURN SELECTED FILES AND DELETE TRASH
cp OUTCAR     $DIR_ACTUAL/$basename\_OUTCAR
cp CONTCAR    $DIR_ACTUAL/$basename\_CONTCAR.vasp
cd $DIR_ACTUAL
rm -rf $TMPDIR
exit 0
---VASP---
"""
inputfile = 'INPUT.txt'
with open(inputfile, "w") as f: f.write(input_text)
if __name__ == "__main__":
    from solids.heuristic  import mainAlgorithm
    xopt_sort=mainAlgorithm(inputfile)
