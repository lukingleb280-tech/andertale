import telebot
from requests import delete

TOKEN = '8279547655:AAHwsoxeISoYoIFgM_cs2oI97y18nwvHdAM'
bot = telebot.TeleBot(TOKEN)

chat_room = {
    #[chat_id]:room_num
    # начать -> 1
    # да -> 2
}
chat_room_question = {
    #[chat_id]:question_num
}


@bot.message_handler(commands=["start"])
def handler_start(message):
    bot.send_message(message.chat.id, "Привет! Напиши 'начать', чтобы начать.")


@bot.message_handler(func=lambda message: True)
def handler_all(message):
    chat_id = message.chat.id
    text = message.text.lower()


    if chat_id in chat_room and chat_room[chat_id] == 3:
        bot.send_message(chat_id, "флауи в ярости ур.гнева 10  флауи - УМРИ! АХАХАХАХАХАХАХАХАХААХА флауи сбивает огненный шар прилетевший из соседней комнаты ")

    if chat_id in chat_room and chat_room[chat_id] == 2:
        if chat_room_question[chat_id] == 1:
            if text == "да":
                bot.send_message(chat_id,"цветок - привет я цветочек,цветочек флауи, Ты тут первый раз верно? Давай я помогу тебе. видишь эти пульки? (он создает кучу пуль в виде лепестков) иди в них они восстановят оз (зайти(да/нет)) да=смерть .")
                chat_room_question[chat_id] = 2

            elif text == 'нет':
                bot.send_message(chat_id, "ты стоишь перед цветком ....... поговорить?")

            else:
                bot.send_message(chat_id, "Пожалуйста, ответь 'да' или 'нет'.")

        elif chat_room_question[chat_id] == 2:
            if text == "да":
                bot.send_message(chat_id, "ТЫ УМЕР. отправь начать чтобы возродится")
                chat_room[chat_id] = 0
                chat_room_question[chat_id] = 0

            elif text == 'нет':
                bot.send_message(chat_id,
                                 'флауи" начинает злится! ур.гнева 5  флауи- Я ЖЕ ЯСНО СКАЗАЛ ЧТО ТЕБЕ НАДО ДЕЛАТЬ!!!! (исполнить просьбу?(да/нет) не советую отвечать да!!!!')
                chat_room[chat_id]= 3

            else:
                bot.send_message(chat_id, "Пожалуйста, ответь 'да' или 'нет'.")

    if chat_id in chat_room and chat_room[chat_id] == 1:
        if text == 'да':
            chat_room[chat_id] = 2
            bot.send_message(
                chat_id,
                "Ты попал в другую комнату, в которой был только один желтый цветок. поговорить?(да/нет)"
            )
            chat_room_question[chat_id] = 1
        elif text == 'нет':
            bot.send_message(chat_id, "ты остался в той же комнате")
        else:
            bot.send_message(message.chat.id, "Привет! Напиши 'начать', чтобы начать.")


    ###########################
    else:
        if text == "начать":
            bot.send_message(chat_id, "класс, я помогу тебе если будут сложности! здесь есть ур гнева и ур добра они играют самую важную роль "
                                      "если ур гнева поднимится до 10 ты УМРЕШЬ!"
                                      "А ЕСЛИ УР ДОБРА ПОДНИМИТСЯ ДО 5 ТО МОНСТР уйдет   ")
            bot.send_message(
                chat_id, "Ты проснулся в странной комнате на подстилке из цветов.")
            bot.send_message(chat_id, "Ты не помнишь, как сюда попал.")
            bot.send_message(chat_id, "Перед тобой дверь. Зайти? (да / нет)")
            chat_room[chat_id] = 1




bot.polling()
