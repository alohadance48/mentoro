import telebot

bot = telebot.TeleBot(token='') # Пофикси меня!

@bot.message_handler(content_types=['text'])
def secret_key(message):
    if message.text == 'L+jQ)m)ig10D':
        '''Пропиши , чтобы кидало в наши секретные кнопки '''
        pass

    else:
        '''Пропиши , чтобы кидало в главное меню!'''
        pass


if __name__ == '__main__':
    bot.polling(none_stop=True)