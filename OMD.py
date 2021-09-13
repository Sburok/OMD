def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Буря налетела, утка еле уцелела.\n'
          'Ветер утку подхватил, прямо в море утащил.\n'
          'Утка было испугалась, но как спастись догадалась.\n'
          'Зонтик лодкой послужил, утке отдых придал сил.\n'
          'Утка с духом собралась и до дома добралась.')


def step2_no_umbrella():
    print('Буря налетела, утка еле уцелела.\n'
          'Ветер утку подхватил, прямо в море утащил.\n'
          'Утка очень испугалась, на теченье полагалась.\n'
          'Прошли три ночи и три дня, на остров утка приплыла.\n'
          'Остров был необитаем, утке приключенья обещаяя.')


if __name__ == '__main__':
    step1()