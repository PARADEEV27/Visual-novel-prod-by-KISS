### Обозначения: #########################################################################################
### - Блоки разделения кода
## - Коментарий
# - закоментировать (отключить\включить часть кода)

### Игра - "Поэт" ########################################################################################

define config.developer = True
define config.name = "Поэт"
define config.version = "Alpha" 

### Определение персонажей игры. (Инициализация) #########################################################

define a = Character("[player_name]", color="#c8ffc8", who_outlines=[(1, "#0a5e0a")], image="ars", what_size=45)
define inner = Character(None, what_color="#9c9c9c", what_size=45, what_italic=True,)
define autor = Character(None, what_color="#cccccc", what_size=45)
define voice = Character("Катя", color="#c86464", who_outlines=[(1, "#5e0a0a")], what_size=45)
define teacher = Character("Марья Ивановна", color="#b41844", what_size=45)
define classmate = Character("Одноклассник", color="#ffaa64", what_size=45)
define stranger = Character("Незнакомец", color="#d464ff", what_size=45)

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
define audio.tear = "audio/paper_tear.ogg"

### Фоны локаций. ########################################################################################

image bg classroom = im.Scale("images/bg_classroom.PNG", 1920, 1080)
image bg classroom_dusk =  im.Scale("images/bg_classroom.PNG", 1920, 1080)
image bg street_day = im.Scale("images/bg_street_day.PNG", 1920, 1080)
image bg street_dusk = im.Scale("images/bg_street_dusk.PNG", 1920, 1080)
image bg street_night =  im.Scale("images/bg_street_night.PNG", 1920, 1080)
image bg park =  im.Scale("images/bg_park.PNG", 1920, 1080)
image bg home_hall =  im.Scale("images/bg_home_hall.JPG", 1920, 1080)
image bg home_room =  im.Scale("images/bg_home_room.PNG", 1920, 1080)
image bg window_view =  im.Scale("images/bg_window_view.PNG", 1920, 1080)
image bg desk =  im.Scale("images/bg_desk.JPG", 1920, 1080)
image bg desk_night =  im.Scale("images/bg_desk_night.PNG", 1920, 1080)
image Marya = im.Scale("images/Marya.PNG", 1180, 1480)
image Katya = im.Scale("images/Katya.PNG", 1080, 1480)
image bg black = "#000000"
image bg white = "#ffffff"
# image ars = "images/ars.png" 

### Счётчики настроения ##################################################################################

default inspiration = 0 ## вдохновение
default meditative = 0 ## созерцание
default passionate = 0 ## страсть
default doubt = 0 ## сомнение

### Переменные для статистики ############################################################################

default total_choices = 0 ## Выбор
default poems_written = 0 ##
default player_name = "" ##
default poem_text = "" ##
default final_poem_quality = 0 # Вычисления в конце

### Экран статистики #####################################################################################
screen inspiration_meter():
    frame:
        xalign 1.0 yalign 0.02
        xmargin 10 ymargin 10
        background Solid("#222222cc")
        padding (10, 5)
        vbox:
            text "Вдохновение: [inspiration]" color "#f5d742" size 20 bold True
            text "Созерцание: [meditative]" color "#42aaf5" size 18
            text "Страсть: [passionate]" color "#f54242" size 18
            text "Сомнение: [doubt]" color "#3cca08" size 18
            text "Выборов: [total_choices]" color "#aaaaaa" size 16

### Экран для внутренних монологов (NVL режим) ###########################################################

