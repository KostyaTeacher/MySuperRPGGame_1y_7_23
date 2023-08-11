Герой


Здоров'я
healths
Тип атаки и величина damage
phys/mag
Захист
defend phys/mag
Розблокування
Воїн (англ. Warrior)
 
 
 
 
100
Ф 30
80% / 0%


Паладин (англ. Paladin)
Ф 50
50% / 20%
1000
Маг (англ. Magician)
Ф 5
М 100
0% / 80%
3000
Шаман (англ. Shaman)
Ф 50
М 50
50% /50%
5000


Вирогідність збіжати з бою - 60% 
Вирогідність зустрити магазин - 20%
Вирогідність зустрити ворога - 50%
Вирогідність зустрити нічого - 30%

Атака збілщується на 20 і коштує 2000
Здоровья +50 і коштує 1000

Ворог
Enemy
Здоров'я
Health
Тип атаки и величина damage
Частота зустрічі
Павук (Spyder)
30
 Ф 10
50%
Скелет (Skeleton)
50
 Ф 20
20%
Зомбі (Zombie)
100
Ф30
М10 
10%
Вампир (Vampire)
150
Ф40
М20 
10%
Демон (Demon)
200
М50 
Ф50
10%

Для встановлення:
pip install pyqt6
pip install pyqt-tools

Скачуемо софт:
https://build-system.fman.io/qt-designer-download

Робимо потрібну форму в QTDesigner (QDIalog) і зберігаємо у теку проєкту
Не забути виставити мін і макс розмірі щоб вікно не можно було змінювати

Конвертуємо її у файл пайтону
В консолі пишемо:
pyuic6 testgame.ui -o testgame.py

Додаємо імпорт:
from testgame import Ui_Dialog



Далі прописуємо базу:

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMessageBox
from  PyQt6.QtCore import QTimer
from superRPGGame_Main import Ui_Dialog

import sys # Тільки для доступу до аргументів командного рядка

# Додатку потрібен один (і лише один) екземпляр QApplication.
# Передаємо sys.argv, щоб дозволити аргументи командного рядка для програми.

#Секція для Змінних__________

#Секція для функцій__________

def tick(): #цей метод викликаться кожну секунду з таймеру
    pass


#Секція для коду__________
app = QApplication(sys.argv)

# Створюємо віджет Qt – вікно.
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
window.show()

timer = QTimer() #таймер для того щоб кожну секунду відбувалася якась рандомна подія
timer.timeout.connect(tick)


#Кінець секції для коду__________

# Запускаємо цикл подій.
app.exec()


Додаємо базу даних про героїв та ворогів
hero_bd = {
    "Warrior": {
        "class":"Воїн",
        "healths": 100,
        "damage_phys": 30,
        "damage_mag": 0,
        "defend_phys": 0.8,
        "defend_mag": 0
    },
    "Paladin": {
        "class":"Паладін",
        "healths": 100,
        "damage_phys": 50,
        "damage_mag": 0,
        "defend_phys": 0.5,
        "defend_mag": 0.2
    },
    "Magician": {
        "class":"Маг",
        "healths": 100,
        "damage_phys": 5,
        "damage_mag": 100,
        "defend_phys": 0,
        "defend_mag": 0.8
    },
    "Shaman": {
        "class":"Шаман",
        "healths": 100,
        "damage_phys": 50,
        "damage_mag": 50,
        "defend_phys": 0.5,
        "defend_mag": 0.5
    }
}

enemy_bd = {
    "Spyder": {
    "class":"Павук",
        "healths": 30,
        "damage_phys": 10,
        "damage_mag": 0,
    },
    "Skeleton": {
        "class":"Скелет",
        "healths": 50,
        "damage_phys": 20,
        "damage_mag": 0,
    },
    "Zombie": {
    "class":"Зомбі",
        "healths": 100,
        "damage_phys": 30,
        "damage_mag": 10,
    },
    "Vampire": {
    "class":"Вампір",
        "healths": 150,
        "damage_phys": 40,
        "damage_mag": 20,
    },
    "Demon": {
        "class":"Демон",
        "healths": 200,
        "damage_phys": 50,
        "damage_mag": 50,
    },
}




