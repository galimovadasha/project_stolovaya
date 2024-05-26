import telebot
import uuid
from telebot import types
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

orders = []
pending_orders = {}

@bot.message_handler(commands=['start'])
def message_reply(message):
    global price, products
    products[str(message.chat.id)] = []
    price[str(message.chat.id)] = 0 
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Салаты', callback_data = 'salads')
    button2 = types.InlineKeyboardButton('Супы', callback_data = 'soups')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Мясо', callback_data = 'meat')
    button4 = types.InlineKeyboardButton('Гарниры', callback_data = 'second dishes')
    markup.row(button3, button4)
    buttton5 = types.InlineKeyboardButton('Выпечка', callback_data = 'bakers')
    button6 = types.InlineKeyboardButton('Напитки', callback_data = 'drinks')
    markup.row(buttton5, button6)
    if len(message.text.split()) > 1:
        param = message.text.split()[1]
        global pending_orders, orders
        succesful_order = pending_orders[param] 
        del pending_orders[param]
        orders.append(succesful_order)
        code = randint(1000, 10000)
        bot.send_message(message.chat.id, f'Ваш заказ успешно оплачен!\nКод для получения заказа: {code}')
        bot.send_message(-1002050298201, f'Заказ {code}: \n{", ".join(succesful_order[0])} - {succesful_order[1]}р.')    
    else:
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Выберите из предложенного:".format(message.from_user), reply_markup = markup)


def vybor_salads():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Цезарь(30р.)', callback_data='Цезарь(30р.)')
    button2 = types.InlineKeyboardButton('Зимний(23р.)', callback_data='Зимний(23р.)')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Греческий(25р.)', callback_data='Греческий(25р.)')
    markup.row(button3)
    confirm_button = types.InlineKeyboardButton('Перейти к оплате', callback_data='confirm')
    markup.row(confirm_button)
    clear_button = types.InlineKeyboardButton('Очистить корзину', callback_data="clear")
    markup.row(clear_button)
    return markup


def vybor_soups():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Борщ(28р.)', callback_data = 'Борщ(28р.)')
    button2 = types.InlineKeyboardButton('Домашний(25р.)', callback_data = 'Домашний(25р.)')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Суп-пюре(27р.)', callback_data = 'Суп-пюре(27р.)')
    button4 = types.InlineKeyboardButton('Окрошка(52р.)', callback_data = 'Окрошка(52р.)')
    markup.row(button3, button4)
    confirm_button = types.InlineKeyboardButton('Перейти к оплате', callback_data='confirm')
    markup.row(confirm_button)
    clear_button = types.InlineKeyboardButton('Очистить корзину', callback_data="clear")
    markup.row(clear_button)
    return markup


def vybor_meat():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Индейка(27р.)', callback_data = 'Индейка(27р.)')
    button2 = types.InlineKeyboardButton('Курица(25р.)', callback_data = 'Курица(25р.)')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Говядина(30р.)', callback_data = 'Говядина(30р.)')
    button4 = types.InlineKeyboardButton('Свинина(23р.)', callback_data = 'Свинина(23р.)')
    markup.row(button3, button4)
    confirm_button = types.InlineKeyboardButton('Перейти к оплате', callback_data='confirm')
    markup.row(confirm_button)
    clear_button = types.InlineKeyboardButton('Очистить корзину', callback_data="clear")
    markup.row(clear_button)
    return markup


def vybor_second_dishes():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Макароны(10р.)', callback_data = 'Макароны(10р.)')
    button2 = types.InlineKeyboardButton('Картофель(13р.)', callback_data = 'Картофель(13р.)')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Гречка(12р.)', callback_data = 'Гречка(12р.)')
    button4 = types.InlineKeyboardButton('Рис(15р.)', callback_data = 'Рис(15р.)')
    markup.row(button3, button4)
    confirm_button = types.InlineKeyboardButton('Перейти к оплате', callback_data='confirm')
    markup.row(confirm_button)
    clear_button = types.InlineKeyboardButton('Очистить корзину', callback_data="clear")
    markup.row(clear_button)
    return markup


