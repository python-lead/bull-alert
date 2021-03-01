from unittest import mock
from unittest.mock import MagicMock

import pytest

from src.apps.services.etherscan import (
    EtherscanAccountModule,
    EtherscanClientResponse,
    EtherscanService,
)


class TestEtherscanAccountModule:
    @classmethod
    def setup_class(cls):
        cls.address = "0xF96081f23CaEbbA2E338473561d47Fd91A997bB0"
        cls.data_dict = {
            "status": 1,
            "message": "OK",
            "result": 217628157490781111,
        }
        cls.error_response_dict = {
            "status": 0,
            "message": "NOTOK",
            "result": "Error! Invalid address format",
        }
        cls.expected_value = EtherscanClientResponse(
            status=cls.data_dict["status"],
            message=cls.data_dict["message"],
            result=cls.data_dict["result"],
        )
        cls.expected_value_on_error = EtherscanClientResponse(
            status=cls.error_response_dict["status"],
            message=cls.error_response_dict["message"],
            result=cls.error_response_dict["result"],
        )

    def setup_method(self):
        self.service = EtherscanAccountModule()

    @mock.patch("src.apps.services.etherscan.httpx.Client")
    def test_get_address_balance(self, client_class_mock):
        self._prepare_get_mock(class_mock=client_class_mock, data=self.data_dict)

        result = self.service.get_balance(address=self.address)
        assert result == self.expected_value

    @mock.patch("src.apps.services.etherscan.httpx.Client")
    def test_get_balance_invalid_request(self, client_class_mock):
        self._prepare_get_mock(
            class_mock=client_class_mock, data=self.error_response_dict
        )

        result = self.service.get_balance(address="")
        assert result == self.error_response_dict

    @staticmethod
    def _prepare_get_mock(class_mock: mock.Mock, data: dict, status_code: int = 200):
        response_mock = MagicMock()
        response_mock.status_code = status_code
        response_mock.json.return_value = data
        client_mock = MagicMock()
        class_mock.return_value = client_mock
        client_mock.get.return_value = response_mock


class TestEtherscanService:
    @classmethod
    def setup_class(cls):
        cls.address = "0xF96081f23CaEbbA2E338473561d47Fd91A997bB0"
        cls.expected_value = EtherscanClientResponse(
            status=1,
            message="OK",
            result=1500000000000000000,
        )
        cls.failing_value = EtherscanClientResponse(
            status=0,
            message="NOOK",
            result="Error! Invalid address format",
        )

    def setup_method(self):
        self.service = EtherscanService(address=self.address)

    @mock.patch("src.apps.services.etherscan.EtherscanClient.get")
    def test_get_balance(self, get_mock):
        get_mock.return_value = self.expected_value
        result = self.service.get_balance()

        assert result == 1.5

    @mock.patch("src.apps.services.etherscan.EtherscanClient.get")
    def test_get_balance_failed_request(self, get_mock):
        get_mock.return_value = self.failing_value

        with pytest.raises(ValueError, match=self.failing_value.result):
            self.service.get_balance()
