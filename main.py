from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name, char_class) -> str:
    '''Функция рассчитывает урон, наносимый персонажем,
    использует модуль рандом для рассчетов.'''
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(5, 10)}')
    return (f'{char_name} нанёс урон противнику '
            f'равный {5 + randint(-3, -1)}')


def defence(char_name, char_class) -> str:
    '''Функция расчитывает кол-во заблокированного урона,
    использует модуль рандом для расчетов.'''
    if char_class == 'warrior':
        return (f'{char_name} блокировал '
                f'{10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал '
                f'{10 + randint(-2, 2)} урона')
    return (f'{char_name} блокировал '
            f'{10 + randint(2, 5)} урона')


def special(char_name, char_class) -> str:
    '''Функция возвращает строку, описывающую специальное умение,
    которое зависит от класса персонажа: воин - выносливость,
    маг - атака, хил - защита. Количество поинтов спец умений
    использует модуль рандом для расчетов'''
    if char_class == 'warrior':
        return (f'{char_name} применил специальное '
                f'умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное '
                f'умение «Атака {5 + 40}»')
    return (f'{char_name} применил специальное '
            f'умение «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    '''Функция запускает тренировку, где можно выбрать один из
    типов взаимодействия: атака, защита или спец умение. Тренировку
    можно пропустить.'''
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — '
              'отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — '
              'превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, '
              'способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать '
          'противника, defence — чтобы блокировать атаку '
          'противника или special — чтобы '
          'использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    '''Функция позволяет выбрать класс персонажа.'''
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, '
                           'Маг — mage, '
                           'Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
            break
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
            break
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
            break
        if (
            char_class != 'warrior' and
            char_class != 'mage' and
            char_class != 'healer'
        ):
            print('Класс недоступен')
            continue
    approve_choice = input('Нажми (Y), чтобы подтвердить '
                           'выбор, или любую другую кнопку, '
                           'чтобы выбрать другого '
                           'персонажа ').lower()
    return str(char_class)


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
