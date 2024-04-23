
import telebot
from telebot import types

bot = telebot.TeleBot('Token')

# стартовая команда
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Планиметрия")
    btn2 = types.KeyboardButton('Справочная информация')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Выберите раздел геометрии", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

# Планиметрия
        if message.text == 'Планиметрия':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Углы и параллельность")
            btn2 = types.KeyboardButton('Геометрические места точек')
            btn3 = types.KeyboardButton('Треугольник')
            btn4 = types.KeyboardButton('Параллелограмм')
            btn5 = types.KeyboardButton('Трапеция')
            btn6 = types.KeyboardButton('Окружность')
            btn7 = types.KeyboardButton('Площади')
            btn8 = types.KeyboardButton('Вернуться к выбору раздела')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
            bot.send_message(message.from_user.id, 'Планиметрия - раздел элементарной геометрии, изучающий фигуры на плоскости.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Выберите интересующий вас раздел планиметрии', reply_markup=markup)

# Кнопки назад
        elif message.text == 'Вернуться к выбору раздела':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Планиметрия")
            btn2 = types.KeyboardButton('Справочная информация')
            markup.add(btn1, btn2)
            bot.send_message(message.from_user.id, "Выберите раздел чтобы начать", reply_markup=markup)

        elif message.text == 'Обратно к подразделу "Углы и параллельность"':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Углы")
            btn2 = types.KeyboardButton('Параллельность')
            btn3 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, "Выберите нужный раздел по теме 'Углы и параллельность'", reply_markup=markup)

        elif message.text == 'Вернуться к выбору раздела Планиметрии':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Углы и параллельность")
            btn2 = types.KeyboardButton('Геометрические места точек')
            btn3 = types.KeyboardButton('Треугольник')
            btn4 = types.KeyboardButton('Параллелограмм')
            btn5 = types.KeyboardButton('Трапеция')
            btn6 = types.KeyboardButton('Окружность')
            btn7 = types.KeyboardButton('Площади')
            btn8 = types.KeyboardButton('Вернуться к выбору раздела')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
            bot.send_message(message.from_user.id, 'Выберите интересующий вас раздел планиметрии', reply_markup=markup)

        elif message.text == 'Углы и параллельность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('Углы')
            btn2 = types.KeyboardButton('Параллельность')
            btn3 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, 'Выберите подраздел по теме "Углы и параллельность"', reply_markup=markup)

# Справочная информация
        elif message.text == 'Справочная информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("О боте")
            btn2 = types.KeyboardButton('Справочное пособие')
            btn3 = types.KeyboardButton('Вернуться к выбору раздела')
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.from_user.id, 'Вся справочная информация, представленная в этом боте, взята из справочного пособия\n"Геометрия в таблицах 7 - 11"', reply_markup=markup)

        elif message.text == 'Справочное пособие':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("")
            file = open('geoma./Spravochnik_pdf.pdf', 'rb')
            markup.add(btn1)
            bot.send_message(message.from_user.id, 'Файл может отправляться некоторое время, подождите пожалуйста.', reply_markup=markup)
            bot.send_document(message.chat.id, file, reply_markup=markup)

        elif message.text == 'О боте':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("")
            markup.add(btn1)
            bot.send_message(message.from_user.id, 'Здесь вы найдете полезную информацию о боте, который предоставляет справочные сведения по планиметрии.\n \nСправочник по геометрии - это автоматизированный помощник, предназначенный для помощи в повторении планиметрии. Бот предоставляет справочные материалы, определения основных геометрических терминов и формул.\n \nФункции бота:\n- Выдача определений и концепций планиметрии, включая геометрические термины, типы фигур и их свойства.\n- Краткая выдержка теории конкретного вопроса (определения, теоремы, следствия, формулы).\n- Ответы на вопросы, связанные с планиметрией, и уточнение сложных тем и концепций.\n \nЕсли у вас возникли вопросы, предложения или вы хотите оставить отзыв о боте, вы можете связаться с нами по следующим контактным данным:\n- Email: None\n- Телефон: None\n- Вконтакте: None\n \nМы стремимся предоставить вам наилучший опыт работы с ботом по планиметрии. Будем рады услышать ваши отзывы и предложения, чтобы улучшить его функциональность и полезность.\n \nБлагодарим вас за использование нашего бота и надеемся, что он поможет вам лучше разобраться в мире планиметрии!', reply_markup=markup)