init python:
    config.nvl_list_length = 20
    
    # Функция для вычисления концовки на основе очков
    def calculate_ending():
        global final_poem_quality
        # Качество стиха зависит от баланса вдохновения и сомнений, плюс бонус за написанные стихи
        raw_score = (inspiration * 2) + meditative + passionate - (doubt * 0.5)
        final_poem_quality = max(0, int(raw_score + (poems_written * 5)))
        return final_poem_quality

    # Функция для генерации стихотворения в зависимости от пути игрока
    def generate_poem():
        global poem_text
        ## вдохновение > cозерцание и вдохновение > страсть
        if inspiration > meditative and inspiration > passionate:
            poem_text = """
Я слышу мир через шелест страниц,
Сквозь гулкие своды и пение птиц.
Мне слово дано как ожог и как свет,
Ведь другого оружия у поэта и нет."""
            return "Вдохновенный стих"
            ## созерцание > вдохновение и созерцание > страсть
        elif meditative > inspiration and meditative > passionate:
            poem_text = """
Шлепки шагов, промокших насквозь кед.
Отражённый в луже, танцует фары свет.
Ручей бежит рекой вдоль тратуара,
Под одним зонтом гуляет рядом пара"""
            return "Созерцательный стих"
            ## страсть > вдохновение и страсть > созерцание
        elif passionate > inspiration and passionate > meditative:
            poem_text = """
Нет любви?! Ты что несёшь?!
Я же чувствую что врёшь!
Да, бывает тяжело однако,
Но это ведь совсем не знаки!"""
            return "Страстный стих"
            ## Сомнение > максимального(вдохновение, страсть, созерцание)
        elif doubt > max(inspiration, passionate, meditative):
            poem_text = """
Мне страшно порой быть настоящим,
Правда блеснёт и сыграет в ящик.
Строго по линии правил плетясь,
Споткнулся, громко падая в грязь."""
            return "Стих сомнений"
        else:
            poem_text = """
Мой каждый шрам, как строчка в книге,
Это момент судьбы застывший в миге,
Шрам хранит в себе души огонь,
Воспоминаний страшных громкий рой."""
            return "Обычный стих"

### Старт игры ###########################################################################################

label start:
    ## Инициализация
    $ renpy.music.set_volume(0.3, delay=0, channel='music')
    $ renpy.music.set_volume(0.5, delay=0, channel='sound')
    
    ## Ввод имени
    $ player_name = renpy.input("Как тебя зовут?", length = 15, default="Макс", exclude='''{}[]#@*1234567890-=+_!№;%:?/$ ^&\'~`.,()"''') 
    $ player_name = player_name.strip().capitalize()
    ## ВАЖНО! я не могу исправить баг с пустым именем.

    ## Интерфейс
    show screen inspiration_meter
    
    ## Начало игры
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
        pause 0.02
        scene bg classroom with hpunch
        show Marya with dissolve:
            xalign 0.75
            yalign -0.5
            
        teacher "Отвечает - [player_name]. "
        teacher "Расскажи нам о стихотворении «Пророк»? Как ты его понял? "

        a "Я... Я думаю «Пророк» не просто о поэте. Это о человеке, который обрёл голос."
        
        teacher "Интересная мысль. Развивай."
        
        a "Поэт проходит через мучительное преображение. Ему открывается и небо, и земля."
        a "Но главное — он получает «жало мудрыя змеи». То есть способность видеть суть."

        inner "Зачем она меня спросила? В классе 30 человек, а спросила именно меня."
        inner "Может, я слишком громко вздохнул, когда она читала?"
        inner "Или она видит что-то, чего не видят другие?"

        teacher "Молодец, хорошее замечание, пятёрка"
        
        a "Спасибо, Марья Ивановна." 
        
        inner "Пятёрка. Смешно. Разве можно оценивать откровение цифрами?"
        inner "Пушкин писал это не для оценок. Он писал кровью сердца."
        
        play sound page_turn
        hide Marya with dissolve
        autor "*Звенит звонок. Класс наполняется шумом.*"
        
        classmate "Слышь, [player_name], ты чё реально эту фигню читал?"
        
        a "Я просто..." 
        
        classmate "Да ладно, забей. Пошли на улицу прогуляемся?"
        
        menu:
            autor "Что ответить однокласнику?"
            
            "Пойдём. Надо проветриться.":
                $ inspiration += 1
                $ total_choices += 1
                a "Да, идём. Голова уже кругом."  
                inner "Обычные разговоры. Обычные люди. А во мне всё бурлит."
                jump scene_exit_alone
                
            "Не, я посижу ещё 5 минут.":
                $ meditative += 1
                $ total_choices += 1
                a "Иди, я догоню. Хочу записать кое-что пока не забыл." 
                inner "Слова улетят, если не записать их сейчас."
                jump scene_write_first

