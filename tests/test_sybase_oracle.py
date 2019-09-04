from __future__ import unicode_literals

import io
import os

from pytest import raises
# This will treat each verifition item as a test scenario objects in Sybase and oracle
# will run through each test scenario and make sure everything passes
# as items are identified it will be a test scenario added to this list



    

sybase_conn = None  # need to install sybase python library
oracle_conn = None  # need to install oracle python libraryyy
def test_connect_oracle():
    
    from sqlalchemy import create_engine, inspect
    engine = create_engine("oracle+cx_oracle://system:Docker12345@dboracle/ORCLCDB")
    inspector = inspect(engine)
    assert True
    #all_check_constraints = inspector.get_check_constraints(
    #    "some_table", include_all=True)

def test_constraints():
    assert False
def test_functions():
    assert False
def test_users():
    assert False
def test_indexes():
    assert False
def test_collations():
    assert False
def test_triggers():
    assert False
def test_schemea():
    assert False
def test_privs():
    assert False
