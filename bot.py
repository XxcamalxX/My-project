import telebot
import random
import os    

bot = telebot.TeleBot("7838908405:AAE9BYnxaODDZB8KRfwOKDMBbx2CV7MQ7kM")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name=random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['password'])
def send_password(message):
    password=gen_pass()
    bot.reply_to(message, f'{password}') 


@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    bot.reply_to(message, gen_emodji())


@bot.message_handler(commands=['coinflip'])
def send_coinflip(message):
    bot.reply_to(message, flip_coin())


@bot.message_handler(commands=['sortirovka'])
def sortirovka(message):
    
    


    eco1=  " бумага-Синий контейнер 📘 (бумага и картон)"
    eco2=  " пластик-Жёлтый контейнер 🟨 (пластик и упаковка)"
    eco3=  " стекло-Зелёный контейнер 🟩 (стекло)"
    eco4=  " металл-Серый контейнер ⚙️ (металл)"
    eco5=  " органика-Коричневый контейнер 🟫 (пищевые отходы)"
    eco6=  " батарейка-Специальный сбор ♻️ (опасные отходы)"
    eco7=  " лампочка-Специальный сбор 💡 (ртутные лампы)"
    eco8=  " одежда-Пункт приёма 👕 (вещи на переработку)"
    ecos=[eco1,eco2,eco3,eco4,eco5,eco6,eco7,eco8]
    sortirovka= random.choice(ecos)
    bot.reply_to(message,f"вещи для сортировки на сегодня {sortirovka}" )
    
def gen_pass(pass_length=10):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password



def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)












    
bot.polling()
