from brownie import (
    network, 
    config, 
    accounts, 
)
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS =["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS =["mainnet-fork", "mainnet-fork-dev"]

def get_account(index=None, id=None):

    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS 
    or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        print("Running brownie local account!")
        return accounts[0]
    else:
        print("Running on " + network.show_active() + "network.")
        return accounts.add(config['wallets']["from_key"])
