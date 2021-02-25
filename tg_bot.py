import telebot
from telebot import types
import math
from functions_for_bot import *
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    buttons = types.InlineKeyboardMarkup()   
    buttons.add(types.InlineKeyboardButton(text='Решить задачу', callback_data='solver'), types.InlineKeyboardButton(text='Теория', callback_data='theory'))
    bot.send_message(message.from_user.id, "Привет)\nВ боте реализованы алгоритмы, позволяющие решать задачи:\n 1) на Формулы включений-исключений\n 2) по Комбинаторике\nЕще реализована возможность получения теоретической справки", reply_markup=buttons)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.from_user.id, "Что бы начать работу с ботом введите команду /start")

@bot.message_handler(content_types=['text'])
def message_handler(message):
    user_id = message.chat.id
    if user_id in input_users: 
  
        if input_users[user_id][:-3] in type_mnozh:
            if message.text.isdigit():
                input_history[user_id].append(int(message.text))
                lenth = len(input_history[user_id])
                print(input_users[user_id])
                if input_users[user_id][:-3] == '2':
                    if lenth == 1:
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text+'\n---------\nВведите значение множества 2', message_id=saved_message_id[user_id]-lenth+1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text+'\nЗначение множества 2: '
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id
                    if lenth == 2:
                        print(saved_message_id[user_id])                        
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text+'\n----------\nВведите значение пересечения множеств 1 и 2', message_id=saved_message_id[user_id]-1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text+'\nЗначение значение пересечения множеств 1 и 2: '
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)     
                        saved_message_id[user_id] = message.id                                          
                    if lenth == 3:   
                        print(input_history[user_id])                        
                        inputs = input_history[user_id]
                        Plus = sum_list(inputs[:2])
                        Minus = int(inputs[-1])
                        Res = str(Plus - Minus)
                        if int(Res) > 0:
                            bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text+'\n----------\nОтвет: ' + Res, message_id=saved_message_id[user_id]-2)
                            bot.send_message(text='-----',chat_id=message.chat.id,reply_markup=mnozh_answer())
                        else:
                            bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text+'\n----------\nОтвет: вы ввели неверные данные, попробуйте еще раз' , message_id=saved_message_id[user_id]-2)
                            bot.send_message(text='-----',chat_id=message.chat.id,reply_markup=mnozh_answer())
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)     
                        input_history[user_id] = []   
                        saved_message_id[user_id] = 0
                        saved_message_text[user_id] = ''
                        input_users[user_id] = ''
                if input_users[user_id][:-3] == '3':
                    if lenth in [1,2]:
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение множества ' + str(lenth + 1), message_id=saved_message_id[user_id]+(-1)**(lenth+1))
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text  + '\nЗначение множества '+str(lenth + 1) +': ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id     
                    if lenth in [3,4]:
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text + '\n---------\nВведите значение пересечения множеств 1 и ' + str(lenth - 1), message_id=saved_message_id[user_id]-2)
                        saved_message_text[user_id] = saved_message_text[user_id]+ message.text +'\nЗначение пересечения множеств 1 и '+ str(lenth - 1) +': ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                    if lenth == 5:  
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text + '\n---------\nВведите значение пересечения множеств 2 и 3', message_id=saved_message_id[user_id]-2)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text +'\nЗначение пересечения множеств 2 и 3: ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)                    
                    if lenth == 6:  
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text + '\n---------\nВведите значение пересечения множеств 1, 2 и 3', message_id=saved_message_id[user_id]-2)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text +'\nЗначение пересечения множеств 1, 2 и 3: ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)     
                    if lenth == 7:   
                        inputs = input_history[user_id]
                        Plus = sum_list(inputs[:3]+inputs[-1:]) 
                        Minus = sum_list(inputs[3:6])
                        print(Plus,Minus)
                        Res = str(Plus - Minus)
                        if int(Res) > 0:
                            bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text+'\n----------\nОтвет: ' + Res, message_id=saved_message_id[user_id]-2)
                            bot.send_message(text='-----',chat_id=message.chat.id,reply_markup=mnozh_answer())
                        else:
                            bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text+'\n----------\nОтвет: вы ввели неверные данные, попробуйте еще раз' , message_id=saved_message_id[user_id]-2)
                            bot.send_message(text='-----',chat_id=message.chat.id,reply_markup=mnozh_answer())
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)     
                        input_history[user_id] = []      
                        saved_message_id[user_id] = 0
                        saved_message_text[user_id] = ''
                        input_users[user_id] = ''                                               
                if input_users[user_id][:-3] == '4':
                    if lenth in range(3):
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение множества ' + str(lenth + 1), message_id=saved_message_id[user_id]+(-1)**(lenth+1))
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text  + '\nЗначение множества '+str(lenth + 1) +': ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id     
                    if lenth == 3:
                        bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение множества 4', message_id=saved_message_id[user_id]-2)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text  + '\nЗначение множества 4: ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id                           
                    if lenth in range(4,7):
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение пересечения множеств 1 и ' + str(lenth - 2), message_id=saved_message_id[user_id]-lenth +1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text  + '\nЗначение пересечения множеств 1 и '+str(lenth - 2) +': ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id                         
                    if lenth in range(7,9):
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение пересечения множеств 2 и ' + str(lenth - 4), message_id=saved_message_id[user_id]-lenth +1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text  + '\nЗначение пересечения множеств 2 и '+str(lenth - 4) +': ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id                           
                    if lenth == 9:
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение пересечения множеств 3 и 4', message_id=saved_message_id[user_id]-lenth +1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text  + '\nЗначение пересечения множеств 3 и 4: ' 
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id                             
                    if lenth in range(10,12):
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение пересечения множеств 1, 2 и ' + str(lenth-7), message_id=saved_message_id[user_id]-lenth +1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text  + '\nЗначение пересечения множеств 1, 2 и ' + str(lenth-7) + ': '
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id                     
                    if lenth in range(12,14):
                        bot.edit_message_text(chat_id=message.chat.id,reply_markup=mnozh_answer_beta(), text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение пересечения множеств ' + str(lenth-11) +  ', 3 и 4', message_id=saved_message_id[user_id]-lenth +1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text + '\nЗначение пересечения множеств ' + str(lenth - 11) + ', 3 и 4: '
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id 
                        print(saved_message_id[user_id])                        
                    if lenth == 14:
                        bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text +'\n---------\nВведите значение пересечения множеств 1, 2, 3 и 4',reply_markup=mnozh_answer_beta(), message_id=saved_message_id[user_id]-lenth +1)
                        saved_message_text[user_id] = saved_message_text[user_id] + message.text + '\nЗначение пересечения множеств 1, 2, 3 и 4: '
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)
                        saved_message_id[user_id] = message.id    
                        print(saved_message_id[user_id])                    
                    if lenth == 15:
                        print(saved_message_id[user_id])
                        inputs = input_history[user_id]
                        Plus = sum_list(inputs[:4] + inputs[10:14]) 
                        Minus = sum_list(inputs[4:10] + inputs[-1:])
                        print(Plus,Minus)
                        Res = str(Plus - Minus)
                        if int(Res) > 0:
                            bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text+'\n----------\nОтвет: ' + Res, message_id=saved_message_id[user_id]-lenth +1)
                            bot.send_message(text='-----',chat_id=message.chat.id,reply_markup=mnozh_answer())
                        else:
                            bot.edit_message_text(chat_id=message.chat.id, text=saved_message_text[user_id] + message.text+'\n----------\nОтвет: вы ввели неверные данные, попробуйте еще раз' , message_id=saved_message_id[user_id]-lenth +1)
                            bot.send_message(text='-----',chat_id=message.chat.id,reply_markup=mnozh_answer())
                        bot.delete_message(chat_id=message.chat.id,message_id=message.id)     
                        input_history[user_id] = []   
                        saved_message_id[user_id] = 0
                        saved_message_text[user_id] = ''
                        input_users[user_id] = ''  
            else:
                bot.send_message(message.from_user.id,'Вы ввели неправильно, вводите все заново :)',reply_markup=mnozh_answer())                                     
        if input_users[user_id] in texts:
            if message.text.isdigit():
                input_history[user_id].append(int(message.text))            
                if len(input_history[user_id]) > 1 and input_users[user_id] in r_once:
                    flag = True
                else:
                    flag = False
                if input_users[user_id] == '111':
                    if len(input_history[user_id]) == 1:
                        bot.send_message(message.from_user.id,'*Указание:* количество выбранных элементов должно равняться общему количеству элементов\nк примеру: n = 3, количество выбранных элементов х1, х2, х3', parse_mode="MARKDOWN")
                    if  len(input_history[user_id]) != input_history[user_id][0] + 1:
                        bot.send_message(message.from_user.id,'Осталось ввести количество элементов '+str(int(input_history[user_id][0]) + 1-len(input_history[user_id]))+' типов ')
                    if len(input_history[user_id]) == input_history[user_id][0] + 1:
                        n = input_history[user_id][0]
                        all_ = 1
                        sum_ = 0
                        for i in range(n-1):
                            number = input_history[user_id][i]        
                            all_ = all_*math.factorial(number)
                            sum_ += number 
                            Res = str(int(math.factorial(sum_)/all_))
                        flag = True 
                if input_users[user_id] in r_once and len(input_history[user_id]) == 1:
                    bot.send_message(message.from_user.id, "Введите значение выбранных элементов *r*", parse_mode="MARKDOWN")
                if input_users[user_id] == '00' and flag:
                    n = input_history[user_id][0]
                    r = input_history[user_id][1]
                    if n >= r:
                        Res = str(int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r))))
                    else:
                        Res = 'Вы ввели неправильно, r не может быть больше n'

                if input_users[user_id] == '01' and flag:
                    n = input_history[user_id][0]
                    r = input_history[user_id][1]            
                    if n == 0 :
                        Res ='Вы ввели неправильно, r не может быть больше n'
                    else:
                        Res = str(int(math.factorial(n + r - 1) / (math.factorial(r) * math.factorial(n - 1))))
                
                if input_users[user_id] == '100' and flag:
                    n = input_history[user_id][0]
                    r = input_history[user_id][1]  
                    if n >= r: 
                        Res = str(int(math.factorial(n) / math.factorial(n - r)))
                    else:
                        Res = 'Вы ввели неправильно, r не может быть больше n'
                
                if input_users[user_id] == '101' and flag:
                    n = input_history[user_id][0]
                    r = input_history[user_id][1]   
                    Res = str(int(n**r))

                if input_users[user_id] == '110':
                    n = input_history[user_id][0]
                    Res = str(int(math.factorial(n)))
                    flag = True
                if flag:
                    bot.send_message(message.from_user.id,'Ответ: ' + Res)
                    bot.send_message(message.from_user.id,'---' , reply_markup=res_comb())
                    input_history[user_id] = []   
                    saved_input_users[user_id] = input_users[user_id]  
                    print(input_users[user_id])
                    input_users[user_id] = ''
                    print(input_users[user_id])

            else:
                bot.send_message(message.from_user.id,'Вы ввели неправильно, попробуйте ещё раз')        




