from game_log_parser import GameLogParser, XgamesGameLogParser, TBSGameLogParser
from schemas import GameLogProviderEnum, GameLogTypeEnum


class GameLogParseF:
    def __init__(
        self,
        provider: GameLogProviderEnum,
        log_type: GameLogTypeEnum,
        payload: str
    ):
        self.provider = provider
        self.log_type = log_type
        self.payload = payload

    def get_parser(self) -> GameLogParser:
        match self.provider:
            case GameLogProviderEnum.xgames:
                return XgamesGameLogParser(self.log_type, self.payload)
            case GameLogProviderEnum.tbs:
                return TBSGameLogParser(self.log_type, self.payload)
            case _:
                raise


if __name__ == '__main__':
    print('xgames')
    parser = GameLogParseF(
        GameLogProviderEnum.xgames,
        GameLogTypeEnum.get_balance,
        payload='{"cmd":"getbalance","server":"stage_test","hall":"44434343","login":"sdsddsdsd","sessionid":"edaf919617bfdbe60955f1707f4c968e0585d55e","currency":"USD","sign":"842444f39317fe20440aa4251616be28"}'
    ).get_parser()
    print(parser.get_balance())
    print('tbs')
    parser_tbs = GameLogParseF(
        GameLogProviderEnum.tbs,
        GameLogTypeEnum.get_balance,
        payload='{"status": "success", "login": "abbd878b-9171-4954-b0d0-6e633583ffe8", "balance": "43", "hall": 11307908,"currency": "EUR", "sign": "110433438b3f84c2a85d9b09fe055cc5"}'
    ).get_parser()
    print(parser_tbs.get_balance())
