from brownie import (
    MyTokenV2,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
    network,
    Contract,
    accounts,
)
from .utils import get_account, upgrade


def main():
    account = get_account(network, accounts)
    print(f"Deploying to new implementation contract {network.show_active()}")
    implementationV2 = MyTokenV2.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    proxy = TransparentUpgradeableProxy.at(TransparentUpgradeableProxy[-1])
    proxy_admin = ProxyAdmin.at(ProxyAdmin[-1])

    upgrade_tx = upgrade(
        account, proxy, implementationV2, proxy_admin_contract=proxy_admin
    )
    upgrade_tx.wait(1)
    print("Proxy has been upgraded!")
    proxy_contract = Contract.from_abi("MyTokenV2", proxy.address, MyTokenV2.abi)
    print(f"value {proxy_contract.get_random_value()}")
