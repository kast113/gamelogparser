import json
import logging
from abc import ABC, abstractmethod
from json import JSONDecodeError

from schemas import GetBalanceSchema, GameLogTypeEnum, WriteBetSchema

logger = logging.getLogger(__name__)


class GameLogParser(ABC):

    log_type: GameLogTypeEnum
    payload: dict

    @abstractmethod
    def __init__(self, log_type: GameLogTypeEnum, payload: str):
        self.log_type = log_type
        try:
            self.payload = json.loads(payload)
        except JSONDecodeError as exc:
            logger.error(exc)
            raise

    @abstractmethod
    def get_balance(self) -> GetBalanceSchema:
        pass

    @abstractmethod
    def write_bet(self) -> WriteBetSchema:
        pass


class XgamesGameLogParser(GameLogParser):

    def __init__(self, log_type: GameLogTypeEnum, payload: str):
        super().__init__(log_type, payload)

    def get_balance(self) -> GetBalanceSchema:
        """
        {
            "cmd": "getbalance",
            "server": "stage_test",
            "hall": "44434343",
            "login": "sdsddsdsd",
            "sessionid": "edaf919617bfdbe60955f1707f4c968e0585d55e",
            "currency": "USD",
            "sign": "842444f39317fe20440aa4251616be28"
        }
        """
        if self.log_type != GameLogTypeEnum.get_balance:
            raise
        return GetBalanceSchema(
            sign=self.payload.get('sign'),
            currency=self.payload.get('currency'),
            login=self.payload.get('login'),
            hall=self.payload.get('hall')
        )

    def write_bet(self) -> WriteBetSchema:
        return WriteBetSchema()


class TBSGameLogParser(GameLogParser):

    def __init__(self, log_type: GameLogTypeEnum, payload: str):
        super().__init__(log_type, payload)

    def get_balance(self) -> GetBalanceSchema:
        """
        {'status': 'success', 'login': 'abbd878b-9171-4954-b0d0-6e633583ffe8', 'balance': '43', 'hall': 11307908, 'currency': 'EUR', 'sign': '110433438b3f84c2a85d9b09fe055cc5'}
        """
        if self.log_type != GameLogTypeEnum.get_balance:
            raise
        return GetBalanceSchema(
            sign=self.payload.get('sign'),
            currency=self.payload.get('currency'),
            login=self.payload.get('login'),
            hall=self.payload.get('hall')
        )

    def write_bet(self) -> WriteBetSchema:
        return WriteBetSchema()