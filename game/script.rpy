### Обозначения:
    ### - Блоки разделения кода
    ## - Коментарий
    # - закоментировать (отключить\включить часть кода)


### Определение персонажей игры.
define Ymiko = Character('Юмико', color="#c8ffc8",what_slow_cps=70)
define Rin = Character('Рин', color="#c8ffc8",what_slow_cps=70)
define Hitomi = Character('Хитоми', color="#ffffff",what_slow_cps=70)

### Создаем персонажа игрока с временным именем
default player_name = "Игрок"
define Player = Character('[player_name]', color="#c8ffc8", what_slow_cps=70)

### Текстуры персонажей
# image Ymiko happy = im.Scale("Ymiko happy.png", 540, 1111)
# image Ymiko sleep = im.Scale("Ymiko sleep.png", 540, 1111)

### Плавные появления героев
label show_hitomi_base:
    show Hitomi:
        alpha 0.0
        xalign 0.5
        parallel:
            ease 1.0 alpha 1.0
    return

### Текстуры локаций
image bg park = im.Scale("i.jfif", 1920, 1080) #Фон локации Парк
image Hitomi = im.Scale("hitomi_base.png", 540, 1111)

### Музыка локаций
# define audio.park_music = "---"

### Комбинирование элементов локаций
label park_location: #Создаю локацию Парк
    scene bg park
    # play music park_music
    return
### Создание статов
default ymiko_love = 0 ## Любовь Юмико

### Старт игры
label start:
    $ player_name = renpy.input("Как тебя зовут?", length=15, exclude="{}[]#@*1234567890-=+_!№;%:?/$ ^&\~`.,()") or "Игрок"
    $ player_name = player_name.capitalize() 
    Player "Где я?"
    call show_hitomi_base
    Ymiko "Ты в игре!"
    call park_location ## Вызываю локацию Парк  
    Player "Отлично! Работа организована!"
    Ymiko "Приятно познакомиться, [player_name]!"
    call scene1_Player_in_room_story1
    call scene2_Hitomi_and_Player
    return