# Углы
        elif message.text == 'Углы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('1. Угол')
            btn2 = types.KeyboardButton('2. Градусная мера углов')
            btn3 = types.KeyboardButton('3. Виды углов')
            btn4 = types.KeyboardButton('4. Угол между прямыми')
            btn5 = types.KeyboardButton('5. Углы, образованные от пересечения прямых и секущей')
            btn6 = types.KeyboardButton('Обратно к подразделу "Углы и параллельность"')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            bot.send_message(message.from_user.id, 'Выбери интересующую справочную информацию по теме "Углы"', reply_markup=markup)
            bot.send_message(message.from_user.id, '1. Угол\n \n2. Градусная мера угла\n \n3. Виды улов\n \n4. Угол между прямыми\n \n5. Угол, образованный от пересечения прямых и секущей', reply_markup=markup)

        elif message.text == '1. Угол':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./ygol1.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Углом называется фигура, образованная двумя лучами, выходящими из одной точки (вершины).\n \nЛуч, выходящий из вершины угла и делящий его пополам, называется биссектрисой угла.', reply_markup=markup)

        elif message.text == '2. Градусная мера углов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file1 = open('geoma./ygol3.jpg', 'rb')
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id,'Градус - величина (градусная мера) угла, равного 1/180 части развернутого угла.',reply_markup=markup)

            file = open('geoma./ygol2..jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Радиан - величина угла, градусная мера которого равна (180/пи)°.', reply_markup=markup)

        elif message.text == '3. Виды углов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./ygol4.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Угол, равный половине развернутого, называется прямым (90°).\n \nУгол меньше прямого называется острым.\n \nУгол больше прямого, но меньше развернутого называется тупым.', reply_markup=markup)
            file1 = open('geoma./ygol5.jpg', 'rb')
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Смежные углы\n \nДва угла, у которых одна сторона общая, а две другие являются дополнительными лучами, называются смежными.\n \nСумма смежных углов равна 180°.\n \nУгол, смежный с прямым, - прямой', reply_markup=markup)
            file2 = open('geoma./ygol6.jpg', 'rb')
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Вертикальные углы\n \nДва угла, стороны одного из которых являются дополнительными лучами сторон другого, называются вертикальными.\n \nВертикальные углы равны', reply_markup=markup)

        elif message.text == '4. Угол между прямыми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./ygol7.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Углом между двумя пересекающимися прямыми называется меньший из вертикальных углов, образовавшихся при пересечении.\n \nПрямые, образующие прямой угол, называются перпендикулярными.\n \nДве прямые плоскости, не имеющие общих точек, называются параллельными.', reply_markup=markup)
            file1 = open('geoma./ygol8.jpg', 'rb')
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'При пересечении двух прямых третьей (секущей) образуются пары углов:\n \n(1; 2), (3; 4), (5; 6) и (7; 8) накрест лежащие;\n \n(1; 8), (5; 3), (4; 6) и (7; 2) cooтветственные;\n \n(1; 3), (2; 4), (5; 8) и (7; 6) одно сторонние', reply_markup=markup)

        elif message.text == '5. Углы, образованные от пересечения прямых и секущей':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./ygol9.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Накрест лежащие углы равны (∠1 = ∠2; ∠3 = ∠4; ∠5 = ∠6; ∠7 = ∠8).\n \nСоответственные углы равны (∠3 = ∠5; ∠1 = ∠2 = ∠7; ∠4 = ∠6).\n \nСумма односторонних углов 180° (∠1 + ∠3 = ∠5 + ∠8 = ∠2 + ∠4 = ∠6 + ∠7 = 180°)', reply_markup=markup)

# Параллельность
        elif message.text == 'Параллельность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('1. Аксиома параллельности')
            btn2 = types.KeyboardButton('2. Признаки параллельных прямых')
            btn3 = types.KeyboardButton('3. Теорема Фалеса')
            btn4 = types.KeyboardButton('4. "Расширенная" теорема Фалеса')
            btn5 = types.KeyboardButton('Обратно к подразделу "Углы и параллельность"')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, 'Выберите интересующую справочную информацию по теме "Параллельность"', reply_markup=markup)
            bot.send_message(message.from_user.id, '1. Аксиома параллельности\n \n2. Признаки параллельных прямых\n \n3. Теорема Фалеса\n \n4. "Расширенная" теорема Фалеса', reply_markup=markup)

        elif message.text == '1. Аксиома параллельности':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            bot.send_message(message.from_user.id, 'Через точку, не лежащую на данной прямой, проходит только одна прямая, параллельная данной.', reply_markup=markup)

        elif message.text == '2. Признаки параллельных прямых':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pr1.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если две различные прямые параллельны третьей, то они параллельны между собой (транзитивность параллельности).', reply_markup=markup)
            file1 = open('geoma./pr2.jpg', 'rb')
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если при пересечении двух прямых третьей накрест лежащие углы равны, то прямые параллельны.\n \nЕсли при пересечении двух прямых третьей соответственные углы равны, то прямые параллельны.\n \nЕсли при пересечении двух прямых третьей сумма односторонних углов равна 180°, прямые параллельны', reply_markup=markup)
            file2 = open('geoma./pr3.jpg', 'rb')
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Сумма углов треугольника равна 180°', reply_markup=markup)

        elif message.text == '3. Теорема Фалеса':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pr4.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если на одной из двух прямых отложены несколько равных отрез ков и через их концы проведены параллельные прямые, пересе кающие вторую прямую, то и на ней отложатся равные отрезки.', reply_markup=markup)

            file1 = open('geoma./pr5.jpg', 'rb')
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Деление отрезка на равные части', reply_markup=markup)

        elif message.text == '4. "Расширенная" теорема Фалеса':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pr6.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если на одной из двух прямых отложены несколько отрезков и через их концы проведены параллельные прямые, пересекающие вторую прямую, то на ней отложатся отрезки, пропорциональные данным.', reply_markup=markup)

