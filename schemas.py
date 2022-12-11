from enum import Enum

import pydantic


class GameLogProviderEnum(str, Enum):
    """GameLogProviderEnum"""
    xgames = 'xgames'
    tbs = 'tbs'


class GameLogTypeEnum(str, Enum):
    """GameLogTypeEnum"""
    write_bet = 'write_bet'
    get_balance = 'get_balance'

'''
{
"cmd":"getbalance",
"server":"stage_test",
+"hall":"44434343",
+"login":"sdsddsdsd",
"sessionid":"edaf919617bfdbe60955f1707f4c968e0585d55e",
+"currency":"USD",
+"sign":"842444f39317fe20440aa4251616be28"
}

{
'status': 'success', 
+'login': 'abbd878b-9171-4954-b0d0-6e633583ffe8', 
'balance': '43', 
+'hall': 11307908, 
+'currency': 'EUR', 
+'sign': '110433438b3f84c2a85d9b09fe055cc5'
}

'''


class GetBalanceSchema(pydantic.BaseModel):
    """GetBalanceSchema"""

    sign: str
    currency: str
    login: str
    hall: int  # hall_pk_id


class WriteBetSchema(pydantic.BaseModel):
    """WriteBetSchema"""

    pass