@bot.callback_query_handler(func=lambda call: True)    
def call_back(call):
    if call.data == 'main':
       bot.edit_message_text("Привет)\nВ боте реализованы алгоритмы, позволяющие решить задачи:\n 1)на Формулы включений-исключений\n 2)по Комбинаторике\nЕще реализована возможность получения теоретической справки", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=main_b())    

    if call.data == 'theory':
     bot.edit_message_text(text='*Теория*\nВыберите интересующую вас тему:', parse_mode="MARKDOWN", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=theory_b())            

    if call.data == "theory_comb":   
        bot.edit_message_text("*Комбинаторика* – раздел математики, который изучает задачи выбора и расположения элементов из некоторого основного множества в соответствии с заданными правилами. Формулы и принципы комбинаторики используются в теории вероятностей для подсчета вероятности случайных событий и, соответственно, получения законов распределения случайных величин\nhttps://ya-znau.ru/znaniya/zn/80", parse_mode="MARKDOWN", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=back_theory())
    elif call.data == "theory_mn":
        bot.edit_message_text("*Формула включений-исключений* — комбинаторная формула, позволяющая определить мощность объединения конечного числа *множеств*, которые в общем случае могут пересекаться друг с другом \nhttps://foxford.ru/wiki/matematika/formula-vklyucheniya-isklyucheniya", parse_mode="MARKDOWN", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=back_theory())

    if call.data == 'solver':
      bot.edit_message_text(text='*Решение*\nВыберите интересующую вас тему:', parse_mode="MARKDOWN", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=solver_b())            
 
    if call.data == 'comb':
        bot.edit_message_text(text='Вы знаете какую формулу использовать или вам нужна помощь?', chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=comb_b())            
    if call.data == 'comb_menu':
        bot.edit_message_text(text='Выберите нужную вам формулу', chat_id=call.message.chat.id, parse_mode="MARKDOWN",message_id=call.message.id, reply_markup=comb_menu_b())            

    if call.data == "solve_comb":  
        bot.edit_message_text("*Указание*: для определения вида формулы ответьте на следующие вопросы\nПорядок важен?", parse_mode="MARKDOWN", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=first_q())    
    if call.data == "1":
        bot.edit_message_text("Нужно выбрать все n элементов?", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=second_q())
    if call.data == "0":
        bot.edit_message_text("Повторения есть?", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=fith_q())  
    if call.data == '11':
        bot.edit_message_text("Повторения есть?", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=third_q())
    if call.data == '10':
        bot.edit_message_text("Повторения есть?",chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=fourth_q())   
    if call.data in texts:
        answer = types.InlineKeyboardMarkup()
        answer.row_width = 2
        answer.add(types.InlineKeyboardButton(text='Решить по формуле', callback_data='Res'),types.InlineKeyboardButton(text='◀️  Меню всех формул', callback_data='comb_menu'), types.InlineKeyboardButton(text='◀️  Выбор с помощью вопросов', callback_data='solve_comb'), types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
        if len(call.data) == 2:
            answer.add(types.InlineKeyboardButton(text='◀️  Назад', callback_data='0'))     
        else:
            answer.add(types.InlineKeyboardButton(text='◀️  Назад', callback_data=call.data[:2]))  
        input_users[call.message.chat.id] = call.data 
        saved_message_id[call.message.chat.id] = call.message.id
        input_history[call.message.chat.id] = []
        saved_message_text[call.message.chat.id] = call.data
        bot.edit_message_text(text = texts[call.data], chat_id=call.message.chat.id, message_id=call.message.id, parse_mode="MARKDOWN", reply_markup=answer)       
    if call.data == 'Res':
        user_id = call.message.chat.id
        message_for_user = saved_message_id[user_id]
        text_for_user = saved_message_text[user_id]
        bot.delete_message(chat_id=user_id, message_id=message_for_user)
        bot.send_message(text = texts[text_for_user], chat_id=user_id, parse_mode="MARKDOWN")
        # input_users[user_id]
        bot.send_message(call.message.chat.id, "Введите значение всех элементов *n*", parse_mode="MARKDOWN")  
    if call.data == 'again':
        # input_users[call.message.chat.id] = call.data 
        # print()
        input_users[call.message.chat.id] = saved_input_users[call.message.chat.id]
        user_id = call.message.chat.id
        print(input_users[user_id])
        text_for_user = saved_message_text[user_id]
        bot.send_message(call.message.chat.id, "Введите значение всех элементов *n*", parse_mode="MARKDOWN") 
        bot.edit_message_text(text = texts[text_for_user], chat_id=user_id, message_id=call.message.id, parse_mode="MARKDOWN") 
       
    if call.data == 'solve_mn':
        bot.edit_message_text("Выберите общее количество множеств", chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=mnozh())
        input_history[call.message.chat.id] = []      
        saved_message_id[call.message.chat.id] = 0
        saved_message_text[call.message.chat.id] = ''
        input_users[call.message.chat.id] = ''          
    if call.data[:-3].isdigit():
        input_history[call.message.chat.id] = []   
        input_users[call.message.chat.id] = call.data
        saved_message_id[call.message.chat.id] = call.message.id 
        saved_message_text[call.message.chat.id] =  "Значение множества 1: "
        bot.edit_message_text("*общее количество множеств: " + type_mnozh[input_users[call.message.chat.id][:-3]] + '*', chat_id=call.message.chat.id, parse_mode="MARKDOWN", message_id=call.message.id) 
        bot.send_message(call.message.chat.id, "Введите значение множества 1",reply_markup=mnozh_answer())   

    bot.answer_callback_query(call.id)

bot.polling(none_stop=True, interval=0)