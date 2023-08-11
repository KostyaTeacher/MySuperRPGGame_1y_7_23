import math
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMessageBox
from PyQt6.QtCore import QTimer
import sys  # Тільки для доступу до аргументів командного рядка
import random as r
import winsound


from superRPGGame_Main import Ui_Dialog
from fightgui import Ui_Dialog_fight
from shopgui import Ui_Dialog_shop



# Додатку потрібен один (і лише один) екземпляр QApplication.
# Передаємо sys.argv, щоб дозволити аргументи командного рядка для програми.

# Секція для Змінних__________
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

step = 0
score = 0
TIMER_INTERVAL = 2000
hero_hp = 200
SCORE_FOR_KILL = 300
HP_DIAPOSON = math.ceil(hero_hp / 5)
HERO_HP_MAX = hero_hp



info = hero_bd.get("Warrior")

events_bd = ["shop", "shop", "nothing", "nothing", "nothing", "enemy", "enemy", "enemy", "enemy", "enemy"]
r.shuffle(events_bd)

enemy_events=["Spyder", "Spyder", "Spyder", "Spyder", "Spyder", "Skeleton", "Skeleton", "Zombie", "Vampire", "Demon"]
r.shuffle(enemy_events)



# Секція для функцій__________
def tick():  # цей метод викликаться кожну секунду з таймеру
    global step
    hero_unlock()
    generator_events()

def timer_start():
    timer.start(TIMER_INTERVAL)

def timer_pause():
    timer.stop()

def hero_unlock():
    global score
    #score = score + 1000 #щоб перевірити що все працуюе
    if score >= 1000:
        ui.btn_hero4.setEnabled(True)
    if score >= 3000:
        ui.btn_hero2.setEnabled(True)
    if score >= 5000:
        ui.btn_hero3.setEnabled(True)

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

def generator_events():
    global step
    global events_bd
    events = r.choice(events_bd)
    if events == "nothing":
        ui.label_info.setText(f"Крок {step}. Нічого не відбувається")
    if events == "shop":
        ui.label_info.setText(f"Крок {step}. Ви зустріли магазин")
        shop()
    if events == "enemy":
        fight()
    step = step + 1

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
    global score
    global hero_hp
    enemy_info = enemy_bd.get(enemy)

    hero_damage = info["damage_phys"] + info["damage_mag"]

    enemy_damage_phys = enemy_info["damage_phys"] - (enemy_info["damage_phys"] * info["defend_phys"])
    enemy_damage_mag = enemy_info["damage_mag"] - (enemy_info["damage_mag"] * info["defend_mag"])
    enemy_damage = int(enemy_damage_mag + enemy_damage_phys)
    enemy_hp = enemy_hp - hero_damage
    filename = "../assets/fight.wav"
    winsound.PlaySound(filename, winsound.SND_FILENAME)
    hero_hp = hero_hp - enemy_damage
    hero_hp_show_down()

    ui1.label_info_battle1.setText(f"Ви б'єте ворога і, наносите йому {hero_damage} шкоди")
    ui1.label_info_battle2.setText(f"{enemy_info['class']} б'є вас і, завдає {enemy_damage} шкоди")

    if enemy_hp <= 0:
        ui1.label_info_battle3.setText(f"У ворога {enemy_info['class']} залишилося 0 hp")
        msgBox = QMessageBox()
        msgBox.setText("Ви перемогли ворога. Вітаємо")
        msgBox.exec()
        ui1.btn_fight.setEnabled(False)
        ui1.btn_fightOK.setEnabled(True)
        score = score + SCORE_FOR_KILL
        ui.lcdNumber.display(str(score))
    else:
        ui1.label_info_battle3.setText(f"У ворога {enemy_info['class']} залишилося {enemy_hp} hp")


    if hero_hp <=0:
        msgBox = QMessageBox()
        msgBox.setText(f"Нажаль ви програли "
                       f"Ви набрали {score} балів "
                       f"Ви перемогли {int(score/SCORE_FOR_KILL)} ворогів")
        msgBox.exec()
        fight_window.close()
        window.close()



def buton_run():
    run = r.randint(1, 100)
    msgBox = QMessageBox()
    if run > 40:
        msgBox.setText("Вам вдалося втекти")
        msgBox.exec()
        fight_window.hide()
        timer.start(TIMER_INTERVAL)
    else:
        msgBox.setText("Нажаль вам не вдалося втектии")
        msgBox.exec()
        ui1.btn_run.setEnabled(False)


def buton_fightOK():
    fight_window.hide()
    timer.start(TIMER_INTERVAL)
    ui1.label_info_battle1.setText("Ініціалізація")
    ui1.label_info_battle2.setText("")
    ui1.label_info_battle3.setText("")
    ui1.btn_fight.setEnabled(True)
    ui1.btn_run.setEnabled(True)
    ui1.btn_fightOK.setEnabled(False)

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


def shop():
    timer.stop()
    check_shop()
    shop_window.show()

def check_shop():
    global score
    global hero_hp



    if score < 1000:
        ui2.btn_shopLife.setEnabled(False)
    if score < 2000:
        ui2.btn_shopAtack.setEnabled(False)
    if score >= 1000:
        ui2.btn_shopLife.setEnabled(True)
    if score >= 2000:
        ui2.btn_shopAtack.setEnabled(True)

    if hero_hp >= HERO_HP_MAX:
        hero_hp == HERO_HP_MAX
        ui2.btn_shopLife.setEnabled(False)



def buton_shopOK():
    shop_window.hide()
    timer.start(TIMER_INTERVAL)


def buy_life():
    global hero_hp
    global score
    score = score - 1000
    hero_hp = hero_hp + HP_DIAPOSON
    ui.lcdNumber.display(str(score))
    check_shop()
    hero_hp_show_up()


def buy_attack():
    global info
    global score
    info["damage_phys"] = info["damage_phys"] + 20
    info["damage_mag"] = info["damage_mag"] + 20
    score = score - 2000
    ui.lcdNumber.display(str(score))
    check_shop()
    ui.label_heroInfo.setText(f"Ваш клас: {info['class']}. Атака фізична - {info['damage_phys']} Магічна - {info['damage_mag']}")





# Секція для коду__________
app = QApplication(sys.argv)

# Створюємо віджет Qt – вікно.
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
window.show()


fight_window = QDialog()
ui1 = Ui_Dialog_fight()
ui1.setupUi(fight_window)

shop_window = QDialog()
ui2 = Ui_Dialog_shop()
ui2.setupUi(shop_window)




timer = QTimer()  # таймер для того щоб кожну секунду відбувалася якась рандомна подія
timer.timeout.connect(tick)

ui.btn_start.clicked.connect(timer_start)

ui.btn_pause.clicked.connect(timer_pause)

ui.btn_hero1.clicked.connect(hero1_click)

ui.btn_hero2.clicked.connect(hero2_click)

ui.btn_hero3.clicked.connect(hero3_click)

ui.btn_hero4.clicked.connect(hero4_click)

ui1.btn_fightOK.clicked.connect(buton_fightOK)

ui1.btn_fight.clicked.connect(buton_fight)

ui1.btn_run.clicked.connect(buton_run)

ui2.btn_shopOK.clicked.connect(buton_shopOK)

ui2.btn_shopLife.clicked.connect(buy_life)

ui2.btn_shopAtack.clicked.connect(buy_attack)

# Кінець секції для коду__________

# Запускаємо цикл подій.
app.exec()
