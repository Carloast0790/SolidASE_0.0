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
    Retain only unique Atoms objects based on MBTR descriptor similarity.
    The input list is assumed to be sorted by energy (lower index = higher priority).
    """
    print('----------GENvsGEN----------\n')

    mbtr = build_mbtr(atoms_list_in)
    descriptors = mbtr.create(atoms_list_in, n_jobs=nproc)
    atoms_list_out = []
    descriptors_out = []
    disc_count = 0

    for i, desc_i in enumerate(descriptors):
        is_unique = True
        for desc_j in descriptors_out:
            norm_i = np.linalg.norm(desc_i)
            norm_j = np.linalg.norm(desc_j)
            dot_product = np.dot(desc_i, desc_j)
            similarity = dot_product / (norm_i * norm_j)
            if similarity >= tolerance:
                print(f"{atoms_list_in[i].info['i']} removed, too similar to a lower-energy structure, similarity = {similarity:.5f}")
                disc_count += 1
                is_unique = False
                break
        if is_unique:
            atoms_list_out.append(atoms_list_in[i])
            descriptors_out.append(desc_i)

    print(f"{disc_count} structures removed by similarity in generation comparison\n")
    return atoms_list_out

# ------------------------------------------------------------------------------------------
def descriptor_comparison_calculated_vs_pool(atoms_calculated, atoms_pool, tolerance, nproc=2):
    """Compares generation structures against the pool of known structures using MBTR similarity.
    in:
        atoms_calculated (list); list of Atoms objects from the current generation to be compared.
        atoms_pool (list); list of Atoms objects from the pool of known structures.
        tolerance (float); similarity threshold above which structures are considered too similar.
        nproc (int); number of processors to use for descriptor calculation.
    out:
        different_calc (list); list of Atoms objects from atoms_calculated that are sufficiently different.
    """
    print('----------GENvsPOOL----------')
    mbtr = build_mbtr(atoms_calculated + atoms_pool)
    descr_calc = mbtr.create(atoms_calculated, n_jobs=nproc)
    descr_pool = mbtr.create(atoms_pool, n_jobs=nproc)

    disc_count = 0
    different_calc = []

    for i, desc_i in enumerate(descr_calc):
        is_unique = True
        for j, desc_j in enumerate(descr_pool):
            norm_i = np.linalg.norm(desc_i)
            norm_j = np.linalg.norm(desc_j)
            dot_product = np.dot(desc_i, desc_j)
            similarity = dot_product / (norm_i * norm_j)
            if similarity >= tolerance:
                print(f"{atoms_calculated[i].info['i']} removed, too similar to {atoms_pool[j].info['i']}, similarity = {similarity:.5f}")
                disc_count += 1
                is_unique = False
                break
        if is_unique:
            different_calc.append(atoms_calculated[i])

    if different_calc:
        print(f"\n{disc_count} structures removed by similarity in Gen vs Pool comparison")
    else:
        print("\nZero structures removed by similarity in Gen vs Pool comparison")

    return different_calc


# def descriptor_comparison_calculated_vs_pool(atoms_calculated, atoms_pool, tolerance, nproc=2):
#     """Compares generation structures against the pool of known structures using MBTR similarity.
#     in:
#         atoms_calculated (list); list of Atoms objects from the current generation to be compared.
#         atoms_pool (list); list of Atoms objects from the pool of known structures.
#         tolerance (float); similarity threshold above which structures are considered too similar.
#         nproc (int); number of processors to use for descriptor calculation.
#     out:
#         different_calc (list); list of Atoms objects from atoms_calculated that are sufficiently different.
#     """
#     print('----------GENvsPOOL----------\n')
#     mbtr = build_mbtr(atoms_calculated + atoms_pool)
#     descr_calc = mbtr.create(atoms_calculated, n_jobs=nproc)
#     descr_pool = mbtr.create(atoms_pool, n_jobs=nproc)

#     disc_count = 0
#     different_calc = []

#     for i in range(len(descr_calc)):
#         stop_flag = False
#         for j in range(len(descr_pool)):
#             norm_i = np.linalg.norm(descr_calc[i])
#             norm_j = np.linalg.norm(descr_pool[j])
#             dot_product = np.dot(descr_calc[i], descr_pool[j])
#             similarity = dot_product / (norm_i * norm_j)
#             if similarity >= tolerance:
#                 print(f"{atoms_calculated[i].info['i']} removed, too similar to {atoms_pool[j].info['i']}, similarity = {similarity:.5f}")
#                 stop_flag = True
#                 disc_count += 1
#                 break
#         if not stop_flag:
#             different_calc.append(atoms_calculated[i])

#     if different_calc:
#         print(f"\n{disc_count} structures removed by similarity in Gen vs Pool comparison")
#     else:
#         print("\nZero structures removed by similarity in Gen vs Pool comparison")

#     return different_calc
