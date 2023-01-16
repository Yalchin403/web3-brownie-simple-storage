from brownie import accounts, SimpleStorage, network
import os
from .utils import get_account


class Utils:
    def deploy_contract():
        account = get_account(network, accounts)
        print(f"using account {account}")
        simple_storage = SimpleStorage.deploy({"from": account})
        print("Deployed contract")
        print("Retrieving current value of favorite number")
        print(simple_storage.retrieve())
        print("Setting numberber for favorite number")
        transaction = simple_storage.store(69, {"from": account})
        transaction.wait(1)
        print("Retrieving new value of favorite number")
        print(simple_storage.retrieve())


def main():
    Utils.deploy_contract()