# Геометрические места точек
        elif message.text == 'Геометрические места точек':
             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
             btn1 = types.KeyboardButton("1. Серединный перпендикуляр")
             btn2 = types.KeyboardButton('2. Биссектриса угла')
             btn3 = types.KeyboardButton('3. Параллельная прямая')
             btn4 = types.KeyboardButton('4. Две вз. перпен. прямые')
             btn5 = types.KeyboardButton('5. Окружность мн.т.')
             btn6 = types.KeyboardButton('6. Две параллельные прямые')
             btn7 = types.KeyboardButton('7. Прямой угол на полуокружности')
             btn8 = types.KeyboardButton('8. Две симетричные дуги')
             btn9 = types.KeyboardButton('9. Окружность Аполлония')
             btn10 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
             markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
             bot.send_message(message.from_user.id, 'Выберите интересующую справочную информацию по теме "Геометрические места точек"', reply_markup=markup)
             bot.send_message(message.from_user.id, '1. Серединный перпендикуляр\n \n2. Биссектриса угла\n \n3. Параллельная прямая\n \n4. Две взаимно перпендикулярные прямые\n \n5. Окружность: множество точек\n6. Две параллельные\n \n7. Прямой угол на полуокружности\n \n8. Две симметричный дуги\n \n9. Окружность Аполлония', reply_markup=markup)

        elif message.text == '1. Серединный перпендикуляр':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm1.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек, равноудаленных от двух данных точек, есть серединный перпендикуляр отрезка, соединяющего эти точки (на нем лежат центры окружностей, проходящих через данные две точки)', reply_markup=markup)

        elif message.text == '2. Биссектриса угла':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm2.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек, равноудаленных от сторон данного угла (меньшего, чем развернутый), есть биссектриса угла (на ней лежат центры окружностей, касающихся сторон угла)', reply_markup=markup)

        elif message.text == '3. Параллельная прямая':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm3.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек, равноудаленных от двух параллельных прямых, есть параллельная им прямая, проходящая через середину отрезка их общего перпендикуляра (на ней лежат центры окружностей, касающихся данных прямых)', reply_markup=markup)

        elif message.text == '4. Две вз. перпен. прямые':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm4.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек, равноудаленных от двух пересекающихся прямых, есть две взаимно перпендикулярные прямые, на которых лежат биссектрисы вертикальных углов, образовавшихся при пересечении данных прямых (на них лежат центры окружностей, касающихся данных прямых)', reply_markup=markup)

        elif message.text == '5. Окружность мн.т.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm5.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек, удаленных на данное расстояние от точки, есть окружность с центром в данной точке.', reply_markup=markup)

        elif message.text == '6. Две параллельные прямые':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm6.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек, удаленных на данное расстояние от прямой, есть две параллельные ей прямые.', reply_markup=markup)

        elif message.text == '7. Прямой угол на полуокружности':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm7.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество вершин прямоугольных треугольников с данной гипотенузой есть окружность, построенная на гипотенузе как на диаметре (исключая концы гипотенузы)', reply_markup=markup)

        elif message.text == '8. Две симетричные дуги':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm8.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек, из которых данный отрезок виден под даным углом, есть две симметричные, опирающиеся на данный отрезок, дуги (исключая концы этих дуг)', reply_markup=markup)

        elif message.text == '9. Окружность Аполлония':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./gm9.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Множество точек М, таких что АМ = kМВ, есть окружность с диаметром N₁ N₂  на прямой АВ такая, что AN₁ : N₁B = k и AN₂ : N₂ B=k (k≠1)', reply_markup=markup)

 #треугольник
        elif message.text == 'Треугольник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("1. Неравенство треугольника")
            btn2 = types.KeyboardButton('2. Признаки равенства треугольников')
            btn3 = types.KeyboardButton('3. Признаки подобия треугольников')
            btn4 = types.KeyboardButton('4. Элементы треугольника')
            btn5 = types.KeyboardButton('5. Площадь треугольника')
            btn6 = types.KeyboardButton('6. Теорема косинусов/синусов')
            btn7 = types.KeyboardButton('7. Вписанная/Описанная окружность, вычисление радиусов')
            btn8 = types.KeyboardButton('8. Прямоугольный треугольник, его свойства и признаки')
            btn9 = types.KeyboardButton("9. Тригонометрические функции острых углов прямоугольного треугольника")
            btn10 = types.KeyboardButton('10. Классификация треугольников')
            btn11 = types.KeyboardButton('11. Равнобедренный треугольник')
            btn12 = types.KeyboardButton('12. Правильный треугольник')
            btn13 = types.KeyboardButton('13. Дополнительные теоремы о треугольнике')
            btn14 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn11, btn10, btn12, btn13,btn14 )
            bot.send_message(message.from_user.id, 'Выберите интересующую справочную информацию по теме "Треугольник"', reply_markup=markup)
            bot.send_message(message.from_user.id, '1. Неравенство треугольника\n \n2. Признаки равенства треугольников\n \n3. Признаки подобия треугольников\n \n4. Элементы треугольника\n \n5. Площадь треугольника\n \n6. Теорема косинусов/синусов\n \n7. Вписанная/Описанная окружность, вычисление  радиусов\n \n8. Прямоугольный треугольник, его свойства и признаки\n \n9. Тригонометрические функции острых углов прямоугольного треугольника\n \n10. Классификация треугольников\n \n11. Равнобедренный треугольник\n \n12. Правильный треугольник\n \n13. Дополнительные теоремы о треугольнике',reply_markup=markup)

        elif message.text == '1. Неравенство треугольника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr1.jpg', 'rb')
            file1 = open('geoma./tr2.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'В любом треугольнике каждая сторона меньше суммы двух других сторон.\n \na - b < c < a + b, где а, b, с длины сторон треугольника, причем а > b\n \nВнешний угол треугольника равен сумме двух внутренних, не смежных с ним углов.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Сумма углов треугольника 180°', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'В треугольнике против большей стороны лежит больший угол, против большего угла большая сторона.', reply_markup=markup)

        elif message.text == '2. Признаки равенства треугольников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr3.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Признаки равенства треугольников\n \nПо двум сторонам и углу между ними (С У С)\n \nПо стороне и двум прилежащим к ней углам (У С У)\n \nПо трем сторонам (С С С)\n \nСходственные (соответствующие) элементы равных треугольников равны.', reply_markup=markup)

        elif message.text == '3. Признаки подобия треугольников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr4.jpg', 'rb')
            file1 = open('geoma./tr5.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Признаки подобия треугольников По двум углам (У У)\n \nПо двум сторонам и углу между ними (С У С)\n \nПо трем сторонам (С С С)', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Прямая, параллельная стороне треугольника, отсекает от него треугольник, подобный данному.\n \nСходственные линейные элементы подобных треугольников пропорциональны сходственным сторонам.\n \nПериметры подобных треугольников относятся как сходственные стороны.\n \nПлощади подобных треугольников относятся как квадраты сходственных сторон.\n \n', reply_markup=markup)

        elif message.text == '4. Элементы треугольника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr6.jpg', 'rb')
            file1 = open('geoma./tr7.jpg', 'rb')
            file2 = open('geoma./tr8.jpg', 'rb')
            file3 = open('geoma./tr9.jpg', 'rb')
            file4 = open('geoma./tr10.jpg', 'rb')
            file5 = open('geoma./tr11.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Медианой треугольника называется отрезок, который соединяет вершину треугольника с серединой противолежащей стороны.\n \nМедианы треугольника пересекаются в одной точке (центре тяжести треугольника) и делятся этой точкой в отношении 2: 1, считая от вершины.\n \nМедиана делит треугольник на два равновеликих треугольника. Три медианы делят треугольник на шесть равновеликих треугольников.', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Высотой треугольника называется отрезок перпендикуляра, опущенного из вершины треугольника на прямую, содержащую противолежащую сторону.\n \nВсе высоты треугольника пересекаются в одной точке - ортоцентре треугольника.', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Биссектрисой треугольника называется отрезок биссектрисы внутреннего угла треугольника.\n \nВсе биссектрисы треугольника пересекаются в одной точке - центре вписанной в треугольник окружности.\n \nБиссектриса делит противолежащую сторону на отрезки, пропорциональные прилежащим сторонам треугольника.', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Биссектрисы внутреннего и смежного с ним внешнего углов треугольника перпендикулярны.\n \nБиссектриса внешнего угла неравнобедренного треугольника пересекает продолжение противолежащей стороны в точке, отстоящей от концов этой стороны на расстояния, пропорциональные длинам двух других сторон.', reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Средней линией треугольника называется отрезок, соединяющий середины двух сторон треугольника.\n \nСредняя линия параллельна третьей стороне и равна ее половине.', reply_markup=markup)
            bot.send_photo(message.chat.id, file5, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Серединным перпендикуляром называется прямая, перпендикулярная стороне треугольника и делящая ее пополам.\n \nВсе серединные перпендикуляры сторон треугольника пересекаются в одной точке центре описанной около треугольника окружности. Около каждого треугольника можно описать окружность и притом только одну.\n \nТочка пересечения серединных треугольника перпендикуляров является точкой пересечения высот треугольника, образованного средними линиями данного.', reply_markup=markup)

        elif message.text == '5. Площадь треугольника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr12.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)

        elif message.text == '6. Теорема косинусов/синусов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr13.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Квадрат стороны треугольника равен сумме квадратов двух других сторон без удвоенного произведения этих сторон на косинус угла между ними.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Стороны треугольника пропорциональны синусам противолежащих им углов.', reply_markup=markup)

        elif message.text == '7. Вписанная/Описанная окружность, вычисление радиусов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr14.jpg', 'rb')
            file1 = open('geoma./tr15.jpg', 'rb')
            file2 = open('geoma./tr22.jpg', 'rb')
            file3 = open('geoma./tr32.jpg', 'rb')
            file4 = open('geoma./tr33.jpg', 'rb')
            bot.send_message(message.from_user.id, 'В каждый треугольник можно вписать окружность и притом только одну.\n \nЕе центр - точка пересечения биссектрис.\n \nФормулы для вычисления радиуса:', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Около каждого треугольника можно описать окружность и притом только одну.\n \nЕе центр - точка пересечения серединных перпендикуляров сторонам треугольника.\n \nФормулы для вычисления радиуса:', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Вычесление радиусов вписанной и описанной окружности:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)

        elif message.text == '8. Прямоугольный треугольник, его свойства и признаки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr16.jpg', 'rb')
            file1 = open('geoma./tr17.jpg', 'rb')
            file2 = open('geoma./tr18.jpg', 'rb')
            file3 = open('geoma./tr21.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Сторона прямоугольного треугольника, противолежащая прямому углу, называется гипотенузой, две другие стороны называются катетами.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Теорема Пифагора:\n \nКвадрат длины гипотенузы равен сумме квадратов длин катетов.\nc² = a² + b²', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Свойства прямоугольного треугольника:\n \nМедиана, проведенная к гипотенузе прямоугольного треугольника, равна половине гипотенузы.\n \nТолько в прямоугольном треугольнике центр описанной окружности лежит на стороне треугольника (совпадает с серединой гипотенузы)', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Признаки прямоугольных треугольников:\n \nЕсли квадрат одной из сторон треугольника равен сумме квадратов двух других сторон, то такой треугольник прямоугольный.\n \nЕсли медиана треугольника равна половине соответствующий ей стороны, то треугольник прямоугольный.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площадь прямоугольного треугольника:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Соотношения в прямоугольном треугольнике:', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)

        elif message.text == '9. Тригонометрические функции острых углов прямоугольного треугольника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr19.jpg', 'rb')
            file1 = open('geoma./tr20.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Синусом острого угла в прямоугольном треугольнике называется отношение противолежащего катета к гипотенузе.\n \nКосинусом острого угла в прямоугольном треугольнике называется отношение прилежащего катета к гипотенузе.\n \nТангенсом острого угла в прямоугольном треугольнике называется отношение противолежащего катета к прилежащему.\n \nКотангенсом острого угла в прямоугольном треугольнике называется отношение прилежащего катета к противолежащему.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)

        elif message.text == '10. Классификация треугольников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr23.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Треугольники классифицируют по сторонам: разносторонние, равнобедренные, равносторонние; а также по углам: остроугольные, тупоугольные и прямоугольные.', reply_markup=markup)

        elif message.text == '11. Равнобедренный треугольник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr24.jpg', 'rb')
            file1 = open('geoma./tr25.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Равнобедренным треугольником называется треугольник с двумя равными сторонами.\n \nОбщая вершина равных (боковых) сторон называется вершиной равнобедренного треугольника, а третья сторона основанием.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Свойства равнобедренного треугольника:\n \nУглы при основании равны.\n \nВысота, проведенная из вершины равнобедренного треугольника, является медианой и биссектрисой (осью симметрии).\n \nВысоты (биссектрисы, медианы), проведенные к боковым сторонам, равны.', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Все эти свойства равнобедренного треугольника обратимы и могут быть использованы для получения признаков равнобедренного треугольника.', reply_markup=markup)

        elif message.text == '12. Правильный треугольник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr26.jpg', 'rb')
            file1 = open('geoma./tr27.jpg', 'rb')
            file2 = open('geoma./tr34.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Правильным (равносторонним) называется треугольник, все стороны которого равны.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Свойства правильного треугольника:\n \n \nВсе углы равностороннего треугольника равны 60°.\n \nТолько в правильном треугольнике совпадают точки пересечения медиан, биссектрис, высот, серединных перпендикуляров. Эта точка называется центром правильного треугольника и является центром вписанной и описанной окружностей.\n \nЦентр правильного треугольника делит его высоты в отношении 2: 1, считая от вершины. Только в правильном треугольнике R = 2r = 2/3h = √3.', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площадь равностороннего треугольника:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)

        elif message.text == '13. Дополнительные теоремы о треугольнике':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./tr28.jpg', 'rb')
            file1 = open('geoma./tr29.jpg', 'rb')
            file2 = open('geoma./tr30.jpg', 'rb')
            file3 = open('geoma./tr31.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Теорема Чевы:\n \nОтрезки АА1, ВВ1, СС1 тогда и только тогда пересекаются в одной точке, когда\n \nAB1/В1С * СА1/А1В * ВС1/С1А = 1', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Теорема Менелая:\n \nТочки А1, В1, С1 тогда и только тогда лежат на одной прямой, когда\n \nAB1/B1C * BC1/C1A * CA1/A1B = 1', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Теорема Стюарта:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Центры вневписанных окружностей лежат в точках пересечения биссектрисы внутреннего и двух биссектрис внешних углов треугольника.', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)

