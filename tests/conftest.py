import pytest

from worlddata.worlddata import WorldData


@pytest.fixture(scope="session")
def world_data():
    _worlddata = WorldData(auth_token='70153e74-70cd-414a-ab61-84fe7adf5c56')

    return _worlddata
