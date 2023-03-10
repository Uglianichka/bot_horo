#5760799551:AAH00O2PG5gzbJGGXmoqYq_JaMQU4SNBa_w
import telebot
from telebot import types
bot = telebot.TeleBot('5760799551:AAH00O2PG5gzbJGGXmoqYq_JaMQU4SNBa_w')

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    capricorn_btn = types.InlineKeyboardButton(text="Козерог", callback_data='1')
    aquarius_btn = types.InlineKeyboardButton(text="Водолей", callback_data='2')
    pisces_btn = types.InlineKeyboardButton(text="Рыбы", callback_data='3')
    aries_btn = types.InlineKeyboardButton(text="Овен", callback_data='4')
    taurus_btn = types.InlineKeyboardButton(text="Телец", callback_data='5')
    gemini_btn = types.InlineKeyboardButton(text="Близнецы", callback_data='6')
    cancer_btn = types.InlineKeyboardButton(text="Рак", callback_data='7')
    leo_btn = types.InlineKeyboardButton(text="Лев", callback_data='8')
    virgo_btn = types.InlineKeyboardButton(text="Дева", callback_data='9')
    libra_btn = types.InlineKeyboardButton(text="Весы", callback_data='10')
    scorpio_btn = types.InlineKeyboardButton(text="Скорпион", callback_data='11')
    sagittarius_btn = types.InlineKeyboardButton(text="Стрелец", callback_data='12')
    keyboard.add(capricorn_btn)
    keyboard.add(aquarius_btn)
    keyboard.add(pisces_btn)
    keyboard.add(aries_btn)
    keyboard.add(taurus_btn)
    keyboard.add(gemini_btn)
    keyboard.add(cancer_btn)
    keyboard.add(leo_btn)
    keyboard.add(virgo_btn)
    keyboard.add(libra_btn)
    keyboard.add(scorpio_btn)
    keyboard.add(sagittarius_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        'Привет, %s, Выберите, пожалуйста, Ваш знак зодиака или напишите /znak, чтобы узнать какой у Вас знак зодиака' % message.from_user.full_name,
        reply_markup=keyboard)
date = 0

@bot.message_handler(content_types=['text'])
def get_text_messades(message):
    if message.text == '/znak':
        bot.send_message(message.from_user.id, 'Напиши свою дату рождения в формате ЧЧ.ММ')
        bot.register_next_step_handler(message,get_date)