### СЦЕНА 2.1: Попытка записать стихи #####################################################################
label scene_write_first:
    play sound pen loop
    
    autor "Ты достаёшь потрепанный блокнот. Страницы пахнут пылью и надеждой."
    
    menu:
        autor "О чем писать?"
        
        "О тишине в классе.":
            $ meditative += 2
            $ poems_written += 1
            
            inner "Парты пусты. Мел крошится в тишине. Скрип половиц."
            inner "«И пустота звенит во мне набатом, напоминая, что я здесь чужой»."
            
            jump scene_exit_school
            
        "О крике внутри.":
            $ passionate += 2
            $ poems_written += 1
            
            inner "Надоело! Надоело быть правильным. Глаголом жечь? Да я сам сгорю!"
            inner "«Я разорву шаблон унылых фраз, пусть лучше хаос, чем молчание сейчас»."
            
            jump scene_exit_school

### СЦЕНА 3: Выход из школы (общий путь) ##################################################################

label scene_exit_school:
    scene bg street_day with dissolve
    play sound step loop volume 0.4
    
    autor "Ты выходишь на крыльцо. Холодный воздух отрезвляет после духоты класса."
    
    jump scene_meeting

label scene_exit_alone:
    scene bg street_day with dissolve
    play sound step loop volume 0.4
    
    autor "Холодный воздух ударяет в голову, прогоняя школьный дурман."
    
    inner "Небо высокое, серое, тяжёлое. Как будто давит на город."
    inner "Дома стоят плечом к плечу, жмутся друг к другу. Им холодно?"
    inner "Глупости. Домам не бывает холодно. Или бывает?"
    
    autor "Мимо проходят люди. Много людей."

    inner "Вот женщина с сумками. Тяжело идёт. Домой спешит, к семье."
    inner "Вот старик с газетой. Остановился, читает. Мир рушится, а он читает."
    inner "Вот влюблённые. Держатся за руки, смеются. Не замечают ничего."
    
    menu:
        autor "О чём думать?"
        
        "О будущем.":
            $ passionate += 1
            $ total_choices += 1
            
            inner "Что ждёт их всех? Что ждёт меня? Университет, работа, пенсия?"
            inner "Неужели вся жизнь — это просто прямая линия от рождения до смерти?"
            
            jump scene_meeting
            
        "О настоящем.":
            $ meditative += 1
            $ total_choices += 1
            
            inner "Они живут сейчас. Прямо в этот момент. И я живу."
            inner "Этот холод, этот ветер, этот серый свет — это и есть жизнь."
            
            jump scene_meeting

### СЦЕНА 4: Встреча с одноклассницей #####################################################################
label scene_meeting:
    
    
    show Katya with hpunch:
        xalign 0.75
        yalign -0.4
    
    autor "*Из холодного воздуха, слегка испугав героя, появляется Катя — одноклассница, с которой они сидят через ряд.*"
    
    voice "Ты чего пялишься на прохожих?"
    
    a "Привет, Кать, да я не пялюсь, просто вдохновляюсь видами" 
    
    voice "Как знаешь. Ты там в классе книгу забыл какую-то, я решила догнать тебя и вернуть"
    
    autor "*Сказала Катя протягивая забытую книгу*"
   
    a "Ой спасибо большое, вот я растяпа" 
    
    voice "Не могла не заметить, что в книге очень много заметок, какие-то ямбы, хореи и всякие ударения"
    
    a "Да, есть там такое"
    
    inner "Боже, она видела мои каракули..."
    inner "Надеюсь, не увидела наброски моего стиха на форзаце..."

    autor "*Катя ехидно улыбнулась и зачитала те самые строчки*"
    
    voice "Иду по границе негодующих лиц \nИ владений судьбы, тех что я принц..."
    
    autor "*Герой засмущался*"
    
    voice "Твоё творение? Давно стихи писать начал?"
    
    menu:
        autor "Признаться?"
        
        "Ну... да.":
            $ inspiration += 1
            $ total_choices += 1
            
            a "Ну... да. Иногда записываю мысли."
            
            voice "Не плохо! А почитаешь как-нибудь? Это правда интересно."
            
            a "Может быть если нравится."
            
            inner "Она попросила почитать... Кто-то всерьез заинтересовался моими каракулями?"
            
        "Да нет, это не мое.":
            $ doubt += 1
            $ total_choices += 1
            
            a "Да нет, это не мое. Так, ручку расписал."
            
            voice "А, ну ладно, тогда я пойду, до завтра!"
            
            autor "Катя пожимает плечами и убегает."
            
            inner "Врать легко. Врать себе — ещё легче. Но почему так тоскливо?"
    
    jump scene_park

