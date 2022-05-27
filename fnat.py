import math
from itertools import product
from typing import List

import Bio


def distance(coord_one: List[float], coord_two: List[float]) -> float:
    return ((coord_one[0] - coord_two[0]) * (coord_one[0] - coord_two[0]) +
            (coord_one[1] - coord_two[1]) * (coord_one[1] - coord_two[1]) +
            (coord_one[2] - coord_two[2]) * (coord_one[2] - coord_two[2]))


def min_distance(atoms_one: List[Bio.PDB.Atom.Atom], atoms_two: List[Bio.PDB.Atom.Atom]) -> float:
    dist = [distance(atom_one.coord, atom_two.coord) for atom_one, atom_two in product(atoms_one, atoms_two)]
    return min(dist)


def calc_fnat(model:str, native:str) -> float:
    pdb_parser = Bio.PDB.PDBParser(QUIET=True)
    ref_model = pdb_parser.get_structure("reference", native)[0]
    sample_model = pdb_parser.get_structure("model", model)[0]
    chain_one, chain_two = ref_model
    for res_chain_one in chain_one.child_list:
        for res_chain_two in chain_two.child_list:
            dist = min_distance(res_chain_one.child_list, res_chain_two.child_list)
            if dist < 5 * 5:
                one_id = res_chain_one.full_id[3][1]
                two_id = res_chain_two.full_id[3][1]
                print(f'{one_id}{res_chain_one.parent.id} {two_id}{res_chain_two.parent.id}', math.sqrt(dist))
                # print(f'{one_id}{chain_one.id} -> {two_id}{chain_two.id} => {math.sqrt(dist)}')
    return 0
