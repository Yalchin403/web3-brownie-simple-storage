from brownie import accounts, SimpleStorage
import os
import pytest


@pytest.fixture()
def setup():
    account = accounts.add(os.getenv("POLYGON_MUMBAI_PRIVATE_KEY"))
    print(f"using account {account}")
    simple_storage = SimpleStorage.deploy({"from": account})
    print("Deployed contract")

    return {
        "account": account,
        "simple_storage": simple_storage
    }

class TestSimpleStorageRetrieveAndStore:
    def test_retrieve(self, setup):
        retrived_value = setup["simple_storage"].retrieve()
        expected_value = 0
        assert retrived_value == expected_value

    def test_store(self, setup):
        retrived_value = setup["simple_storage"].retrieve()
        expected_value = 0
        assert retrived_value == expected_value