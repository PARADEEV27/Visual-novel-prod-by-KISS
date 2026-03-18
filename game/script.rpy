### Обозначения: #########################################################################################

    ### - Блоки разделения кода
    ## - Коментарий
    # - закоментировать (отключить\включить часть кода)

### Игра - "Поэт" ########################################################################################

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

### Музыка и звуки. ######################################################################################

define audio.winter = "audio/winter_wind.ogg"
define audio.ambient_home = "audio/home_quiet.ogg"
define audio.step = "audio/footstep_snow.ogg"
define audio.pen = "audio/pen_scrape.ogg"
define audio.door = "audio/door_open.ogg"
define audio.bell = "audio/school_bell.ogg"
define audio.page_turn = "audio/page_turn.ogg"
define audio.clock = "audio/clock_tick.ogg"
define audio.heartbeat = "audio/heartbeat.ogg"

### Фоны локаций. ########################################################################################

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

### Персонаж #############################################################################################

image ars = "images/ars.png" 

### Счётчики настроения ##################################################################################

default inspiration = 0
default meditative = 0
default passionate = 0
default doubt = 0

### Переменные для статистики ############################################################################

default total_choices = 0
default poems_written = 0

### Экран статистики #####################################################################################

screen inspiration_meter():
    frame:
        xalign 1.0 yalign 0.02
        xmargin 10 ymargin 10
        background Solid("#222222cc")
        padding (10, 5)
        vbox:
            text "Вдохновение: [inspiration]" color "#f5d742" size 20 bold True
            text "Выборов: [total_choices]" color "#aaaaaa" size 16

### Экран для внутренних монологов (NVL режим) ###########################################################

init python:
    config.nvl_list_length = 20
    ## Не менять значение!! ↑

### Старт игры ###########################################################################################

label start:
    # Инициализация
    $ renpy.music.set_volume(0.3, delay=0, channel='music')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    
    # Интерфейс
    show screen inspiration_meter
    
    # Начало игры
    scene bg black with dissolve
    play music winter loop volume 0.2
    
    autor "Осень. Зима. Весна. Лето."
    autor "Времени нет, когда ты молод."
    autor "Есть только моменты. Один из них..."
    
    scene bg classroom with dissolve
    play sound bell volume 0.3
    pause 1.0

    ### СЦЕНА 1: Урок литературы #########################################################################

    label scene_classroom:
        scene bg classroom
        show ars at center with dissolve
        
        teacher "Итак, Арсений, что ты можешь сказать о стихотворении «Пророк»?"
        
        a "Я... я думаю, что это не просто о поэте. Это о человеке, который обрёл голос."
        
        teacher "Интересная мысль. Развивай."
        
        inner "Зачем она меня спросила? В классе 30 человек, а спросила именно меня."
        inner "Может, я слишком громко вздохнул, когда она читала?"
        inner "Или она видит что-то, чего не видят другие?"
        
        a "Поэт проходит через мучительное преображение. Ему открывается и небо, и земля."
        a "Но главное — он получает «жало мудрыя змеи». То есть способность видеть суть."
        
        teacher "Молодец, хорошее замечание, пятёрка"
        
        a "Спасибо, Марья Ивановна." 
        
        inner "Пятёрка. Смешно. Разве можно оценивать откровение цифрами?"
        inner "Пушкин писал это не для оценок. Он писал кровью сердца."
        
        play sound page_turn
        autor "Звенит звонок. Класс наполняется шумом."
        
        classmate "Слышь, Арсений, ты чё такой умный?"
        
        a "Я просто..." 
        
        classmate "Да ладно, шучу. Пошли на улицу?"
        
        menu:
            "Что ответить?"
            
            "Пойдём. Надо проветриться.":
                $ inspiration += 1
                $ total_choices += 1
                a "Да, идём. Голова кругом."  
                inner "Обычные разговоры. Обычные люди. А во мне всё бурлит."
                
            "Нет, я посижу ещё.":
                $ meditative += 1
                $ total_choices += 1
                a "Иди, я догоню. Хочу записать кое-что." 
                inner "Слова улетят, если не записать их сейчас."

### СЦЕНА 2: Выход из школы ##############################################################################

label scene_exit:
    scene bg street_day with dissolve
    play sound step loop volume 0.4
    
    autor "Холодный воздух ударяет в голову, прогоняя школьный дурман."
    
    show ars at left with dissolve
    
    inner "Небо высокое, серое, тяжёлое. Как будто давит на город."
    inner "Дома стоят плечом к плечу, жмутся друг к другу. Им холодно?"
    inner "Глупости. Домам не бывает холодно. Или бывает?"
    
    autor "Мимо проходят люди. Много людей."
    
    inner "Вот женщина с сумками. Тяжело идёт. Домой спешит, к семье."
    inner "Вот старик с газетой. Остановился, читает. Мир рушится, а он читает."
    inner "Вот влюблённые. Держатся за руки, смеются. Не замечают ничего."
    
    menu:
        "О чём думать?"
        
        "О будущем.":
            $ passionate += 1
            $ total_choices += 1
            inner "Что ждёт их всех? Что ждёт меня? Университет, работа, пенсия?"
            inner "Неужели вся жизнь — это просто прямая линия от рождения до смерти?"
            
        "О настоящем.":
            $ meditative += 1
            $ total_choices += 1
            inner "Они живут сейчас. Прямо в этот момент. И я живу."
            inner "Этот холод, этот ветер, этот серый свет — это и есть жизнь."


### Временый мусор #######################################################################################

#$ player_name = renpy.input("Как тебя зовут?", length=15, exclude='''{}[]#@*1234567890-=+_!№;%:?/$ ^&\'~`.,()"''') or "Игрок"
#$ player_name = player_name.capitalize() 
