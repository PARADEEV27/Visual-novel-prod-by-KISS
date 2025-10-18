### Обозначения: #########################################################################
    ### - Блоки разделения кода
    ## - Коментарий
    # - закоментировать (отключить\включить часть кода)


### Определение персонажей игры. #########################################################
define Ymiko = Character('Юмико', color="#c8ffc8",what_slow_cps=70)
## Пресонаж: Юмико ↑
define Rin = Character('Рин', color="#c8ffc8",what_slow_cps=70)
## Пресонаж: Рин ↑
define Hitomi = Character('Хитоми', color="#ffffff",what_slow_cps=70)
## Пресонаж: Хитоми ↑

### Создаем персонажа игрока с временным именем
default player_name = "Игрок"
define Player = Character('[player_name]', color="#c8ffc8", what_slow_cps=70)
## Пресонаж: Игрок ↑

### Текстуры персонажей ##################################################################
# image Ymiko happy = im.Scale("Ymiko happy.png", 540, 1111)
# image Ymiko sleep = im.Scale("Ymiko sleep.png", 540, 1111)
image Hitomi = im.Scale("hitomi_base.png", 540, 1111)
## Текстура - Хитоми (База) ↑

### Плавные появления героев #############################################################
label show_hitomi_base:
    show Hitomi:
        alpha 0.0
        xalign 0.5
        parallel:
            ease 0.5 alpha 1.0
    return
## Появление - Хитоми (База) ↑

### Текстуры локаций #####################################################################
image bg park = im.Scale("i.jfif", 1920, 1080) 
## Фон локации Парк ↑

### Музыка локаций #######################################################################
# define audio.park_music = "---"
## Музыка локации Парк ↑

### Комбинирование элементов локаций #####################################################
label park_location: #Создаю локацию Парк
    scene bg park
    # play music park_music
    return
## Сцена парка с музыкой ↑

### Создание статов ######################################################################
default persistent.player_clicked_no_in_save_event = False
## Событие Игрок нажал на копку "НЕТ" в сохранении ↑

### Старт игры ###########################################################################
label start:
    $ player_name = renpy.input("Как тебя зовут?", length=15, exclude='''{}[]#@*1234567890-=+_!№;%:?/$ ^&\'~`.,()"''') or "Игрок"
    $ player_name = player_name.capitalize() 
    Player "Где я?"
    call show_hitomi_base
    Ymiko "Ты в игре!"
    call park_location ## Вызываю локацию Парк  
    call scene1_Player_in_room_story1
    call scene2_Hitomi_and_Player
    Player "persistent.player_clicked_no_in_save_event (Нажал нет) = [persistent.player_clicked_no_in_save_event]"