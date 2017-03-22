# -*- coding: utf-8 -*-

# Copyright (c) 2016 by University of Kassel and Fraunhofer Institute for Wind Energy and Energy
# System Technology (IWES), Kassel. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

import pytest
import os

import pandapower as pp
import pandapower.networks as pn
from pandapower.converter import from_mpc
from pandapower.toolbox import convert_format
try:
    import pplog as logging
except:
    import logging

logger = logging.getLogger(__name__)


def test_from_mpc():
    case24 = pn.case24_ieee_rts()
    this_file_path = os.path.dirname(os.path.realpath(__file__))
    mat_case_path = os.path.join(this_file_path, 'case24_ieee_rts.mat')
    case24_from_mpc = from_mpc(mat_case_path, f_hz=60, casename_mpc_file='mpc')
    case24 = convert_format(case24)

    pp.runpp(case24)
    pp.runpp(case24_from_mpc)

    assert case24_from_mpc.converged
    assert pp.nets_equal(case24, case24_from_mpc, check_only_results=True)


if __name__ == '__main__':
#    test_from_mpc()
    pytest.main(["test_from_mpc.py", "-s"])
