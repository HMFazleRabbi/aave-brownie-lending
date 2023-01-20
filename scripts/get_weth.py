from scripts.helpful_scripts import get_account
from brownie import config, network, interface
from web3 import Web3

def get_weth(value=Web3.toWei(0.001, "ether") ):
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": value})
    tx.wait(1)
    print(f"Received {value} WETH")
    return tx

def main():
    get_weth()