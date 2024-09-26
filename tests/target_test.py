import pytest
from returns.maybe import Nothing
from repository.target_repository import *



def test_create_target():
    target = Target(target_industry="The Matrix", city_id=5, target_type_id=5871, target_priority= 2)
    create_target(target)
    assert target.target_id > 0
    assert target.target_industry == "The Matrix"

def test_get_all_targets():
    targets = get_all_target()
    targets = targets.unwrap() if targets else []
    assert len(targets) > 0

def test_get_target_by_id():
    a = find_target_by_id(8)
    assert find_target_by_id(8).unwrap().target_id == 8 if a is not Nothing else False

def test_update_target():
    update_target(8, Target(target_industry="The Matrix", city_id=5, target_type_id=5871, target_priority= 2))
    a =  find_target_by_id(8).unwrap().target_industry
    assert a == "The Matrix"

def test_delete_target():
    delete_target(8)
    assert True if find_target_by_id(8) is Nothing else False