### СЦЕНА 5: Парк #########################################################################################
label scene_park:
    scene bg street_day with dissolve
    play ambient winter fadein 2.0
    
    autor "Ты сворачиваешь в парк. Деревья стоят голые, чёрные на фоне серого неба."
    
    inner "Зимой парк всегда пуст, находится тут даже жутко, но так завораживает"
    
    autor "На скамейке сидит незнакомый пожилой мужчина в старом пальто. И что-то читает."
    
    menu:
        autor "Что делать?"
        
        "Пройти мимо.":
            $ meditative += 1
            
            inner "Не стоит мешать. Чтение — это интимный процесс. Как молитва."
            
            jump scene_home
            
        "Подойти, спросить что читает.":
            $ inspiration += 2
            $ total_choices += 1
            
            a "Извините... что читаете?"
            
            stranger "Оруэлла. «1984». А ты, юноша, видимо, тоже ценитель слов на бумаге?"
            
            a "Немного совсем, чего грех таить?"
            
            stranger "Взгляд у тебя — ищущий. Смотришь на мир не как все. Другой бы и не заметил меня даже"
            
            a "Интересная книга то?"
            
            stranger "Интересная, но рано тебе ещё в антиутопию погружаться"
            
            autor "*Незнакомец ухмыльнулся и опустил взгляд обратно в книгу.*"
            
            inner "Что-ж взгляд — ищущий, интересно..."

            jump scene_home

### СЦЕНА 6: Дом ##########################################################################################
label scene_home:
    scene bg home_hall with dissolve
    play sound door
    stop sound
    play music ambient_home loop volume 0.2
    
    autor "Дома тихо. Родители ещё на работе."
    
    inner "Квартира пуста. Можно дышать полной грудью. Можно быть собой."
    
    scene bg desk_night with dissolve
    play sound clock loop
    
    autor "Твоя комната. Твой стол. Твоя тетрадь."
    
    menu:
        autor "Чем заняться вечером?"
        
        "Писать, пока есть настроение.":
            $ passionate += 2
            $ poems_written += 1
            $ total_choices += 1
            play sound pen loop
            
            autor "Ручка скользит по бумаге, оставляя чернильный след."
            
            inner "Строчки рождаются одна за другой. Это как наваждение."
            
            
            jump scene_night
            
        "Лечь на кровать и смотреть в потолок.":
            $ meditative += 2
            $ total_choices += 1
            
            autor "Белый потолок. Трещина в углу. Пятно от воды над люстрой."
            
            inner "Карта неизведанной страны. Континенты штукатурки, океаны побелки."
            
            autor "Мысли текут медленно, лениво. День заканчивается."
            
            jump scene_night

### СЦЕНА 7: Ночь и решение ###############################################################################
label scene_night:
    scene bg black with dissolve
    "..."
    scene bg desk_night with dissolve
    play music winter loop volume 0.1
    stop sound
    play sound clock
    
    autor "Час пролетел незаметно. На столе — исписанный лист."
    autor "Ночь опускается на город. За окном фонари рисуют жёлтые круги на снегу."
    
    inner "Завтра в школу. Опять этот бесконечный круг."
    inner "Но что-то изменилось во мне за этот день. Или только начинает меняться?"
    
    play sound heartbeat loop volume 0.3
    
    autor "В тишине ночи ты слышишь стук собственного сердца. Или это пульс вселенной?"
    
    menu:
        autor "Главный вопрос этого вечера:"
        
        "Я хочу писать, несмотря ни на что.":
            $ inspiration += 3
            $ passionate += 2
            $ total_choices += 1
            $ poems_written += 1
            
            autor "Ты садишься за стол. Рука сама тянется к ручке."
            autor "Ты пишешь то, что чувствуешь здесь и сейчас."
            
            jump ending
            
        "Может, это всё глупости? Подростковые фантазии.":
            $ doubt += 3
            $ total_choices += 1
            play sound tear
            autor "Ты берёшь исписанный лист. Хочется скомкать и выбросить."
            menu:
                autor "Выбросить или оставить?"
                "Выбросить.":
                    $ doubt += 2
                    
                    autor "Бумажный комок летит в корзину. Глухо ударяется о дно."
                    
                    inner "Вот и всё. Нет поэта. Есть школьник [player_name]."
                
                "Оставить.":
                    $ meditative += 2
                    
                    autor "Ты аккуратно складываешь лист и убираешь в ящик стола."
                   
                    inner "Не сейчас. Но, может быть, потом."
            
            jump ending

