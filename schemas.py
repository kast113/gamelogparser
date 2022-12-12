import datetime
import decimal
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
"cmd":"getbalance", ???
"server":"stage_test", ???
+"hall":"44434343",
+"login":"sdsddsdsd",
"sessionid":"edaf919617bfdbe60955f1707f4c968e0585d55e",
+"currency":"USD",
+"sign":"842444f39317fe20440aa4251616be28"
}

{
'status': 'success', ???
+'login': 'abbd878b-9171-4954-b0d0-6e633583ffe8', 
'balance': '43', ???
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

################################
# xgame loss
'''
{
'cmd': 'writebet', 
'server': 'stage_test', 
'hall': '59d1d02d-3feb-4bc0-b978-088619ad4aa8', 
+'login': '8a5b8fc4-0130-42e4-b6eb-950d12da5599', 
+ 'sessionid': '5ecabc52865421eb5606512022d0abdccf204dcd', 
+ 'tradeId': '59d1d02d-3feb-4bc0-b978-088619ad4aa8_8a5b8fc4-0130-42e4-b6eb-950d12da5599_20222_1670586024', 
+'date': '2022-12-09 11:40:24', 
+ 'game_id': '20222', 
+ 'bet': 30, 
+ 'win': 0, 
+ 'win_loss': -30, 
+ 'bet_info': 'bet', 
'jackpot_info': None, 
'bet_id': '6810769E-8AF9-4CD6-8B11-63C56FE5134D', 
'is_bet': 1, 
'finish': 1, 
'freespin': 0, 
'matrix': [['4', '5', '6', '1', '1'], ['3', '2', '3', '10', '7'], ['0', '1', '2', '3', '4']], 
'win_lines': [], 
'sign': 'aa0f8d4faa9f28ef08318c6db177703b'}
'''
# tbs loss
'''
{'cmd': 'writeBet',
 'hall': '11307908', 
 'key': 'KglP5yOPES314XLdyTkDIgWiZ4edNMNi', 
+ 'sessionId': '7363353', 
+ 'login': 'abbd878b-9171-4954-b0d0-6e633583ffe8', 
+ 'tradeId': '77394286_5080237273_1670585675290_16629719994', 
+ 'bet': '0.25', 
+ 'win': '0', 
 'action': 'SpinNormal', 
+ 'winLose': -0.25, 
+ 'betInfo': 'SpinNormal', 
+ 'date': '2022-12-09 11:34:35', 
 'matrix': 'MQKFA;JAIM1;1B1JF;', 
+ 'gameId': '1555', 
 'WinLines': ''}
 '''


class WriteBetSchema(pydantic.BaseModel):
    """WriteBetSchema"""

    login: str
    bet_date: datetime.datetime
    bet: decimal.Decimal
    win: decimal.Decimal
    win_loss: decimal.Decimal
    bet_info: str  # or our enum
    game_id: int
    session_id: str  # str | int
    trade_id: str