def vybor_bakers():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Шанежка с сыром(40р.)', callback_data = 'Шанежка с сыром(40р.)')
    button2 = types.InlineKeyboardButton('Лицейская пицца(45р.)', callback_data = 'Лицейская пицца(45р.)')
    markup.row(button1)
    markup.row(button2)
    button3 = types.InlineKeyboardButton('Булочка с сахаром(43р.)', callback_data = 'Булочка с сахаром(43р.)')
    button4 = types.InlineKeyboardButton('Хлеб(2р.)', callback_data = 'Хлеб(2р.)')
    markup.row(button3)
    markup.row(button4)
    confirm_button = types.InlineKeyboardButton('Перейти к оплате', callback_data='confirm')
    markup.row(confirm_button)
    clear_button = types.InlineKeyboardButton('Очистить корзину', callback_data="clear")
    markup.row(clear_button)
    return markup


def vybor_drinks():
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Компот(6р.)', callback_data = 'Компот(6р.)')
    button2 = types.InlineKeyboardButton('Чай(3р.)', callback_data = 'Чай(3р.)')
    markup.row(button1, button2)
    button3 = types.InlineKeyboardButton('Молочный коктейль(10р.)', callback_data = 'Молочный коктейль(10р.)')
    button4 = types.InlineKeyboardButton('Кисель(2р.)', callback_data = 'Кисель(2р.)')
    markup.row(button3)
    markup.row(button4)
    confirm_button = types.InlineKeyboardButton('Перейти к оплате', callback_data = 'confirm')
    markup.row(confirm_button)
    clear_button = types.InlineKeyboardButton('Очистить корзину', callback_data="clear")
    markup.row(clear_button)
    return markup   

price = {}
products = {}

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    global price, products
    if callback.data == 'salads':
        markup = vybor_salads()
        bot.send_message(callback.message.chat.id, text='Выберите из предложенного:', reply_markup=markup)

    elif callback.data == 'soups':
        markup = vybor_soups()
        bot.send_message(callback.message.chat.id, text='Выберите из предложенного:', reply_markup=markup)

    elif callback.data == 'meat':
        markup = vybor_meat()
        bot.send_message(callback.message.chat.id, text='Выберите из предложенного:', reply_markup=markup)

    elif callback.data == 'second dishes':
        markup = vybor_second_dishes()
        bot.send_message(callback.message.chat.id, text='Выберите из предложенного:', reply_markup=markup)

    elif callback.data == 'bakers':
        markup = vybor_bakers()
        bot.send_message(callback.message.chat.id, text='Выберите из предложенного:', reply_markup=markup)

    elif callback.data == 'drinks':
        markup = vybor_drinks()
        bot.send_message(callback.message.chat.id, text='Выберите из предложенного:', reply_markup=markup)

    elif callback.data == "confirm":
        if str(callback.message.chat.id) in products and str(callback.message.chat.id) in price:
            product_ = products[str(callback.message.chat.id)]
            price_ = price[str(callback.message.chat.id)]
            global pending_orders
            order_id = str(uuid.uuid4())
            pending_orders[order_id] = [product_, price_]
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton('Оплатить заказ', url=f'http://filestorage.gellyzxc.ru/projects/fake_payment/?id={order_id}&price={price_}&fallback=TheLyceum2TelegramBot')
            markup.row(button)
            bot.send_message(callback.message.chat.id, text='Ваш заказ:\n' + "\n".join(product_) + f"\nЦена заказа: {price_} р.", reply_markup=markup)
        
    elif callback.data == "clear":
        products[str(callback.message.chat.id)] = []
        price[str(callback.message.chat.id)] = 0
        bot.send_message(callback.message.chat.id, text="Корзина очищена")

    else:
        bot.send_message(callback.message.chat.id, text=f"Вы выбрали {callback.data}" )
        products[str(callback.message.chat.id)].append(callback.data)
        indx1 = callback.data.find("(")+1
        indx2 = callback.data.find(")")-2
        price[str(callback.message.chat.id)] += int(callback.data[indx1:indx2])
        return price[str(callback.message.chat.id)]

bot.infinity_polling(timeout = 60, long_polling_timeout = 60, none_stop = True)
