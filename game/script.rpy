# Определение персонажей игры.
define Ymiko = Character('Юмико', color="#c8ffc8",what_slow_cps=70)
define Player = Character('Игрок', color="#c8ffc8",what_slow_cps=70)
define Rin = Character('Игрок', color="#c8ffc8",what_slow_cps=70)



#Создание статов
default ymiko_love = 0 #Любовь Юмико

# Старт игры
label start:
    Player "Где я?"
    Ymiko "Ты в игре!"
    call park_location #Вызываю локацию Парк  
    call scene1_Player_in_room_story1
    Player "Отлично! Работа организована!"
    $ player_name = renpy.input("Как тебя зовут?", length=15, exclude="{}[]#@*") or "Игрок"
    Ymiko "Приятно познакомиться, [player_name]!"
    return