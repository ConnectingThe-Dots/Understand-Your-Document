import pytest
from src.analyzer import load_config, assign_levels

def test_assign_levels_empty():
    cfg = load_config("config/default.yaml")
    assert assign_levels([], cfg) == []