Додаємо работу для кнопок старт и пауза
step = 1

def tick(): #цей метод викликаться кожну секунду з таймеру
    global step
    step = step + 1
    ui.label_info.setText(f"Крок {step}. Нічого не відбувається")

def timer_start():
    timer.start(1000)

def timer_pause():
    timer.stop()


ui.btn_start.clicked.connect(timer_start)

ui.btn_pause.clicked.connect(timer_pause)


Додаємо розблокування героїв, для цього нама потрібно знати скільке вже очків у гравця

score = 0


def hero_unlock():
    global score
    score = score + 500 #щоб перевірити що все працую
    if score >= 1000:
        ui.btn_hero4.setEnabled(True)
    if score >= 3000:
        ui.btn_hero2.setEnabled(True)
    if score >= 5000:
        ui.btn_hero3.setEnabled(True)

и додаємо виклик ціє функцій у функцію tick
def tick(): #цей метод викликаться кожну секунду з таймеру
    global step
    hero_unlock()
    step = step + 1
    ui.label_info.setText(f"Крок {step}. Нічого не відбувається")



Додаємо зміну інфи про обраного персонажа
info = hero_bd.get("Warrior") #ініціалізуємо значення за замовченням, після створення бд

ui.btn_hero1.clicked.connect(hero1_click)

ui.btn_hero2.clicked.connect(hero2_click)

ui.btn_hero3.clicked.connect(hero3_click)

ui.btn_hero4.clicked.connect(hero4_click)

def hero1_click():
    global info
    info = hero_bd.get("Warrior")
    ui.label_heroInfo.setText(f"Ваш клас: {info['class']}. Атака фізична - {info['damage_phys']} Магічна - {info['damage_mag']}")

def hero2_click():
    global info
    info = hero_bd.get("Magician")
    ui.label_heroInfo.setText(f"Ваш клас: {info['class']}. Атака фізична - {info['damage_phys']} Магічна - {info['damage_mag']}")

def hero3_click():
    global info
    info = hero_bd.get("Shaman")
    ui.label_heroInfo.setText(f"Ваш клас: {info['class']}. Атака фізична - {info['damage_phys']} Магічна - {info['damage_mag']}")

def hero4_click():
    global info
    info = hero_bd.get("Paladin")
    ui.label_heroInfo.setText(f"Ваш клас: {info['class']}. Атака фізична - {info['damage_phys']} Магічна - {info['damage_mag']}")


Починаємо генерувати рандомні події:
Спочатку робимо геренацію подій - ворог чи магазин чи нічого
choice

import random as r

events_bd = ["shop", "shop", "nothing", "nothing", "nothing", "enemy", "enemy", "enemy", "enemy", "enemy"]
r.shuffle(events_bd)

def generator_events():
    global step
    global events_bd
    events = r.choice(events_bd)
    if events == "nothing":
        ui.label_info.setText(f"Крок {step}. Нічого не відбувається")
    if events == "shop":
        ui.label_info.setText(f"Крок {step}. Ви зустріли магазин")
    if events == "enemy":
        ui.label_info.setText(f"Крок {step}. Ви зустріли ворога")
    step = step + 1
Змінюємо функцію tick

def tick(): #цей метод викликаться кожну секунду з таймеру
    hero_unlock()
    generator_events()




Реалізовуємо битву. Виводимо вікно битви і додаємо функцію Fight

from fightgui import Ui_Dialog_fight


fight_window = QDialog()
ui1 = Ui_Dialog_fight()
ui1.setupUi(fight_window)


