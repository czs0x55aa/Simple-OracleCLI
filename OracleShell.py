# coding=utf8
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.token import Token
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.styles import style_from_dict

from CMDUtils import Parser, Executor
from OracleUtils import DBInstance


style = style_from_dict({
    Token.Toolbar: '#ffffff bg:#333333',
})

bottom_tip = 'bottom tip.'
def get_bottom_toolbar_tokens(cli):
    return [(Token.Toolbar, bottom_tip)]

word_completer = WordCompleter(['find', 'cd', 'select'])

def main():
    print ('Welcome.')
    mem_history = InMemoryHistory()
    parser = Parser()
    db_connect = DBInstance(dump=True)
    executor = Executor(db_connect)
    while True:
        input_cmd = prompt(u'>>> ', history=mem_history,
                        get_bottom_toolbar_tokens=get_bottom_toolbar_tokens,
                        auto_suggest=AutoSuggestFromHistory(),
                        style=style,
                        completer=word_completer)
        exe_config, msg = parser.resolve(input_cmd)
        if exe_config is not None:
            executor.execute(exe_config)
        else:
            print (msg)
            break

if __name__ == '__main__':
    main()
