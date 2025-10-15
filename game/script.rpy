# Определение персонажей игры.
define Ymiko = Character('Юмико', color="#c8ffc8",what_slow_cps=70)
define Rin = Character('Рин', color="#c8ffc8",what_slow_cps=70)
define Hitomi = Character('Хитоми', color="#ffffff",what_slow_cps=70)

# Создаем персонажа игрока с временным именем
default player_name = "Игрок"
define Player = Character('[player_name]', color="#c8ffc8", what_slow_cps=70)

#Создание статов
default ymiko_love = 0 #Любовь Юмико

# Старт игры
label start:
    $ player_name = renpy.input("Как тебя зовут?", length=15, exclude="{}[]#@*") or "Игрок" 

    Player "Где я?"
    Ymiko "Ты в игре!"
    call park_location #Вызываю локацию Парк  
    Player "Отлично! Работа организована!"
    Ymiko "Приятно познакомиться, [player_name]!"
    call scene1_Player_in_room_story1
    call scene2_Hitomi_and_Player
    return