### КОНЦОВКИ ##############################################################################################
label ending:
    stop music fadeout 2.0
    stop sound
    scene bg black with dissolve
    pause 1.0
    
    # Итоговый результат
    $ poem_name = generate_poem()
    $ final_score = calculate_ending()
    
    show text "Несколько лет спустя..." with dissolve
    pause 2.0
    hide text with dissolve
    
    # Логика определения концовки
    if inspiration >= 5 and doubt < 3:
        jump ending_true_poet
    elif passionate >= 5 and doubt < 4:
        jump ending_rebel
    elif meditative >= 5 and doubt < 5:
        jump ending_philosopher
    elif doubt >= 6:
        jump ending_silence
    else:
        jump ending_common

label ending_true_poet:
    scene bg desk with dissolve
    
    autor "Ты стоишь на сцене маленького литературного кафе."
    autor "В руках — сборник. Твой сборник. Пахнет типографской краской."
    
    show text "[poem_text]" at truecenter with dissolve
    pause 7.0
    hide text with dissolve
    
    autor "Зал аплодирует. Кто-то просит автограф."
    autor "Ты вспоминаешь тот зимний день в школе. Слова Марьи Ивановны. Разговор с незнакомцем в парке."
    
    inner "Я обрел голос. Я стал тем, кем должен был стать."
    
    autor "Путь был долгим. Но стихи стоили каждой бессонной ночи."
    
    jump credits

label ending_rebel:
    scene bg street_night with dissolve
   
    autor "Ты стал голосом поколения. Твои стихи печатают на заборах, их цитируют на митингах."
    autor "Они острые, как бритва. Они жгут глаголом."
    
    show text "[poem_text]" at truecenter with dissolve
    pause 7.0
    hide text with dissolve
    
    autor "Но иногда, глядя в зеркало, ты видишь не поэта. Ты видишь оратора. Бунтаря."
    
    inner "Я хотел просто писать. А получилось — кричать."
    
    autor "Может, в этом и есть моя правда."
    
    jump credits

label ending_philosopher:
    scene bg street_day with dissolve
    
    autor "Ты пишешь в стол. Редко публикуешься. Твои стихи сложны, полны метафор и отсылок."
    autor "Их понимают единицы. Но те, кто понимают, — становятся твоими друзьями на всю жизнь."
    
    show text "[poem_text]" at truecenter with dissolve
    pause 7.0
    hide text with dissolve
    
    autor "Ты нашел гармонию в созерцании. Тишина перестала пугать, она стала холстом."
    
    inner "Я слышу, как растет трава. Я слышу, как падает снег. Этого достаточно."
    
    jump credits

label ending_silence:
    scene bg home_hall with dissolve
    
    autor "Блокнот пылится на дальней полке. Ты выбрал другую дорогу. Стабильную, понятную, обычную."
    autor "Офис, дом, телевизор."
    
    autor "Но однажды ночью ты просыпаешься от строки, которая пришла во сне."
    autor "Ты не записываешь её."
    autor "Утром ты её уже не помнишь. Только щемящее чувство потери."
    
    inner "Иногда я думаю: а что, если бы тогда, в тот зимний вечер, я не выбросил листок?"
    
    jump credits

label ending_common:
    scene bg classroom_dusk with dissolve
    
    autor "Жизнь идет своим чередом. Ты окончил школу, поступил в институт."
    autor "Иногда что-то пишешь в заметках телефона. Друзьям нравится, но дальше лайков дело не идет."
    
    show text "[poem_text]" at truecenter with dissolve
    pause 7.0
    hide text with dissolve
    
    autor "Ты не стал великим поэтом. Но ты стал человеком, который умеет видеть красоту в обыденном."
    autor "Разве этого мало?"
    
    jump credits

label credits:
    scene bg black with dissolve
    pause 1.0
    
    show text "СПАСИБО ЗА ИГРУ!" with dissolve
    pause 2.0
    
    ## Вывод статистики в конце
    $ renpy.say(None, "Статистика прохождения:\nВдохновение: [inspiration], Созерцание: [meditative], Страсть: [passionate], Сомнения: [doubt]\nНаписано стихов: [poems_written]")
    
    ## Возврат в меню
    return