def generator_events():
    global step
    global events_bd
    events = r.choice(events_bd)
    print(events)
    if events == "nothing":
        ui.label_info.setText(f"Крок {step}. Нічого не відбувається")
    if events == "shop":
        ui.label_info.setText(f"Крок {step}. Ви зустріли магазин")
    if events == "enemy":
        fight()
    step = step + 1

enemy_events=["Spyder", "Spyder", "Spyder", "Spyder", "Spyder", "Skeleton", "Skeleton", "Zombie", "Vampire", "Demon"]

r.shuffle(enemy_events)

def fight():
    global enemy_bd
    ui.label_info.setText(f"Крок {step}. Ви зустріли ворога")
    enemy = r.choice(enemy_events)
    enemy_info = enemy_bd.get(enemy)
    timer.stop()
    ui1.label_welcome1.setText(f"Ви зустріли ворога {enemy_info['class']}")
    fight_window.show()
Пішемо основну логіку бою
Додаємо реакцію на кнопку ОК
ui1.btn_fightOK.clicked.connect(buton_fightOK)

def buton_fightOK():
    fight_window.hide()
    timer.start(2000)


Підключаємо кнопки битися і бігти 
def buton_fight():
    ui1.label_info_battle1.setText("Fight")

def buton_run():
    ui1.label_info_battle1.setText("Run")

ui1.btn_fight.clicked.connect(buton_fight)

ui1.btn_run.clicked.connect(buton_run)

Пишемо метод buton_run бо він простіший

def buton_run():
    run = r.randint(1, 100)
    if run > 40:
        msgBox = QMessageBox()
        msgBox.setText("Вам вдалося втекти")
        msgBox.exec()
        fight_window.hide()
        timer.start(2000)
    else:
        msgBox = QMessageBox()
        msgBox.setText("Нажаль вам не вдалося втектии")
        msgBox.exec()
        ui1.btn_run.setEnabled(False)

Змінюємо інтервал таймеру на константу

TIMER_INTERVAL = 2000

def timer_start():
    timer.start(TIMER_INTERVAL)


Пишемо код бою

hero_hp = 200

def buton_fight():
     print(enemy)

І бачимо що вілітає з помілкою

Робимо зміну enemy глобальною щоб ми могли використовувати її в різних функціях

Дописуємо global enemy і enemy_hp у функції fight() і def buton_fight()

Помилка зникла

Текст:
Ви б'єте ворога і, наносите йому 125 шкоди
Скелет б'є вас і, завдає 100 шкоди
У ворога Скелет залишилося 1000 hp


def fight():
    global enemy_bd
    global enemy    
    global enemy_hp
    ui.label_info.setText(f"Крок {step}. Ви зустріли ворога")
    enemy = r.choice(enemy_events)
    enemy_info = enemy_bd.get(enemy)
    timer.stop()
    ui1.label_welcome1.setText(f"Ви зустріли ворога {enemy_info['class']}")
    enemy_hp = enemy_info["healths"]
    fight_window.show()

def buton_fight():
    global enemy
    global info
    global enemy_hp
    enemy_info = enemy_bd.get(enemy)


    hero_damage = info["damage_phys"] + info["damage_mag"]

    enemy_damage_phys = enemy_info["damage_phys"] - (enemy_info["damage_phys"] * info["defend_phys"])
    enemy_damage_mag = enemy_info["damage_mag"] - (enemy_info["damage_mag"] * info["defend_mag"])
    enemy_damage = int(enemy_damage_mag + enemy_damage_phys)
    enemy_hp = enemy_hp - hero_damage

    ui1.label_info_battle1.setText(f"Ви б'єте ворога і, наносите йому {hero_damage} шкоди")
    ui1.label_info_battle2.setText(f"{enemy_info['class']} б'є вас і, завдає {enemy_damage} шкоди")
    ui1.label_info_battle3.setText(f"У ворога {enemy_info['class']} залишилося {enemy_hp} hp")