def get_date(message):
    global date
    while date ==0:
        try:
            date = float(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Цифрами, пожалуйста ")
            break
        keyboard_1 = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes')
        keyboard_1.add(key_yes)
        key_no = types.InlineKeyboardButton(text= 'Нет', callback_data= 'no' )
        keyboard_1.add(key_no)
        question = 'Вы родились ' + str(date) + '?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard_1)

ov = [21.03, 22.03, 23.03, 24.03, 25.03, 26.03, 27.03, 28.03, 29.03, 30.03, 31.03, 01.04, 02.04, 03.04, 04.04, 05.04, 06.04, 07.04, 08.04, 09.04, 10.04, 11.04, 12.04, 13.04, 14.04, 15.04, 16.04, 17.04, 18.04, 19.04, 20.04]
tel = [21.04, 22.04, 23.04, 24.04, 25.04, 26.04, 27.04, 28.04, 29.04, 30.04, 01.05, 02.05, 03.05, 04.05, 05.05, 06.05, 07.05, 08.05, 09.05, 10.05, 11.05, 12.05, 13.05, 14.05, 15.05, 16.05, 17.05, 18.05, 19.05, 20.05]
bl = [21.05, 22.05, 23.05, 24.05, 25.05, 26.05, 27.05, 28.05, 29.05, 30.05, 31.05, 01.06, 02.06, 03.06, 04.06, 05.06, 06.06, 07.06, 08.06, 09.06, 10.06, 11.06, 12.06, 13.06, 14.06, 15.06, 16.06, 17.06, 18.06, 19.06, 20.06]
rak = [21.06, 22.06, 23.06, 24.06, 25.06, 26.06, 27.06, 28.06, 29.06, 30.06, 31.06, 01.07, 02.07, 03.07, 04.07, 05.07, 06.07, 07.07, 08.07, 09.07, 10.07, 11.07, 12.07, 13.07, 14.07, 15.07, 16.07, 17.07, 18.07, 19.07, 20.07, 21.07, 22.07]
lev = [23.07, 24.07, 25.07, 26.07, 27.07, 28.07, 29.07, 30.07, 31.07, 01.08, 02.08, 03.08, 04.08, 05.08, 06.08, 07.08, 08.08, 09.08, 10.08, 11.08, 12.08, 13.08, 14.08, 15.08, 16.08, 17.08, 18.08, 19.08, 20.08, 21.08, 22.08]
dev = [23.08, 24.08, 25.08, 26.08, 27.08, 28.08, 29.08, 30.08, 31.08, 01.09, 02.09, 03.09, 04.09, 05.09, 06.09, 07.09, 08.09, 09.09, 10.09, 11.09, 12.09, 13.09, 14.09, 15.09, 16.09, 17.09, 18.09, 19.09, 20.09, 21.09, 22.09]
ves = [23.09, 24.09, 25.09, 26.09, 27.09, 28.09, 29.09, 30.09, 31.09, 01.10, 02.10, 03.10, 04.10, 05.10, 06.10, 07.10, 08.10, 09.10, 10.10, 11.10, 12.10, 13.10, 14.10, 15.10, 16.10, 17.10, 18.10, 19.10, 20.10, 21.10, 22.10]
skp = [23.10, 24.10, 25.10, 26.10, 27.10, 28.10, 29.10, 30.10, 31.10, 01.11, 02.11, 03.11, 04.11, 05.11, 06.11, 07.11, 08.11, 09.11, 10.11, 11.11, 12.11, 13.11, 14.11, 15.11, 16.11, 17.11, 18.11, 19.11, 20.11, 21.11]
st = [22.11, 23.11, 24.11, 25.11, 26.11, 27.11, 28.11, 29.11, 30.11, 31.11, 01.12, 02.12, 03.12, 04.12, 05.12, 06.12, 07.12, 08.12, 09.12, 10.12, 11.12, 12.12, 13.12, 14.12, 15.12, 16.12, 17.12, 18.12, 19.12, 20.12, 21.12]
koz = [22.12, 23.12, 24.12, 25.12, 26.12, 27.12, 28.12, 29.12, 30.12, 31.12, 01.01, 02.01, 03.01, 04.01, 05.01, 06.01, 07.01, 08.01, 09.01, 10.01, 11.01, 12.01, 13.01, 14.01, 15.01, 16.01, 17.01, 18.01, 19.01 ]
vod = [20.01, 21.01, 22.01, 23.01, 24.01, 25.01, 26.01, 27.01, 28.01, 29.01, 30.01, 31.01, 01.02, 02.02, 03.02, 04.02, 05.02, 06.02, 07.02, 08.02, 09.02, 10.02, 11.02, 12.02, 13.02, 14.02, 15.02, 16.02, 17.02, 18.02]
rbk = [19.02, 20.02, 21.02, 22.02, 23.02, 24.02, 25.02, 26.02, 27.02, 28.02, 29.02, 01.03, 02.03, 03.03, 04.03, 05.03, 06.03, 07.03, 08.03, 09.03, 10.03, 11.03, 12.03, 13.03, 14.03, 15.03, 16.03, 17.03, 18.03, 19.03, 20.03]


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == 'yes':
            if date in ov:
                bot.send_message(call.message.chat.id, 'Вы ОВЕН',reply_markup=create_keyboard())
            elif date in tel:
                bot.send_message(call.message.chat.id, 'Вы ТЕЛЕЦ',reply_markup=create_keyboard())
            elif date in bl:
                bot.send_message(call.message.chat.id, 'Вы БЛИЗНЕЦЫ',reply_markup=create_keyboard())
            elif date in rak:
                bot.send_message(call.message.chat.id, 'Вы РАК',reply_markup=create_keyboard())
            elif date in lev:
                bot.send_message(call.message.chat.id, 'Вы ЛЕВ',reply_markup=create_keyboard())
            elif date in dev:
                bot.send_message(call.message.chat.id, 'Вы ДЕВА',reply_markup=create_keyboard())
            elif date in ves:
                bot.send_message(call.message.chat.id, 'Вы ВЕСЫ',reply_markup=create_keyboard())
            elif date in skp:
                bot.send_message(call.message.chat.id, 'Вы СКОРПИОН',reply_markup=create_keyboard())
            elif date in st:
                bot.send_message(call.message.chat.id, 'Вы СТРЕЛЕЦ',reply_markup=create_keyboard())
            elif date in koz:
                bot.send_message(call.message.chat.id, 'Вы КОЗЕРОГ',reply_markup=create_keyboard())
            elif date in vod:
                bot.send_message(call.message.chat.id, 'Вы ВОДОЛЕЙ',reply_markup=create_keyboard())
            elif date in rbk:
                bot.send_message(call.message.chat.id, 'Вы РАК',reply_markup=create_keyboard())
        elif call.data == 'no':
            bot.send_message(call.message.chat.id, 'Начните заново (/start или /znak)', reply_markup=create_keyboard())
        elif call.data == "1":
            img = open('Козерог.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Козерог 22 декабря — 19 января '
                        'Это человек-маятник, что вечно балансирует между двумя крайностями, '
                        'как утверждает смешная характеристика знаков зодиака. Для детей этого знака '
                        'характерна взрослая серьёзность и основательность. С этими качествами Козерог не '
                        'расстаётся даже в старости. Он с головой бросается в работу, словно в омут, и вытащить его '
                        'будет просто нереально. Он потратит все душевные и физические силы даже на заведомо '
                        'невыполнимое дело. Впрочем, если Козерогу приспичило загулять, то и этому занятию он отдастся '
                        'полностью, безудержно веселясь до полной деградации. Спасти его от печальной участи можно '
                        'только в том случае, если удастся отвлечь внимание на что-то более интересное.Козероги - '
                        'неисправимые пессимисты. Если уж он убеждён, что все вокруг гады ползучие, которые к успеху '
                        'пришли по головам или через постель, то хоть кол ему теши на голове - не переубедишь всё равно.',
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('Водолей.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Водолей 20 января — 18 февраля '
                        'Словоблудие выплёскивается из Водолеев, как вода из крана. Если кто и способен долго выдерживать'
                        ' этот поток и даже быть интересным собеседником, так это Близнецы. Пожалуй, можно ещё '
                        'поспорить, кто кого переговорит в итоге.Любовь для Водолея - это прежде всего романтика: '
                        'прогулки при Луне, встречи рассвета. Готовьтесь с ним покорять окутанные тайнами древние '
                        'развалины - это для него непременный атрибут ухаживания. Как утверждают прикольные '
                        'характеристики знаков зодиака, в стихах и серенадах такому человеку нет равных. '
                        'Женщины-Водолеи привыкли следовать велению сердца. Если оно подсказывает, что вы должны '
                        'быть вместе, ждите её на пороге с чемоданами. Что больше всего ценят Водолеи? Конечно, '
                        'Они готовы выстроить вокруг себя трёхметровую стену, лишь бы только их никто не трогал, если '
                        'хочется побыть в одиночестве. И никакая осада не поможет - Водолей сделал необходимый запас '
                        'печенек и будет ещё долго жить и не тужить в своём уютном мирке.',
                reply_markup=keyboard)
            img.close()
        if call.data == "3":
            img = open('tild3838-3331-4062-a665-643262656261__2.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Рыбы 19 февраля — 20 марта '
                        'Если кто и способен из ничего создать для себя и окружающих альтернативную выдуманную '
                        'реальность, так это Рыбы. Причём для них мир фантазии будет таким же настоящим, как и наш '
                        'привычный. Они запросто убедят в этом кого угодно. Барон Мюнхгаузен, например, как утверждают '
                        'характеристики знаков зодиака, неопытный и робкий малёк, блёклая икринка.Попросите этого '
                        'человека о чём угодно - цветы поливать в ваше отсутствие, диплом за вас написать - он '
                        'непременно в лепёшку расшибётся, но выполнит просьбу. Такой уж уродился альтруист, ничего не '
                        'поделаешь. В любви Рыбы застенчивы и осторожны, будут долго ходить вокруг да около, '
                        'прежде чем сделать шаг навстречу. «Ваниль» - это про них: грустные вздохи, трогательные '
                        'подарочки, неловкость и слёзы по ночам, а, главное, - все мысли только о нём (или о ней). '
                        'Так что если вы готовы взять влюблённую в вас Рыбу и под локоток повести в нужном направлении '
                        '(и всю жизнь потом подталкивать пинками вперёд) - дерзайте.',
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            img = open('Овен.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Овен 21 марта — 19 апреля '
                        'Все прикольные характеристики знаков зодиака сходятся в одном: найти более упёртого спорщика,'
                        ' нежели этот капризный и твердолобый барашек, у вас не получится.Овен ненавидит бытовую '
                        'рутину, зато с удовольствием будет крутиться рядом и выдавать свои новаторские идеи без '
                        'умолку. Заставить его сделать то, что не хочется, почти невозможно. Но есть одна маленькая'
                        ' хитрость. Скажите, что другой человек выполнит это лучше. Тут уж Овен разобьётся в лепёшку, '
                        'чтобы доказать своё лидерство и превосходство.Огненную натуру Овна отмечают смешные '
                        'характеристики знаков зодиака. По времени, которое этот человек готов потратить на завоевание'
                        ' объекта своей страсти, ему нет равных. Баран, он и в Африке баран, идущий напролом сквозь'
                        ' джунгли. Овна в этом деле даже можно окрестить ракетой - действует моментально, напористо '
                        'и отвязаться от его ухаживаний просто нереально. «Вы привлекательны, я - чертовски '
                        'привлекателен, так чего время терять» - вот его девиз в любви.',
                reply_markup=keyboard)
            img.close()
        if call.data == "5":
            img = open('Телец.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Телец 20 апреля — 20 мая '
                        'Вот он, достойный конкурент Овна по степени упрямства. Это подтвердят вам не только обычные'
                        ' гороскопы, но и любая смешная характеристика знаков зодиака. Причём к завидному упорству '
                        'прилагается в качестве «бонуса» и лютый консерватизм. Попробуйте заставить Тельца выкинуть '
                        'что-то из устаревшего домашнего хлама и вы это поймёте. Будь это испорченный диск, оставшаяся'
                        ' со школьных времён тетрадка или изорвавшиеся кроссовки - неважно. Для него все эти вещи '
                        'являются ценными. А ещё Тельцы ужасные зануды: слушая их бесконечные поучения, можно не '
                        'только заснуть, но и захрапеть.Представители этого созвездия - замкнутые личности. Проще '
                        'поговорить со стеной, нежели с Тельцом. По крайней мере, постучав по ней, вы услышите гул. '
                        'В случае с Тельцом сохраниться загробная тишина и звенящее молчание.К любви отношение Тельца '
                        'такое же, как и к вещам - чем больше денег и времени он потратил, добиваясь вас, тем ценнее '
                        'вы для него будете.',
                reply_markup=keyboard)
            img.close()
        if call.data == "6":
            img = open('Близнецы.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Близнецы 21 мая — 21 июня '
                        'Они легки в делах и мыслях. Близнецы из той породы людей, что будут выступать «за любой кипиш,'
                        ' кроме голодовки». Как отмечают смешные характеристики знаков зодиака, по дате рождения и '
                        'характеру эти личности полностью соответствуют взбалмошным индивидам, у которых в голове '
                        'гуляет целая компания ветров. Любовь Близнецов к болтовне имеет поистине катастрофический '
                        'характер для тех, кто сам не Близнецы. Много часов они могут не умолкать, совершенно не '
                        'обращая внимания на реакцию окружающих. Кажется, даже на собственных поминках Близнец '
                        'поднимется из гроба и расскажет валяющимся в обмороке гостям подходящий по теме анекдот. '
                        'Лень этих личностей столь же легендарна, как и их разговорные умения. Из-за нежелания '
                        'углубляться в какую-то тему и изучать её подолгу, они поверхностно описывают то или иное '
                        'явление, нахватавшись всего понемножку. Идеальная для них профессия - та, что поможет '
                        'мгновенно и без лишних телодвижений заработать миллион.',
                reply_markup=keyboard)
            img.close()
        if call.data == "7":
            img = open('Рак.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Рак 22 июня — 22 июля '
                        'Натуры интеллигентные, мягкие и романтичные, даже если внешне похожи на чёрствый батон, '
                        'брутального мужлана или неотёсанную деревенщину. При просмотре недетских фильмов эротического'
                        ' характера они всегда втайне надеются, что в конце главные герои поженятся. Смешная '
                        'характеристика знаков зодиака сравнивает Раков с их тёзками из животного мира. Подобно '
                        'им представители этого созвездия, если и делают вперёд аккуратный шаг, то тут же бегут '
                        'обратно. Они являются нерешительными типами, которые из-за своей осторожности боятся даже'
                        ' изменять - мало ли, что на уме у другого человека. Искромётно шутить в присутствии Рака '
                        'нежелательно, ведь люди эти сентиментальны и могут расстроиться даже из-за лёгкого юмора, '
                        'направленного на них или их близких. Сатира про животных - строжайшее табу. Они скорее'
                        ' переживут землетрясение и цунами, нежели вынесут чёрный юмор про несчастных собачек и '
                        'кошечек.',
                reply_markup=keyboard)
            img.close()
        if call.data == "8":
            img = open('Лев.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Лев 23 июля — 22 августа '
                        'Единственный и неповторимый Он горд и величав, даже если оказывается запертым в клетке '
                        'зоопарка. Дикие крики находящихся рядом животных его не интересуют - он персона важная и'
                        ' всячески это демонстрирует. Если рассматривать главные характеристики знаков зодиака,'
                        ' смешное описание выделяет царственность этой особы, сбить спесь с которой не сможет, '
                        'кажется, никакая неприятность. то хорошо самому Льву, то бывает не очень весело и приятно'
                        ' его близким, ведь ему требуется обращение, достойное статуса. По его мнению, окружающие '
                        'должны быть рады уже тому, что Его Высочество находится рядом. Львиная аура способна затмить '
                        'всё вокруг своим сиянием, раскрашивая даже мутное болотце всеми цвета радуги. Впрочем, иногда'
                        ' в тот водоворот событий, который генерирует вокруг себя Лев, может попасть совсем не то, что '
                        'ему хотелось бы. Что поделаешь, такова сила царской воли. Хотите распознать Льва в своём '
                        'окружении? ',
                reply_markup=keyboard)
            img.close()
        if call.data == "9":
            img = open('Дева.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Дева 23 августа — 22 сентября '
                        'Истинным подтверждением того, что внешность бывает обманчива, являются представители этого'
                        ' созвездия. Казалось бы, при слове «дева» воображение рисует нам милое, хрупкое и ранимое'
                        ' создание, которое сидит дома за рукоделием. С таким представлением несогласны астрологи, '
                        'составляющие характеристики знаков зодиака. Смешная ирония судьбы заключается в том, что в'
                        ' реальности дела обстоят «чуточку» иначе. Вместо тонко чувствующего друга, поддерживающего с '
                        'тяжёлые времена, соратника во всех начинаниях, Дева запросто может оказаться… серийным'
                        ' убийцей. Да-да, статистика утверждает, что большинство маньяков родились именно под этим'
                        ' знаком зодиака (а чего ещё ждать от таких аккуратистов и чистюль?).Своё умение подстраиваться'
                        ' под окружающую обстановку и быть всегда подчёркнуто вежливым и корректным человеком, Дева '
                        'запросто может использовать, чтобы добиться желаемой цели.',
                reply_markup=keyboard)
            img.close()
        if call.data == "10":
            img = open('Весы.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Весы 23 сентября — 23 октября '
                        'Какими бы ни были смешные характеристики знаков зодиака, по годам и месяцам все они точно'
                        ' определяют одно: знак этот полностью оправдывает своё название. Люди-Весы постоянно '
                        'пребывают в поиске равновесия душевного, а потому совершенно не обращают внимания на мир '
                        'материальный. Пусть кто-то другой занимается решением бытовых проблем, будь то готовка, '
                        'стирка или уборка, а у Весов есть дела более возвышенные.Людей этого знака вечно бросает в'
                        ' разные стороны. Быстро загоревшись новой идеей, все доступные ресурсы они бросят на то, '
                        'чтобы её осуществить. Они подключат уйму народа и создадут событие государственного масштаба,'
                        ' но на середине пути им всё это надоест. Они тихонько удалятся, оставляя других разгребать '
                        'заваренную ими кашу.Непостоянство Весов распространяется и на дела любовные. Причём для них '
                        'это состояние настолько привычно, что после измены их даже не будет мучить совесть.',
                reply_markup=keyboard)
            img.close()
        if call.data == "11":
            img = open('Скорпион.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Скорпион 24 октября — 21 ноября '
                        'Это настоящие ядовитые заразы. Смешные характеристики знаков зодиака в стихах и прозе '
                        'воспевают их способность разбивать сердца всех, кто окажется в пределах видимости.'
                        ' Поблагодарить в этом надо природное обаяние Скорпионов и их умение обольщать. Есть у'
                        ' этого знака способность постоянно в кого-нибудь влюбляться, причём каждый раз «до гробовой'
                        ' доски». Объект внимания тут же будет поставлен перед этим фактом. Отвертеться от '
                        'оригинальных ухаживаний Скорпиона вряд ли получится, да и не захочется - он тонкий психолог'
                        ' и непременно сумеет найти дорожку к сердцу возлюбленной (или возлюбленного).Скорпионы - '
                        'лидеры с рождения и умны не по годам. Если представитель этого знака выбрал для себя цель, '
                        'то, какой бы она ни была труднодостижимой, будет идти к ней с принципиальным упрямством. И '
                        'пусть придётся разрушить всё, что окажется на пути - Скорпиона это не остановит. Зато и '
                        'строить новый мир после устроенного хаоса он будет с таким же энтузиазмом.',
                reply_markup=keyboard)
            img.close()
        if call.data == "12":
            img = open('Стрелец.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Стрелец 22 ноября — 21 декабря '
                        'Люди этого знака зодиака всегда достигают поставленной цели, даже если это произойдёт '
                        'не сразу. Смешная характеристика знаков зодиака советует взглянуть на их символ: всё сразу'
                        ' станет ясно. Только вот если другие получают желаемое благодаря упорству и трудолюбию, '
                        'Стрельцам в этом помогает попутный ветер, который направляет пущенные стрелы точно в яблочко.'
                        'По натуре своей Стрельцы - настоящие благотворители. Вечно пытаются пожалеть всех подряд и '
                        'накормить страждущих (причём неважно, что думают сами одариваемые). Их девиз - «кто, кроме '
                        'меня?». Этим отлично пользуются работодатели. Ну а что, Стрелец не станет возражать, если '
                        'его нагрузить кучей работы. Надо лишь намекнуть, что для фирмы очень важно, чтобы всё было '
                        'сделано. А уж как именно - Стрелец сам сумеет найти способ.Но не стоит в открытую обижать '
                        'Стрельца. Нет, они вовсе не злопамятные, просто злые, и память у них отличная. Припомнят вам '
                        'все недоразумения начиная с детского сада. ',
                reply_markup=keyboard)
            img.close()


if __name__ == '__main__':
    bot.polling(none_stop=True)
