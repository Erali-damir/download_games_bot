import telebot
from telebot import types

# токен-бота
bot = telebot.TeleBot('1450714949:AAEpi0mcjPQZjh6MD0VDgBOwaTYNKrJJrQs')

# если / help, / start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте!"
                    + message.from_user.first_name
                    + ", в боте можно скачивать разные игры по жанрам.",
                    reply_markup=markup_menu)


markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_1 = types.KeyboardButton('Стрелялки')
btn_2 = types.KeyboardButton('Аркады')
btn_3 = types.KeyboardButton('Игры на двоих')
markup_menu.add(btn_1, btn_2, btn_3)

Game1 = types.ReplyKeyboardMarkup (resize_keyboard=True, row_width=2)
btn_a1 = types.KeyboardButton('Special Forces Group 2')
btn_a2 = types.KeyboardButton('Modern Ops')
btn_a3 = types.KeyboardButton('Sniper 3D')
btn_a4 = types.KeyboardButton('Code of War')
btn_a5 = types.KeyboardButton('Striker Zone')
btn_a6 = types.KeyboardButton('В меню')
Game1.add(btn_a1, btn_a2, btn_a3, btn_a4, btn_a5, btn_a6)

Game2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a7 = types.KeyboardButton('Sonic Dash')
btn_a8 = types.KeyboardButton('Hungry Shark Evolution')
btn_a9 = types.KeyboardButton('Кухонная Лихорадка')
btn_a10 = types.KeyboardButton('Кирпичный выключатель поиск')
btn_a11 = types.KeyboardButton('Gun Fu: Stickman 2')
btn_a12 = types.KeyboardButton('В меню')
Game2.add(btn_a7, btn_a8, btn_a9, btn_a10, btn_a11, btn_a12)

Game3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a13 = types.KeyboardButton('Игры на двоих троих 4 игрока')
btn_a14 = types.KeyboardButton('Stickman Party')
btn_a15 = types.KeyboardButton('Cubic 2 3 4 Игроки Игры')
btn_a16 = types.KeyboardButton('Two guys & Zombies')
btn_a17 = types.KeyboardButton('BGC: 2 3 4 игрока')
btn_a18 = types.KeyboardButton('В меню')
Game3.add(btn_a13, btn_a14, btn_a15, btn_a16, btn_a17, btn_a18)

vmenyu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_naz5 = types.KeyboardButton('В меню')
vmenyu.add(btn_naz5)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "В меню":
        bot.reply_to(message, "Назад", reply_markup=markup_menu)
    if message.text == "Стрелялки":
        bot.reply_to(message, "Выберите игру", reply_markup=Game1)
    if message.text == "Аркады":
        bot.reply_to(message, "Выберите игру", reply_markup=Game2)
    if message.text == "Игры на двоих":
        bot.reply_to(message, "Выберите игру", reply_markup=Game3)
    if message.text == "Special Forces Group 2":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.ForgeGames.SpecialForcesGroup2&hl=ru&gl=US""", reply_markup=Game1)
    if message.text == "Modern Ops":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.edkongames.mobs&hl=ru&gl=US""", reply_markup=Game1)
    if message.text == "Sniper 3D":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.fungames.sniper3d&hl=ru&gl=US""", reply_markup=Game1)
    if message.text == "Code of War":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.extremedevelopers.codeofwar&hl=ru&gl=US""", reply_markup=Game1)
    if message.text == "Striker Zone":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.extremedevelopers.strikerzone&hl=ru&gl=US""", reply_markup=Game1)
    if message.text == "Sonic Dash":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.sega.sonicdash&hl=ru&gl=US""", reply_markup=Game2)
    if message.text == "Hungry Shark Evolution":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.fgol.HungrySharkEvolution&hl=ru&gl=US""", reply_markup=Game2)
    if message.text == "Кухонная Лихорадка":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.nordcurrent.canteenhd&hl=ru&gl=US""", reply_markup=Game2)
    if message.text == "Кирпичный выключатель поиск":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.mobirix.swipebrick2&hl=ru&gl=US""", reply_markup=Game2)
    if message.text == "Gun Fu: Stickman 2":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.dobsoftstudios.gunfustickman2&hl=ru&gl=US""", reply_markup=Game2)
    if message.text == "Игры на двоих троих 4 игрока":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.ction.playergames&hl=ru&gl=US""", reply_markup=Game3)
    if message.text == "Stickman Party":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.PlayMax.playergames&hl=ru&gl=US""", reply_markup=Game3)
    if message.text == "Cubic 2 3 4 Игроки Игры":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.CubeCubeSports.Cubic234PlayerGames&hl=ru&gl=US""", reply_markup=Game3)
    if message.text == "Two guys & Zombies":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.yad.twoguysandzombieshotseat&hl=ru&gl=US""", reply_markup=Game3)
    if message.text == "BGC: 2 3 4 игрока":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=com.arqew.bgc&hl=ru&gl=US""", reply_markup=Game3)
bot.polling()
