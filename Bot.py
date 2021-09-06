# This Python file uses the following encoding: utf-8
import os, sys
import telebot
import config
from telebot import types
import logging


logging.basicConfig(filename='bot_log.log', level=logging.INFO,format='%(asctime)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',encoding='utf-8')
bot = telebot.TeleBot(config.TOKEN,parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):  

    logging.info(message.text,' : ',message.from_user) 

    bot.send_message(message.chat.id,"Welcome to the club, {0.first_name}!\n я - {1.first_name} , бот созданный помочь с выбором пивасик.".format(message.from_user, bot.get_me()),
    parse_mode='html')

    # КНОПКИ ДЛЯ УТОЧНЕНИЯ ВИДА ПИВА
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Эль", callback_data='Ale')
    item2 = types.InlineKeyboardButton("Лагер", callback_data='Lager')
          
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, 'Давай определимся с видом пивасика', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    logging.info(call.data,' : ',message.from_user)
    try:
        if call.message:
            if call.data == 'Ale':
                bot.send_message(call.message.chat.id, 'Эль варится из ячменного солода с использованием пивных дрожжей верхового брожения.')
                
                #КНОПКИ ДЛЯ УТОЧНЕНИЯ ВИДА ЭЛЯ
                markup1= types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("Портер(Porter)", callback_data='Porter')
                item4 = types.InlineKeyboardButton("Стаут(Stout)", callback_data='Stout')
                item5 = types.InlineKeyboardButton("Бледный Эль(Pale Ale)", callback_data='PaleAle')
                item6 = types.InlineKeyboardButton("Пшеничное (Witbier)", callback_data='Witbier')
                markup1.add(item3, item4, item5, item6)
                
                bot.send_message(call.message.chat.id,'Существует множество видов Эля самые распространенные это:',reply_markup=markup1)
        # ЕСЛИ НАЖМУТ ПОРТЕР ОТВЕТИТ
            if call.data == 'Porter':
                bot.send_message(call.message.chat.id,'Национальный английский сорт пива.\nХарактерезует данное пиво:\nСодержание спирта от 4 до 10%\n - Темный оттенок\n - Высокая плотность\n - Сильный аромат солода\n - Наделен сладко-горьковатым вкусом')           
        # ЕСЛИ НАЖМУТ Стаут ОТВЕТИТ
            if call.data == 'Stout':
                bot.send_message(call.message.chat.id,'Пиво родом из Ирландии.\nХарактерезует данное пиво:\nСодержание спирта от 4 до 12%\n - Темный оттенок с густой кремовой пенкой\n - Высокая плотность\n - Горьковатый вкус с кофейно-шоколадными тонами\n - Имеет бодрящий эффект') 
        # ЕСЛИ НАЖМУТ Бледный ОТВЕТИТ
            if call.data == 'PaleAle':
                bot.send_message(call.message.chat.id,'Впервые данное пиво сварили в Англии, сейчас чаще все встречаются IPA(India Pale Ale) и APA(American Pale Ale)\nХарактерезует данное пиво:\nСодержание спирта от 4-10%\n - Светлый оттенок(бывает золотистым)\n - Богатый хмельной аромат и приятная горечь')                           
        # ЕСЛИ НАЖМУТ пшеничка ОТВЕТИТ
            if call.data == 'Witbier':
                bot.send_message(call.message.chat.id,'Немецкое пиво широко распространенное в баварии\nХарактерезует данное пиво:\nСодержание спирта от 4 - 7%\n - Мутное и светлое пиво(бывает темным)\n - Имеет фруктовый пряный вкус (происходит это из-за большого количества эфиров,возникающих за счет высоких температур брожения)')  
        # ПОШЛО ПОЕХАЛО С ЛАГЕРОМ    
        if call.message:
            if call.data == 'Lager':
                bot.send_message(call.message.chat.id, 'Тип пива, при изготовлении которого используется низовое брожение с последующей ферментацией при низкой температуре')
            
                #КНОПКИ ДЛЯ УТОЧНЕНИЯ ВИДА лагера
                markup2 = types.InlineKeyboardMarkup(row_width=2)
                item7 = types.InlineKeyboardButton("Светлый Лагер", callback_data='Svetloe')
                item8 = types.InlineKeyboardButton("Пилснер", callback_data='Pilsner')
                markup2.add(item7, item8)              
                
                bot.send_message(call.message.chat.id,'Существует множество видов Эля самые распространенные это:',reply_markup=markup2)
                
            if call.data == 'Svetloe':
                bot.send_message(call.message.chat.id, 'Cветлое пиво, легкий сорт лагера с характерным нежным ароматом хмеля и солода\nСодержание от 3,2 до 6,0%.')          
            if call.data == 'Pilsner':   
                bot.send_message(call.message.chat.id, 'Тип светлого лагера. Название происходит от чешского города Пльзень, где в 1842 году и был изобретен этот стиль.\nСодержание алкоголя от 4 до 6 %\nЦвет: от соломенного до золотого. \nВкус: горьковатый, с «земляными» нотками.')                

    except Exception as e:
        logging.error(e,' : ',message.from_user)
        print(repr(e))

bot.polling(none_stop=True)