На цьому этапі все ниби працює але ми бачимо що коли вікно відкривається заново то там старі дані, це буде потрібно також виправити у кінці.

Робимо розблокування кнопки ОК після перемоги, діалогове вікно і блокування кнопки битися

def buton_fight():
    global enemy
    global info
    global hero_hp
    global enemy_hp
    enemy_info = enemy_bd.get(enemy)


    hero_damage = info["damage_phys"] + info["damage_mag"]

    enemy_damage_phys = enemy_info["damage_phys"] - (enemy_info["damage_phys"] * info["defend_phys"])
    enemy_damage_mag = enemy_info["damage_mag"] - (enemy_info["damage_mag"] * info["defend_mag"])
    enemy_damage = int(enemy_damage_mag + enemy_damage_phys)
    enemy_hp = enemy_hp - hero_damage




    ui1.label_info_battle1.setText(f"Ви б'єте ворога і, наносите йому {hero_damage} шкоди")
    ui1.label_info_battle2.setText(f"{enemy_info['class']} б'є вас і, завдає {enemy_damage} шкоди")

    if enemy_hp <= 0:
        ui1.label_info_battle3.setText(f"У ворога {enemy_info['class']} залишилося 0 hp")
        msgBox = QMessageBox()
        msgBox.setText("Ви перемогли ворога. Вітаємо")
        msgBox.exec()
        ui1.btn_fight.setEnabled(False)
        ui1.btn_fightOK.setEnabled(True)
    else:
        ui1.label_info_battle3.setText(f"У ворога {enemy_info['class']} залишилося {enemy_hp} hp")

Теперь робимо щоб вікно відновлювало свій стан, тобто повератємо усе в первиний стан, це робимо після того як буде нажата кнопка ОК

def buton_fightOK():
    fight_window.hide()
    timer.start(TIMER_INTERVAL)
    ui1.label_info_battle1.setText("Ініціалізація")
    ui1.label_info_battle2.setText("")
    ui1.label_info_battle3.setText("")
    ui1.btn_fight.setEnabled(True)
    ui1.btn_run.setEnabled(True)
    ui1.btn_fightOK.setEnabled(False)


Все працує, але бачимо що поки наш герой безсмертний
Фіксимо це

Додаємо кінець гри



    if hero_hp <=0:
        msgBox = QMessageBox()
        msgBox.setText(f"Нажаль ви програли "
                       f"Ви набрали {score} балів "
                       f"Ви перемогли {int(score/SCORE_FOR_KILL)} ворогів")
        msgBox.exec()
        fight_window.close()
        window.close()


Додаємо очки за вбівство

SCORE_FOR_KILL = 300

def buton_fight():
global score 

   if enemy_hp <= 0:
        ui1.label_info_battle3.setText(f"У ворога {enemy_info['class']} залишилося 0 hp")
        msgBox = QMessageBox()
        msgBox.setText("Ви перемогли ворога. Вітаємо")
        msgBox.exec()
        ui1.btn_fight.setEnabled(False)
        ui1.btn_fightOK.setEnabled(True)
        score = score + SCORE_FOR_KILL
        ui.lcdNumber.display(str(score))


Робимо героя смертним

hero_hp = hero_hp - enemy_damage
print(hero_hp)

Робимо функцію відображення хп

hero_hp = hero_hp - enemy_damage
    hero_hp_show_down()

Додаємо зверху константу
HP_DIAPOSON = math.ceil(hero_hp / 5)


def hero_hp_show_down():
    global hero_hp
    if hero_hp <= HP_DIAPOSON * 4:
        ui.hearts5.hide()
    if hero_hp <= HP_DIAPOSON * 3:
        ui.hearts4.hide()
    if hero_hp <= HP_DIAPOSON * 2:
        ui.hearts3.hide()
    if hero_hp <= HP_DIAPOSON:
        ui.hearts2.hide()
    if hero_hp <= 0:
        ui.hearts1.hide()

