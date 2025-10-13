#Текстуры локаций
image bg park = im.Scale("i.jfif", 1920, 1080) #Фон локации Парк

#Текстуры персонажей
# image Ymiko happy = im.Scale("Ymiko happy.png", 540, 1111)
# image Ymiko sleep = im.Scale("Ymiko sleep.png", 540, 1111)

#Музыка локаций
# define audio.park_music = "---"

#Комбинирование элементов локаций
label park_location: #Создаю локацию Парк
    scene bg park
    # play music park_music

label scene1_in_room_location: #Создаю локацию Комната
    scene bg park
