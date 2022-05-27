from pathlib import Path

import pandas as pd
from pandas._testing import assert_frame_equal

import DockQ

TEST_DATA_DIR = Path(__file__).parent / 'data'


def test_calculate_dockq_score():
    # when
    calc_dock_q = DockQ.calc_DockQ(model=str(TEST_DATA_DIR / 'model.pdb'),
                                   native=str(TEST_DATA_DIR / 'native.pdb'),
                                   use_CA_only=False, capri_peptide=False)
    # then
    assert calc_dock_q == {'DockQ': 0.699929293073312,
                           'irms': 1.231691803285442,
                           'Lrms': 1.5159500885615596,
                           'fnat': 0.533333,
                           'nat_correct': 32,
                           'nat_total': 60,
                           'fnonnat': 0.238095,
                           'nonnat_count': 10,
                           'model_total': 42, 'chain1': 'A',
                           'chain2': 'B', 'len1': 374,
                           'len2': 228,
                           'class1': 'receptor',
                           'class2': 'ligand'}
