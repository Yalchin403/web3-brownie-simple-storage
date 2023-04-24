from brownie import (
    accounts,
    SimpleStorage,
    network,
    Contract,
    MyToken,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
)
import os
from .utils import get_account, encode_function_data


class Utils:
    @staticmethod
    def deploy_contract():
        account = get_account(network, accounts)
        # print(f"using account {account}")
        # simple_storage = SimpleStorage.deploy({"from": account})
        # print("Deployed contract")
        # print("Retrieving current value of favorite number")
        # print(simple_storage.retrieve())
        # print("Setting numberber for favorite number")
        # transaction = simple_storage.store(69, {"from": account})
        # transaction.wait(1)
        # print("Retrieving new value of favorite number")
        # print(simple_storage.retrieve())
        upgradeable_nft_erc1155 = MyToken.deploy(
            {"from": account},
            publish_source=config["networks"][network.show_active()]["verify"],
        )

        proxy_admin = ProxyAdmin.deploy(
            {"from": account},
        )

        encoded_initializer_function = encode_function_data()

        proxy = TransparentUpgradeableProxy.deploy(
            upgradeable_nft_erc1155.address,
            proxy_admin.address,
            encoded_initializer_function,
            {"from": account, "gas_limit": 1000000},
        )
        print(f"Proxy deployed to {proxy} ! You can now upgrade it to version 2!")
        proxy_contract = Contract.from_abi("MyToken", proxy.address, MyToken.abi)
        print(
            f"Here is the initial value in the MyToken: {proxy_contract.get_random_value()}"
        )


def main():
    utils = Utils()
    utils.deploy_contract()