# Параллелограм
        elif message.text == 'Параллелограмм':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("1. Параллелограмм, его свойства и признаки")
            btn2 = types.KeyboardButton('2. Параллелограмм, его дополнительные свойства')
            btn3 = types.KeyboardButton('3. Формулы параллелограмма')
            btn4 = types.KeyboardButton('4. Ромб')
            btn5 = types.KeyboardButton('5. Прямоугольник')
            btn6 = types.KeyboardButton('6. Квадрат')
            btn7 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
            markup.add(btn1, btn2, btn3, btn4,btn5, btn6, btn7)
            bot.send_message(message.from_user.id, 'Выберите интересующую справочную информацию по теме "Параллелограмм"', reply_markup=markup)
            bot.send_message(message.from_user.id, '1. Параллелограмм, его свойства и признаки\n \n2. Параллелограмм, его дополнительные свойства\n \n3. Формулы параллелограмма\n \n4. Ромб\n \n5. Прямоугольник\n \n6. Квадрат', reply_markup=markup)

        elif message.text == '1. Параллелограмм, его свойства и признаки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./par1.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Параллелограммом называется четырехугольник, противоположные стороны которого попарно параллельны.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Свойства параллелограмма:\n \nДиагональ делит параллелограмм на два равных треугольника.\n \nПротивоположные стороны параллелограмма равны.\n \nСумма соседних углов параллелограмма 180°.\n \nДиагонали параллелограмма, пересекаясь, делятся пополам.\n \n', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Признаки параллелограмма:\n \nЕсли в четырехугольнике две противоположные стороны равны и параллельны, то это параллелограмм.\n \nЕсли в четырехугольнике противоположные стороны попарно равны, то это параллелограмм.\n \nЕсли в четырехугольнике диагонали, пересекаясь, делятся пополам, то это параллелограмм.', reply_markup=markup)

        elif message.text == '2. Параллелограмм, его дополнительные свойства':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./par2.jpg', 'rb')
            file2 = open('geoma./par4.jpg', 'rb')
            file1 = open('geoma./par3.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Дополнительные свойства параллелограмма:', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Биссектриса угла параллелограмма отсекает от него равнобедренный треугольник.\n \nБиссектрисы соседних углов параллелограмма перпендикулярны, а биссектрисы противоположных углов параллельны или лежат на одной прямой.\n \nДиагонали параллелограмма делят его на четыре равновеликих треугольника.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Высоты параллелограмма обратно пропорциональны соответственным сторонам параллелограмма.\n \nВысоты параллелограмма, опущенные из одной вершины, образуют угол, равный углу параллелограмма при соседней вершине.', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Середина любого отрезка с концами на противоположных сторонах параллелограмма лежит на прямой, проходящей через середины двух других сторон.', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)

        elif message.text == '3. Формулы параллелограмма':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./par5.jpg', 'rb')
            file1 = open('geoma./par6.jpg', 'rb')
            file2 = open('geoma./par7.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Сумма квадратов диагоналей параллелограмма равна сумме квадратов его четырех сторон.', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Периметр параллелограмма: P = 2a + 2b', reply_markup=markup)

        elif message.text == '4. Ромб':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./par8.jpg', 'rb')
            file1 = open('geoma./par9.jpg', 'rb')
            file2 = open('geoma./par10.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Ромбом называется параллелограмм, все стороны которого равны.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Свойства ромба:\n \nДиагонали ромба взаимно перпендикулярны.\n \nДиагонали ромба лежат на биссектрисах его углов.\n \nВысоты ромба равны.\n \nРомб обладает всеми свойствами параллелограмма.\n \nВ ромб можно вписать окружность.', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Признаки ромба:\n \nЕсли в параллелограмме диагонали взаимно перпендикулярны, то это ромб.\n \nЕсли диагональ параллелограмма лежит на биссектрисе его угла, то это ромб.\n \nЕсли стороны четырехугольника равны, то это ромб.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площадь ромба:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)

        elif message.text == '5. Прямоугольник':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./par11.jpg', 'rb')
            file1 = open('geoma./par12.jpg', 'rb')
            file2 = open('geoma./par13.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Прямоугольником называется параллелограмм, у которого все углы прямые.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Свойства прямоугольника:\n \nПрямоугольник обладает всеми свойствами параллелограмма.\n \nДиагонали прямоугольника равны.\n \nОколо прямоугольника можно описать окружность.', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Признаки прямоугольника:\n \nЕсли в параллелограмме диагонали равны, то это прямоугольник.\n \nЕсли в параллелограмме один угол прямой, то это прямоугольник.\n \nЕсли в четырехугольнике три угла прямые, то это прямоугольник.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площадь прямоугольника:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)

        elif message.text == '6. Квадрат':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./par14.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Квадратом называется прямоугольник, у которого все стороны равны (ромб с прямыми углами).\n \nКвадрат обладает всеми свойствами ромба и прямоугольника.\n \nКвадрат - правильный четырехугольник.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)