Залишилось реалізувати магазин

from shopgui import Ui_Dialog_shop

shop_window = QDialog()
ui2 = Ui_Dialog_shop()
ui2.setupUi(shop_window)

Переходимо у наш generator_events()
і дописуємо

shop()

Реалізуємо цей метод

def shop():
    timer.stop()
    check_shop()
    shop_window.show()

def check_shop():
    global score
    if score < 1000:
        ui2.btn_shopLife.setEnabled(False)
    if score < 2000:
        ui2.btn_shopAtack.setEnabled(False)
    if score >= 1000:
        ui2.btn_shopLife.setEnabled(True)
    if score >= 2000:
        ui2.btn_shopAtack.setEnabled(True)

Реалізуємо кнопку ОК

def buton_shopOK():
    shop_window.hide()
    timer.start(TIMER_INTERVAL)

ui2.btn_shopOK.clicked.connect(buton_shopOK)


Реалізовуємо кнопки купити

ui2.btn_shopLife.clicked.connect(buy_life)

ui2.btn_shopAtack.clicked.connect(buy_attack)

def buy_attack():
    global info
    global score
    info["damage_phys"] = info["damage_phys"] + 20
    info["damage_mag"] = info["damage_mag"] + 20
    score = score - 2000
    ui.lcdNumber.display(str(score))
    check_shop()
    ui.label_heroInfo.setText(f"Ваш клас: {info['class']}. Атака фізична - {info['damage_phys']} Магічна - {info['damage_mag']}")

створюємо констатнут де збірігається максимальне ХП
HERO_HP_MAX = hero_hp

в check_shop дописуємо
global hero_hp

   if hero_hp >= HERO_HP_MAX:
        hero_hp == HERO_HP_MAX
        ui2.btn_shopLife.setEnabled(False)

def buy_life():
    global hero_hp
    global score
    score = score - 1000
    hero_hp = hero_hp + HP_DIAPOSON
    ui.lcdNumber.display(str(score))
    check_shop()
    hero_hp_show_up()

Реалізуємо hero_hp_show_up()

def hero_hp_show_up():
    if hero_hp >= 1:
        ui.hearts1.show()
    if hero_hp >= HP_DIAPOSON:
        ui.hearts2.show()
    if hero_hp >= HP_DIAPOSON * 2:
        ui.hearts3.show()
    if hero_hp >= HP_DIAPOSON * 3:
        ui.hearts4.show()
    if hero_hp >= HP_DIAPOSON * 4:
        ui.hearts5.show()


Здаєтьсу усе
Що можно додати:
Різну кількість балів за різніх монстрів
Блокування кнопок старт і пауза колі відкрито інше вікно
Окремий єкран кінця гри зі статистикою
Різне хп у кожного героя
Більше різних ворогів
Зробити більш класний баланс
Зробити щоб урон був не стабільний а у межах диапозону типу 50-80
Зробити критичний удар з деякою вирогідністью наприклад 5 або 10%
Зробити рандомну генерацию додаткових подій, наприклад ви знайшли золото або потрапили у лаву
Зробити щоб коли купляєшь атаку збільшувалась лише приорітетна атака - у воїна і паладина тільки фізічна, у мага - магічна, у шамана обидві бо він імба і всі хочуть бути шаманом-королем (https://www.youtube.com/watch?v=Z5tPJhaK71A)
Додати якусь умови повної пермоги у грі
Можливість використовувати зілля лікуваня (додаткова кнопка)
Генрацію рандомного літературного тексту при зустрічі кожного монстра, наприклад “Герой прокрадається скрізь ліс, і раптово на нього стрибає Скелет”
Ну і усе на ваш розсуд


https://drive.google.com/drive/folders/1BZSVdHd3mXqHbmI3jneWnJex48nc4k-i?usp=sharing

