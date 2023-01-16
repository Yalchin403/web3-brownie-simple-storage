from brownie import SimpleStorage


def get_deployed_contract_address_by_index(contract, contract_index):
    return contract[contract_index]


def main():
    number_of_deployed_contracts = len(SimpleStorage)
    print(f"number of deployed SimpleStorage contracts {number_of_deployed_contracts}")
    print(get_deployed_contract_address_by_index(SimpleStorage, 0))