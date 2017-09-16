import os

from addons import *
from utils import *


tdir = 'Symmetry-Adapted-Perturbation-Theory'


def test_SAPT0ao(workspace):
    exe_py(workspace, tdir, 'SAPT0ao')


def test_SAPT0(workspace):
    exe_py(workspace, tdir, 'SAPT0')


def test_SAPT0_ROHF(workspace):
    exe_py(workspace, tdir, 'SAPT0_ROHF')
