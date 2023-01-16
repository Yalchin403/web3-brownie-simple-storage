import os


def get_account(network, accounts):
    if network.show_active() == "development":
        return accounts[0]
    
    return accounts.add(os.getenv("PRIVATE_KEY"))