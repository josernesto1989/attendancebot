#bot = telegram.Bot('870389483:AAE6i7fBhPR88g_OL363CMx7_hp9KkUu3dQ')
#!/usr/bin/python3
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################

asistencia = [
['Jose','A'],
['Alayn','A'],
['Pedro','A'],
['Osmanys','A'],
['Ronald','A'],
['Tania','A'],
['Michel','A'],
['Yaiselin','A'],
['Yarima','A'],
['Jisel','A'],
['Yaneisys','A'],
['Alejandro','A'],
['Reinier ON','A'],
['Yandy','A'],
['Fidel D.','A'],
['Andres','A'],
['Luis R.','A']
]
posAsistencia = 0
isFirst = True


def start(update: Update, context: CallbackContext):
  update.message.reply_text('hola')
  # update.message.reply_text(main_menu_message(),
  #                           reply_markup=main_menu_keyboard())

#Comando para chequear asistencia /asist
def asist(update: Update, context: CallbackContext):
  global asistencia
  update.message.reply_text('Registre la asistencia',
                            reply_markup=InlineKeyboardMarkup(createListMenu(asistencia)))

def changeAsist(update: Update, context: CallbackContext):
  global asistencia
  query = update.callback_query
  args = query.data.split()
  if args.__len__() > 1:
    pos = int(args[1])
    if asistencia[pos][1] == 'A':
      asistencia[pos][1] = "P" 
    else:
      asistencia[pos][1] = 'A'
  context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text='Registre la asistencia',
                        reply_markup=InlineKeyboardMarkup(createListMenu(asistencia)))
 

def createListMenu(asistList):
  respList = []
  currentPos = 0
  for person in asistList:
    cbData = 'chAsist ' + str(currentPos)
    currentPos = currentPos +1
    indicator = '🆗'
    if person[1] == 'A':
      indicator = '🔴' 
    respList.append([InlineKeyboardButton(person[0]+' '+ indicator, callback_data=cbData)])
  respList.append(([InlineKeyboardButton("Enviar",callback_data="endAsist")]))
  return respList


def printAsistencia(update, context):
  query = update.callback_query
  global asistencia
  global posAsistencia
  global isFirst
  isFirst = True
  posAsistencia = 0
  query = update.callback_query
  presentList = [] 
  notPresentList = []
  for person in asistencia:
    presentList.append(person[0])  if person[1]=='P' else notPresentList.append(person[0])
  output ='Presentes:\n'
  for person in presentList:
    output = output + person +'\n'
  output = output +'\n Ausentes:\n'
  for person in notPresentList:
    output = output + person +'\n' 
  context.bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=output)




############################# Handlers #########################################
updater = Updater('870389483:AAE6i7fBhPR88g_OL363CMx7_hp9KkUu3dQ', use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('asist', asist))
dp.add_handler(CallbackQueryHandler(changeAsist, pattern='chAsist'))
dp.add_handler(CallbackQueryHandler(printAsistencia, pattern='endAsist'))

updater.start_polling()
updater.idle()
################################################################################