from typing import List

from src.apps.users.models import ETH, Blockchain, User, Wallet


def create_user(name: str, wallets: List[Wallet]) -> User:
    return User(name=name, wallets=wallets)


def create_wallets(addresses: List[str], blockchains: List[Blockchain]) -> List[Wallet]:
    return [
        Wallet(address=address, blockchain=blockchain)
        for address, blockchain in zip(addresses, blockchains)
    ]


user_1 = create_user(
    name="Crypto Boar",
    wallets=create_wallets(
        addresses=["0xF96081f23CaEbbA2E338473561d47Fd91A997bB0"],
        blockchains=[ETH],
    ),
)
whale_1 = create_user(
    name="Fatty 1",
    wallets=create_wallets(
        addresses=["0xF96081f23CaEbbA2E338473561d47Fd91A997bB0"],
        blockchains=[ETH],
    ),
)
whale_2 = create_user(
    name="Fatty 2",
    wallets=create_wallets(
        addresses=["0x67C2F31cFB8a809634De7202257d5537ca671DD5"],
        blockchains=[ETH],
    ),
)
whale_3 = create_user(
    name="Fatty 3",
    wallets=create_wallets(
        addresses=["0x0caC9C3D7196f5BbD76FaDcd771fB69b772c0F9d"],
        blockchains=[ETH],
    ),
)
