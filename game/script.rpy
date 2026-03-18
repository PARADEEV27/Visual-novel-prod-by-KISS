### Обозначения: #########################################################################
    ### - Блоки разделения кода
    ## - Коментарий
    # - закоментировать (отключить\включить часть кода)

### Игра - "Поэт"

define config.developer = True
define config.name = "Отражение"
define config.version = "1.0" 
## Убрать позже в другой файл ↑

### Определение персонажей игры. (Инициализация) #########################################################
define a = Character("Арсений", color="#c8ffc8", who_outlines=[(1, "#0a5e0a")], image="ars", what_size=35)
define inner = Character(None, what_color="#767676", what_size=35, what_italic=True)
define autor = Character(None, what_color="#cccccc", what_size=35)
define voice = Character("Катя", color="#c86464", who_outlines=[(1, "#5e0a0a")], what_size=35)
define teacher = Character("Марья Ивановна", color="#64c8ff", what_size=35)
define classmate = Character("Одноклассник", color="#ffaa64", what_size=35)

### Музыка и звуки. #################################################
define audio.winter = "audio/winter_wind.ogg"
define audio.ambient_home = "audio/home_quiet.ogg"
define audio.step = "audio/footstep_snow.ogg"
define audio.pen = "audio/pen_scrape.ogg"
define audio.door = "audio/door_open.ogg"
define audio.bell = "audio/school_bell.ogg"
define audio.page_turn = "audio/page_turn.ogg"
define audio.clock = "audio/clock_tick.ogg"
define audio.heartbeat = "audio/heartbeat.ogg"

### Фоны локаций.
image bg classroom = im.Scale("images/bg_classroom.jpg", 1950, 1550)
image bg classroom_dusk = "images/bg_classroom_dusk.jpg"
image bg street_day = im.Scale("images/bg_street_day.jpg", 2200, 1300)
image bg street_dusk = im.Scale("images/bg_street_dusk.jpg", 1732, 1400)
image bg street_night = "images/bg_street_night.jpg"
image bg park = "images/bg_park.jpg"
image bg home_hall = "images/bg_home_hall.jpg"
image bg home_room = "images/bg_home_room.jpg"
image bg window_view = "images/bg_window_view.jpg"
image bg desk = "images/bg_desk.jpg"
image bg desk_night = "images/bg_desk_night.jpg"
image bg black = "#000000"
image bg white = "#ffffff"

### Персонаж ###
image ars = "images/ars.png" 

### Счётчики настроения ###
default inspiration = 0
default meditative = 0
default passionate = 0
default doubt = 0

### Переменные для статистики ###
default total_choices = 0
default poems_written = 0

### Экран статистики ###
screen inspiration_meter():
    frame:
        xalign 1.0 yalign 0.02
        xmargin 10 ymargin 10
        background Solid("#222222cc")
        padding (10, 5)
        vbox:
            text "Вдохновение: [inspiration]" color "#f5d742" size 20 bold True
            text "Выборов: [total_choices]" color "#aaaaaa" size 16

### Экран для внутренних монологов (NVL режим) ###
init python:
    config.nvl_list_length = 20
    ## Не менять значение!! ↑



### Плавные появления героев #############################################################
label show_SPACE:
    show SPACE:
        alpha 0.0
        xalign 0.5
        parallel:
            ease 0.5 alpha 1.0
    "Где-то там... за этой стопкой непрочитанных формуляров... вращаются галактики. Пыль на корешках энциклопедий — та же звездная пыль, осевшая на полках вечности. Каждое слово, напечатанное в этих книгах, — чей-то застывший крик или шепот в бездну."
    "Мы придумали богов, чтобы не чувствовать себя такими... маленькими. А потом придумали науку, чтобы доказать, что богов нет, и почувствовать себя еще более одинокими. Забавно."
    "(Глубокий, неровный вдох.)"
    "Человек... этот странный сгуток белков и тревоги. Он строит города, пишет симфонии, расщепляет атом, но до сих пор не знает, что делать с собственной тоской в воскресный вечер."
    "Мы ищем смысл в хронологии событий, выстраивая даты и эпохи, как солдатиков на линейке. А время просто течет сквозь пальцы. Как песок. Как читатели, которые берут книгу и никогда не возвращают."
    "(Легкое движение плеч, будто от холода.)"
    "А что, если вся наша история — лишь краткое примечание на полях чьей-то огромной, ненаписанной книги? Если Вселенной плевать на наши войны, наши открытия и нашу любовь? Если мы просто... случайный сбой программы в бесконечном коде?"
    "Страшно? Нет. Странным образом, в этом есть покой. Если мы сами выбираем, чему придавать значение, значит, и тишина за окном, и этот старый библиотечный запах — и есть настоящая реальность. Больше ничего не нужно. Просто быть. Смотреть, как пылинки танцуют в луче света, и знать..."
    return
## Плавный вызов локации SPACE ↑

### Текстуры локаций #####################################################################
image bg TABLELOC = im.Scale("TABLEBOOK.jpg", 1920, 1080) 
## Фон локации Стола ↑
image bg LIBRARY = im.Scale("LIBRARY.jpg", 1920, 1080) 
## Фон локации Лестницы в библиотеке ↑


### Музыка локаций #######################################################################
# define audio.park_music = "---"

## Музыка локации Парк ↑
define audio.void_music = "Литвин.mp3"
define audio.SPACE_music = "main-menu-theme.mp3"

### Комбинирование элементов локаций #####################################################
label TABLELOC: #Создаю локацию TABLELOC
    scene bg TABLELOC
    "(Громкий, резкий звонок будильника на телефоне. Тело дергается, подскакивает на стуле.)"
    "...что это, черт возьми, перерыв закончился!"
    "(Протирает глаза, смотрит на открытую книгу перед собой.)"
    "Ох... Галактики, говоришь? Смысл бытия? (Кривится, хватаясь за затекшую шею.) Спину бы теперь не потерять в этой вечной борьбе с высокими стеллажами. Так, стопка книг на возврат, забытый читательский билет под ноутбуком..." 
    "Пойду, расставлю. Жизнь продолжается. Кто-то же должен наводить порядок в этом вашем мироздании."
    return
## Сцена окончания перерыва в библиотеке ↑
label LIBRARY: #Создаю локацию LIBRARY
    scene bg LIBRARY
    return
## Сцена лестницы (Пока пустая)↑


### Создание статов ######################################################################
default persistent.player_clicked_no_in_save_event = False
## Событие Игрок нажал на копку "НЕТ" в сохранении ↑

### Старт игры ###########################################################################
label start:
    stop music
    play sound void_music


    "(Голова медленно сползает с ладони, лоб касается столешницы. Тишина. Слышно только тиканье часов и гудение ламп дневного света.)"
    play music SPACE_music
    call show_SPACE
    stop music
    call TABLELOC ## Вызываю локацию стол
    call LIBRARY
    "fwefe"
    return

### Временый мусор #######################################################################

#$ player_name = renpy.input("Как тебя зовут?", length=15, exclude='''{}[]#@*1234567890-=+_!№;%:?/$ ^&\'~`.,()"''') or "Игрок"
#$ player_name = player_name.capitalize() 
