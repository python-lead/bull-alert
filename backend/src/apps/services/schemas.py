from typing import Union

from pydantic import BaseModel


class EtherscanClientResponse(BaseModel):
    status: int
    message: str
    result: Union[int, str]