# Трапеция
        elif message.text == 'Трапеция':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("1. Трапеция, ее элементы")
            btn2 = types.KeyboardButton('2. Некоторые свойства трапеции')
            btn3 = types.KeyboardButton('3. Равнобокая трапеция')
            btn4 = types.KeyboardButton('4. Теорема о 4 точках трапеция')
            btn5 = types.KeyboardButton('5. Дополнительно о трапеции')
            btn6 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
            bot.send_message(message.from_user.id, 'Выберите интересующую справочную информацию по теме "Трапеция"', reply_markup=markup)
            bot.send_message(message.from_user.id, '1. Трапеция, ее элементы\n \n2. Некоторые свойства трапеции\n \n3. Равнобокая трапеция\n \n4. Теорема о 4 точках трапеция\n \n5. Дополнительно о трапеции', reply_markup=markup)

        elif message.text == '1. Трапеция, ее элементы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./trap1.jpg', 'rb')
            file1 = open('geoma./trap2.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Трапецией называется четырехугольник, две стороны которого параллельны, а две другие не параллельны.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Элементы трапеции:\n \nВС и AD - верхнее и нижнее основания,\nАВ и СD боковые стороны,\nAC и BD - диагонали,\nMN - средняя линия,\nMN = 1/2 (BC + AD).\nВысота трапеции ВВ1 - расстояние между прямыми оснований.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площадь трапеции:', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)

        elif message.text == '2. Некоторые свойства трапеции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./trap7.jpg', 'rb')
            file1 = open('geoma./trap8.jpg', 'rb')
            file2 = open('geoma./trap9.jpg', 'rb')
            file3 = open('geoma./trap10.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Свойства треугольников в трапеции:', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Отрезок, параллельный основаниям, проходящий через точку пересечения диагоналей:', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Отрезок, параллельный основаниям и делящий трапецию на две равновеликие части:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'В трапецию можно вписать окружность тогда и только тогда, когда сумма оснований равна сумме боковых сторон.\n \nBC+AD = AB + CD', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)

        elif message.text == '3. Равнобокая трапеция':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./trap11.jpg', 'rb')
            file1 = open('geoma./trap12.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Равнобокой (равнобедренной) называется трапеция с равными боковыми сторонами.', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Свойства равнобокой трапеции:\n \nДиагонали равнобокой трапеции равны (d1 = d2).\n \nУглы при одном основании равнобокой трапеции равны.\n \nТолько около равнобокой трапеции можно описать окружность; она совпадает с окружностью, описанной около любого треугольника с вершинами в вершинах трапеции. Ее центр лежит на серединном перпендикуляре к основаниям трапеции.\n \nЕсли центр описанной окружности лежит на основании трапеции, то ее диагональ перпендикулярна боковой стороне.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'В равнобедренную трапецию можно вписать окружность, если боковая сторона равна средней линии.', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)

        elif message.text == '4. Теорема о 4 точках трапеция':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./trap6.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Теорема о четырех точках трапеции:\n \nСередины оснований, точка пересечения диагоналей и точка пересечения продолжений боковых сторон трапеции лежат на одной прямой.', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)

        elif message.text == '5. Дополнительно о трапеции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./trap4.jpg', 'rb')
            file1 = open('geoma./trap5.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Разбиение трапеции на параллелограмм и треугольник:', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Построение трапеции по основаниям и боковым сторонам:', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)

# Окружность
        elif message.text == 'Окружность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("1. Окружность кратко")
            btn2 = types.KeyboardButton('2. Круг')
            btn3 = types.KeyboardButton('3. Прямая и окружность')
            btn4 = types.KeyboardButton('4. Две окружности')
            btn5 = types.KeyboardButton('5. Углы и окружность')
            btn6 = types.KeyboardButton('6. Общие касательные двух окружностей')
            btn7 = types.KeyboardButton('7. Вписанная окружность')
            btn8 = types.KeyboardButton('8. Описанная окружность')
            btn9 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
            bot.send_message(message.from_user.id, 'Выберите интересующую справочную информацию по теме "Окружность"', reply_markup=markup)
            bot.send_message(message.from_user.id, '1. Окружность кратко\n \n2. Круг\n \n3. Прямая и окружность\n \n4. Две окружности\n \n5. Углы и окружность\n \n6. Общие касательные двух окружностей\n \n7. Вписанная окружность\n \n8. Описанная окружность',reply_markup=markup)

        elif message.text == '1. Окружность кратко':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr1.jpg', 'rb')
            file1 = open('geoma./kr2.jpg', 'rb')
            file2 = open('geoma./kr3.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Окружностью называется множество точек плоскости, находящихся на одинаковом расстоянии от данной точки (центра окружности)', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Отрезки в окружности:\n \nДля любой точки М окружности с центром О выполняется равенство: ОМ = R (отрезок ОМ - радиус окружности).\n \nОтрезок, соединяющий две точки окружности, называется хордой. Хорда, проходящая через центр окружности, называется диаметром окружности (D).\nD=2R', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Длина окружности:\nС = 2пиR', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Дуга окружности:\n \nЧасть окружности, заключенная между ее двумя точками, называется дугой\n \nДве любые точки М и N окружности определяют на ней две дуги: MkN и MlN. Любую из этих дут стягивает хорда MN.\n \nРавные дуги стягиваются равными хордами', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Длина дуги:', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)

        elif message.text == '2. Круг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr4.jpg', 'rb')
            file1 = open('geoma./kr5.jpg', 'rb')
            file2 = open('geoma./kr6.jpg', 'rb')
            file3 = open('geoma./kr7.jpg', 'rb')
            file4 = open('geoma./kr8.jpg', 'rb')
            file5 = open('geoma./kr9.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Кругом называется часть плоскости, ограниченная окружностью. Для всех точек N круга выполняется неравенство ON ≤  R', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Часть круга, ограниченная дугой и двумя радиусами, называется сектором круга.\n \nЛюбые два радиуса задают два сектора', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Часть круга, ограниченная дугой и стягивающей ее хордой, называется сегментом.\n \nЛюбая хорда делит круг на двасегмента.\n \nСегмент, задаваемый диаметром, называется полукругом', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Диаметр, перпендикулярный хорде, делит эту хорду и стягиваемые ею дуги пополам.\n \nЕсли диаметр делит хорду, не являющуюся диаметром, пополам, то он ей перпендикулярен', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если две хорды AB и CD имеют общую точку М, то\nAM * MB = CM * MD.\n \nДля данной точки М внутри окружности произведение отрезков хорды, на которые делит ее данная точка, есть величина постоянная и равная:\n(R + ОМ)(R - ОМ)', reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Центры всех окружностей, про- ходящих через две данные точки, лежат на серединном перпендикуляре к отрезку с концами в данных точках﻿', reply_markup=markup)
            bot.send_photo(message.chat.id, file5, reply_markup=markup)

        elif message.text == '3. Прямая и окружность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr10.jpg', 'rb')
            file1 = open('geoma./kr11.jpg', 'rb')
            file2 = open('geoma./kr12.jpg', 'rb')
            file3 = open('geoma./kr13.jpg', 'rb')
            file4 = open('geoma./kr14.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Прямая, имеющая с окружностью одну общую точку, называется касательной к окружности; прямая, имеющая с окружностью две общие точки, секущей.\n \nПрямая касается окружности тогда и только тогда, когда диаметр, проходящий через общую точку прямой и окружности, перпендикулярен этой прямой', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если расстояние ОМ от центра окружности до прямой:\n \nбольше радиуса - прямая не имеет с окружностью общих точек,\nравно радиусу - прямая касается окружности,\nМеньше радиуса - высекает на прямой хорду длиной(см фото)', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если окружность касается сторон данного угла, то:\n \nцентр окружности лежит на биссектрисе угла,\nотрезки касательных равны между собой', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если из точки вне окружности к ней проведены касательная и секущая, то квадрат длины отрез- ка касательной равен произведению всего отрезка секущей на его внешнюю часть.\n \nПроизведения длин отрезков секущих, проведенных из одной точки, равны', reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)

        elif message.text == '4. Две окружности':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr15.jpg', 'rb')
            file1 = open('geoma./kr16.jpg', 'rb')
            file2 = open('geoma./kr17.jpg', 'rb')
            file3 = open('geoma./kr18.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Две окружности, имеющие общий центр, называются концентрическими', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)

        elif message.text == '5. Углы и окружность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr19.jpg', 'rb')
            file1 = open('geoma./kr20.jpg', 'rb')
            file2 = open('geoma./kr21.jpg', 'rb')
            file3 = open('geoma./kr22.jpg', 'rb')
            file4 = open('geoma./kr23.jpg', 'rb')
            file5 = open('geoma./kr24.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Центральным углом в окружности называется угол между двумя ее радиусами.\n \nГрадусная мера центрального угла равна градусной мере дуги, на которую он опирается (измеряется дугой, на которую он опирается)', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Угол, вершина которого лежит на окружности, а стороны содержат хорды, называется вписанным углом.\n \nВписанный угол измеряется половиной дуги, на которую он опирается.\n \nВписанный угол, опирающийся на диаметр, прямой.\n \nВписанные углы, опирающиеся на одну и ту же дугу, равны', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Вписанные углы, опирающиеся на одну и ту же хорду, либо равны, либо их сумма 180°', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Угол между хордой и касательной измеряется половиной содержащейся в этом угле дуги окружности', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Угол с вершиной внутри окружности (угол между двумя хордами)', reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Угол с вершиной вне окружности (угол между двумя секущими)', reply_markup=markup)
            bot.send_photo(message.chat.id, file5, reply_markup=markup)

        elif message.text == '6. Общие касательные двух окружностей':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr25.jpg', 'rb')
            file1 = open('geoma./kr26.jpg', 'rb')
            file2 = open('geoma./kr27.jpg', 'rb')
            file3 = open('geoma./kr28.jpg', 'rb')
            file4 = open('geoma./kr29.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если одна окружность касается другой изнутри, то у них одна общая касательная', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если окружности пересекаются, то у них две общих касательных (две внешних касательных, внутренних касательных нет)', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Если одна окружность лежит внутри другой, то общих касательных нет', reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)

        elif message.text == '7. Вписанная окружность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr30.jpg', 'rb')
            file1 = open('geoma./kr31.jpg', 'rb')
            file2 = open('geoma./kr32.jpg', 'rb')
            file3 = open('geoma./kr33.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Окружность называется вписанной в многоугольник, если она касается всех его сторон.\n \nЕе центр должен принадлежать всем биссектрисам внутренних углов этого многоугольника. Ее радиус можно вычислить по формуле r = S/p, где Ѕ - площадь, а р - полупериметр многоугольника.\n \nНе во всякий многоугольник можно вписать окружность', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'В любой треугольник можно вписать окружность и притом только одну.Ее центр лежит в точке пересечения биссектрис внутренних углов, а радиус может быть вычислен по формулам(см. фото): ', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'В выпуклый четырехугольник можно вписать окружность тогда и только тогда, когда суммы длин его противоположных сторон равны', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)

        elif message.text == '8. Описанная окружность':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./kr34.jpg', 'rb')
            file1 = open('geoma./kr35.jpg', 'rb')
            file2 = open('geoma./kr36.jpg', 'rb')
            file3 = open('geoma./kr37.jpg', 'rb')
            file4 = open('geoma./kr38.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Окружность называется описанной около многоугольника, если она проходит через все его вершины. Ее центр лежит на всех серединных перпендикулярах сторон (и диагоналей) этого многоугольника. Радиус вычисляется как радиус окружности, описанной около треугольника, определенного любыми тремя вершинами данного многоугольника', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Около любого треугольника можно описать окружность и притом только одну. Ее центр лежит в точке пересечения серединных перпендикуляров сторон треугольника, а радиус вычисляется по формулам(см. фото):', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Около четырехугольника можно описать окружность тогда и только тогда, когда сумма его противоположных углов равна 180°', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Теорема Птолемея\n \nВо вписанном четырехугольнике произведение диагоналей равно сумме произведений его противоположных сторон.\nAC * BD = AB * CD + BC * AD', reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)


# Площадь
        elif message.text == 'Площади':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn2 = types.KeyboardButton("1. Площадь квадрата")
            btn3 = types.KeyboardButton('2. Площадь прямоугольника')
            btn4 = types.KeyboardButton('3. Площадь параллелограмма')
            btn5 = types.KeyboardButton('4. Площадь треугольника.')
            btn6 = types.KeyboardButton('5. Некоторые соотношения площадей треугольников')
            btn7 = types.KeyboardButton('6. Площадь трапеции')
            btn8 = types.KeyboardButton('7. Соотношения площадей, связанных с трапецией')
            btn9 = types.KeyboardButton('8. Площадь правильного n - угольника')
            btn10 = types.KeyboardButton('9. Площадь круга')
            btn11 = types.KeyboardButton('Вернуться к выбору раздела Планиметрии')
            markup.add( btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
            bot.send_message(message.from_user.id, 'Площади равных фигур равны.\n \nЕсли фигура составлена из нескольких фигур, не имеющих общих внутренних точек, то ее площадь равна сумме площадей этих фигур.\n \nФигуры, имеющие равные площади, называются равновеликими', reply_markup=markup)
            bot.send_message(message.from_user.id, 'Выберите интересующую справочную информацию по теме "Площадь"', reply_markup=markup)
            bot.send_message(message.from_user.id, '1. Площадь квадрата\n \n2. Площадь прямоугольника\n \n3. Площадь параллелограмма\n \n4. Площадь треугольника\n \n5. Некоторые соотношения площадей треугольников\n \n6. Площадь трапеции\n \n7. Соотношения площадей, связанных с трапецией\n \n8. Площадь правильного n - угольника\n \n9. Площадь круга', reply_markup=markup)

        elif message.text == '9. Площадь круга':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pl17.jpg', 'rb')
            file1 = open('geoma./pl18.jpg', 'rb')
            file2 = open('geoma./pl19.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)

        elif message.text == '8. Площадь правильного n - угольника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pl16.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)

        elif message.text == '6. Площадь трапеции':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pl11.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)

        elif message.text == '7. Соотношения площадей, связанных с трапецией':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pl12.jpg', 'rb')
            file1 = open('geoma./pl13.jpg', 'rb')
            file2 = open('geoma./pl14.jpg', 'rb')
            file3 = open('geoma./pl15.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)

        elif message.text == '5. Некоторые соотношения площадей треугольников':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pl4.jpg', 'rb')
            file1 = open('geoma./pl5.jpg', 'rb')
            file2 = open('geoma./pl6.jpg', 'rb')
            file3 = open('geoma./pl7.jpg', 'rb')
            file4 = open('geoma./pl8.jpg', 'rb')
            bot.send_message(message.from_user.id, 'Площади подобных треугольников (фигур) относятся как квадраты сходственных элементов (сторон, медиан, высот и т. п.), их отношение равно квадрату коэффициента подобия', reply_markup=markup)
            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площади треугольников, имеющих равные высоты (общую высоту), относятся как стороны, соответствующие этим высотам', reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площади треугольников, имеющих равные стороны, относятся как соответствующие этим сторонам высоты', reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Площади треугольников, имеющих равный угол (или общий угол), относятся как произведения сторон, содержащих этот угол', reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)
            bot.send_message(message.from_user.id, 'Медиана делит треугольник на два равновеликих треугольника.\n \nТри медианы треугольника делят его на шесть равновеликих треугольников', reply_markup=markup)
            bot.send_photo(message.chat.id, file4, reply_markup=markup)

        elif message.text == '4. Площадь треугольника.':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pl2.jpg', 'rb')
            file1 = open('geoma./pl3.jpg', 'rb')
            file2 = open('geoma./pl9.jpg', 'rb')
            file3 = open('geoma./pl10.jpg', 'rb')

            bot.send_photo(message.chat.id, file, reply_markup=markup)
            bot.send_photo(message.chat.id, file1, reply_markup=markup)
            bot.send_photo(message.chat.id, file2, reply_markup=markup)
            bot.send_photo(message.chat.id, file3, reply_markup=markup)

        elif message.text == '3. Площадь параллелограмма':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            file = open('geoma./pl1.jpg', 'rb')
            bot.send_photo(message.chat.id, file, reply_markup=markup)

        elif message.text == '2. Площадь прямоугольника':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            bot.send_message(message.from_user.id, 'S = a * b', reply_markup=markup)

        elif message.text == '1. Площадь квадрата':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('')
            markup.add(btn1)
            bot.send_message(message.from_user.id, 'S = a * a', reply_markup=markup)















bot.polling(none_stop=True)
