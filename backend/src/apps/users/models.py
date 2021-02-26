from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ValidationError


class Blockchain(BaseModel):
    symbol: str
    name: str


ETH = Blockchain(symbol="eth", name="Ethereum")
BSC = Blockchain(symbol="bsc", name="Binance Smart Chain")


class BlockchainType(BaseModel):
    CORRECT_BLOCKCHAINS = (ETH, BSC)
    eth = ETH
    bnc = BSC


class Wallet(BaseModel):
    CORRECT_BLOCKCHAINS = (ETH, BSC)
    address: str
    blockchain: Blockchain

    def create_eth_wallet(self, address: str) -> Wallet:
        return self._create_wallet(address=address, blockchain=ETH)

    def create_btc_wallet(self, address: str) -> Wallet:
        return self._create_wallet(address=address, blockchain=BSC)

    def _create_wallet(self, address, blockchain: Blockchain) -> Wallet:
        if blockchain not in self.CORRECT_BLOCKCHAINS:
            raise ValidationError("Incorrect blockchain value", Blockchain)

        return Wallet(address=address, blockchain=blockchain)


class User(BaseModel):
    name: str
    wallets: Optional[List[Wallet]]
