from urllib.parse import ParseResult, urlencode, urlparse, urlunparse

import httpx
from httpx import Response

from src.apps.services.schemas import EtherscanClientResponse
from src.apps.users.schemas import ETH
from src.core.config import settings


class EtherscanClient:
    def __init__(self):
        self._api_key = settings.ETHERSCAN_API_KEY
        self._api_url = "https://api.etherscan.io/api"
        self.url: ParseResult = urlparse(self._api_url)
        self.client = httpx.Client()

    def get(self, parsed_params: str):
        return self.handle_response(
            self.client.get(urlunparse(self.url._replace(query=parsed_params)))
        )

    def handle_response(self, response: Response) -> EtherscanClientResponse:
        if not response.status_code == 200:
            raise NotImplementedError(
                "There is currently no support for failed requests"
            )
        return EtherscanClientResponse(**response.json())


class EtherscanAccountModule:
    BALANCE_ACTION = "balance"

    def __init__(self):
        self.module = "account"

    def get_balance(self, address: str):
        params = {
            "module": self.module,
            "action": self.BALANCE_ACTION,
            "address": address,
            "tag": "latest",
            "apikey": settings.ETHERSCAN_API_KEY,
        }

        client = EtherscanClient()

        return client.get(parsed_params=(urlencode(params)))


class EtherscanModulesManager:
    def __init__(self):
        self.account = EtherscanAccountModule()


class EtherscanService:
    def __init__(self, address: str):
        self.address = address
        self.modules = EtherscanModulesManager()
        self.blockchain = ETH

    def get_balance(self):
        response = self.modules.account.get_balance(address=self.address)
        if response.status == 0:
            raise ValueError(response.result)

        return self.blockchain.get_super_unit_value(response.result)
