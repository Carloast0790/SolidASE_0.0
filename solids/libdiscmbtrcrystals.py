import numpy as np
from dscribe.descriptors import MBTR

def build_mbtr(atoms_list):
    """
    Construye un objeto MBTR configurado para un conjunto de estructuras.
    """
    # Especies presentes en todas las estructuras de entrada
    species = sorted(set(
        sym for atoms in atoms_list for sym in atoms.get_chemical_symbols()
    ))

    mbtr = MBTR(
        species=species,
        geometry={"function": "distance"},
        weighting={"function": "inverse_square", "r_cut": 10, "threshold": 1e-3},
        grid={"min": 0, "max": 10, "sigma": 1e-3, "n": 100},
        periodic=True,
        normalization="none",
        sparse=False,
        dtype="float64",
    )
    return mbtr

# ------------------------------------------------------------------------------------------
def descriptor_comparison_calculated(atoms_list_in, tolerance, nproc=2):
    """
    Compara los descriptores MBTR de una lista de estructuras y elimina aquellas
    demasiado similares segun el umbral dado.
    """
    atoms_list_out = []
    mbtr = build_mbtr(atoms_list_in)
    descriptors = mbtr.create(atoms_list_in, n_jobs=nproc)

    disc_count = 0
    for i in range(len(descriptors)):
        stop_flag = False
        for j in range(i + 1, len(descriptors)):
            norm_i = np.linalg.norm(descriptors[i])
            norm_j = np.linalg.norm(descriptors[j])
            dot_product = np.dot(descriptors[i], descriptors[j])
            similarity = dot_product / (norm_i * norm_j)
            if similarity >= tolerance:
                print(f"{atoms_list_in[i].info['i']} removed, too similar to {atoms_list_in[j].info['i']}, similarity = {similarity:.5f}")
                disc_count += 1
                stop_flag = True
                break
        if not stop_flag:
            atoms_list_out.append(atoms_list_in[i])

    print(f"\n{disc_count} structures removed by similarity in generation comparison\n")
    return atoms_list_out

# ------------------------------------------------------------------------------------------
def descriptor_comparison_calculated_vs_pool(atoms_calculated, atoms_pool, tolerance, nproc=2):
    """
    Compara los descriptores MBTR de las estructuras recien calculadas contra un pool existente,
    y elimina aquellas demasiado similares segun el umbral dado.
    """
    print('---------------- Duplicates Removal Gen vs Pool -------------------\n')

    mbtr = build_mbtr(atoms_calculated + atoms_pool)
    descr_calc = mbtr.create(atoms_calculated, n_jobs=nproc)
    descr_pool = mbtr.create(atoms_pool, n_jobs=nproc)

    disc_count = 0
    different_calc = []

    for i in range(len(descr_calc)):
        stop_flag = False
        for j in range(len(descr_pool)):
            norm_i = np.linalg.norm(descr_calc[i])
            norm_j = np.linalg.norm(descr_pool[j])
            dot_product = np.dot(descr_calc[i], descr_pool[j])
            similarity = dot_product / (norm_i * norm_j)
            if similarity >= tolerance:
                print(f"{atoms_calculated[i].info['i']} removed, too similar to {atoms_pool[j].info['i']}, similarity = {similarity:.5f}")
                stop_flag = True
                disc_count += 1
                break
        if not stop_flag:
            different_calc.append(atoms_calculated[i])

    if different_calc:
        print(f"\n{disc_count} structures removed by similarity in Gen vs Pool comparison\n")
    else:
        print("\nZero structures removed by similarity in Gen vs Pool comparison\n")

    return different_calc
