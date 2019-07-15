# -*- coding: utf-8 -*-

import os

import pytest

def test_env_absent():
    # Even if the env var is not initially set, the environ
    # variables should not be affected.
    original_vars = dict(os.environ)

    import pygamesilent

    assert dict(os.environ) == original_vars
