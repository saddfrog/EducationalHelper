import telebot
from telebot import types
# token = '1658623331:AAGUl5GPP_TqErO3RVEvPEzThPLDPBqzoLU'
token = '1624112260:AAGEbBjhjduaafTsT3LKN1wY_X1mMbGP_z8'
def main_b():
    buttons = types.InlineKeyboardMarkup()   
    buttons.add(types.InlineKeyboardButton(text='Теория', callback_data='theory'), types.InlineKeyboardButton(text='Решить задачу', callback_data='solver'))
    return buttons
def theory_b():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(types.InlineKeyboardButton(text='Комбинаторика', callback_data='theory_comb'), types.InlineKeyboardButton(text='Множества', callback_data='theory_mn'), types.InlineKeyboardButton(text='◀️ Назад', callback_data='main'))       
    return keyboard
def solver_b():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(types.InlineKeyboardButton(text='Комбинаторика', callback_data='comb'), types.InlineKeyboardButton(text='Множества', callback_data='solve_mn'), types.InlineKeyboardButton(text='◀️ Назад', callback_data='main'))              
    return keyboard
def comb_b():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(types.InlineKeyboardButton("Помочь с определением формулы", callback_data="solve_comb"), types.InlineKeyboardButton("Выбрать формулу самостоятельно", callback_data="comb_menu"),
    types.InlineKeyboardButton(text='◀️  Назад', callback_data='solver'),types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup

def first_q():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("✅  Да", callback_data="1"), types.InlineKeyboardButton("❌  Нет", callback_data="0"), types.InlineKeyboardButton("◀️  Назад", callback_data="comb"), types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup
def second_q():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("✅  Да", callback_data="11"), types.InlineKeyboardButton("❌  Нет", callback_data="10"), types.InlineKeyboardButton("◀️  Назад", callback_data="solve_comb"), types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup
def third_q():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("✅  Да", callback_data="111"), types.InlineKeyboardButton("❌  Нет", callback_data="110"), types.InlineKeyboardButton("◀️  Назад", callback_data="1"), types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup
def fourth_q():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("✅  Да", callback_data="101"), types.InlineKeyboardButton("❌  Нет", callback_data="100"), types.InlineKeyboardButton("◀️  Назад", callback_data="1"), types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup
def fith_q():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("✅  Да", callback_data="01"), types.InlineKeyboardButton("❌  Нет", callback_data="00"), types.InlineKeyboardButton("◀️  Назад", callback_data="solver"), types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup

def back_theory():
    answer = types.InlineKeyboardMarkup()
    answer.row_width = 1
    answer.add(types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'), types.InlineKeyboardButton(text='◀️  Назад', callback_data='theory')) 
    return answer    
def res_comb():
    back = types.InlineKeyboardMarkup()   
    back.row_width = 1
    back.add(types.InlineKeyboardButton(text='◀️  Ввести еще раз значения для формулы', callback_data='again'), types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'), types.InlineKeyboardButton(text='◀️  Меню формул', callback_data='comb_menu'))
    return back


def mnozh():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(types.InlineKeyboardButton("2", callback_data="2Res"), types.InlineKeyboardButton("3", callback_data="3Res"), types.InlineKeyboardButton("4", callback_data="4Res"), types.InlineKeyboardButton("◀️  Назад", callback_data="solver"))
    markup.add(types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup 

input_users = {}
saved_message_id = {}
input_history = {}
save_message = {}
users_steps = {}
saved_message_text = {}
saved_input_users = {}
texts = {'00':'*Сочетания*\nФормула:\n `n!/(r!(n - r)!)`\n', '01':'*Сочетания с повторениями*\nФормула:\n`C^r(n + r - 1) = ( n + r - 1)!/(r!*(n - 1)!)`\n', '100':'*Размещения*\nФормула:\n`A^r(n)=n!/(n - r)!`', '101':'*Размещения с повторениями*\nФормула:\n`A^r(n)=n^r`', '110':'*Перестановки*\nФормула:\n`Pn = n!`', '111':'*Перестановки с повторениями*\nФормула:\n`n!/(n1!*n2!*...*nk!)`'}         
r_once = ['00','01','100','101']
type_mnozh = {'2':'2\n|A∪B|=|A|+|B|−|A∩B|','3':'3\n|A∪B∪C|=|A|+|B|+|C|−|A∩B|−|A∩C|−|B∩C|+|A∩B∩C|','4':'4\n|A∪B∪C∪D|=|A|+|B|+|C|+|D|−|A∩B|−|A∩C|−|A∩D|−|B∩C|−|B∩D|−|C∩D|+|A∩B∩C|+|A∩C∩D|+|A∩B∩D|+|B∩C∩D|+|A∩B∩C∩D|'}
texts_menu = {'00':'Сочетания','01':'Сочетания с повторениями', '100':'Размещения', '101':'Размещения с повторениями', '110':'Перестановки', '111':'Перестановки с повторениями'}         
def comb_menu_b():

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(texts_menu['00'], callback_data="00"), types.InlineKeyboardButton(texts_menu['01'], callback_data="01"))
    markup.add(types.InlineKeyboardButton(texts_menu['100'], callback_data="100"), types.InlineKeyboardButton(texts_menu['101'], callback_data="101"))
    markup.add(types.InlineKeyboardButton(texts_menu['110'], callback_data="110"), types.InlineKeyboardButton(texts_menu['111'], callback_data="111"))
    markup.add(types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    markup.add(types.InlineKeyboardButton(text='◀️  Назад', callback_data='comb'))
    return markup

def back_to_mnozh_menu_b():

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='◀️  Назад', callback_data='solve_mn'))
    markup.add(types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup     

def sum_list(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + sum_list(numList[1:])

def mnozh_answer():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='◀️  Ввести еще раз значения',callback_data='solve_mn'))
    markup.add(types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    return markup     

def mnozh_answer_beta():
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton(text='◀️  Ввести еще раз значения',callback_data='solve_mn'))
    # markup.add(types.InlineKeyboardButton(text='◀️  Главное меню', callback_data='main'))
    # return markup     

    return     