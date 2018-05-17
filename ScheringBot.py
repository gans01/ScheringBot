import telebot
from telebot import types

token = "{YOUR_BOT_TOKEN}" # It's safer to use another script and import token from there.
bot = telebot.TeleBot(token)

#### TELEGRAM BOT TEMPLATE ####

# Functions:
# 1: Quick reply buttons. Example:
# bot.send_message(message.chat.id, text, reply_markup = newButton("Button 1", "Button 2")

# 2: Quick inline buttons with callback. Ex:
# -..-, reply_markup = InlineCallback( ("Text 1 goes here", "Callback data 1 here"), ("Text 2 goes here", "Callback data 2 here") ) ## mind the double brackets and 2 arguments inside each bracket pair.

# 3: Quick inline buttons with URL work the same way.

# Edit callback data functions in callback_query_handler.

#       Variables that you can edit:        ############################################################################

Buttons_In_A_Row = 2 ## How many buttons to insert in a row for economy of space
commands = { # Add as much as you like
    "command1":"command1 description",
    "command2":"command 2 description",
    "cmd3":"cmd3 description",
}

########################################################################################################################
### Your variables ###



### Pre-Made Functions ###

#This function creates reply markup buttons. By clicking on one, a message handler for text content is fired. Use "if text == {button_text}:"
def newButton(*args):
    mrkup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=Buttons_In_A_Row)
    buts = []
    for arg in args:
        but = types.KeyboardButton(arg)
        buts.append(but)
    mrkup.add(*buts)
    return mrkup

#This function creates inline buttons with callback data. Inside callback_query_handler use the same data string to identify and fire a desired function.
# Example: If your button data is "data1", then in callback query handler use "if data == "data1":"
def InlineCallback(*args):
    mrkup = types.InlineKeyboardMarkup()
    buts = []
    for arg1, arg2 in args:
        but = types.InlineKeyboardButton(text = arg1, callback_data=arg2)
        buts.append(but)
    mrkup.add(*buts)
    return mrkup

#This function creates inline buttons with URLs. By clicking on one, a user is prompted to enter given website.
def InlineUrl(*args):
    mrkup = types.InlineKeyboardMarkup()
    buts = []
    for arg1, arg2 in args:
        but = types.InlineKeyboardButton(text = arg1, url=arg2)
        buts.append(but)
    mrkup.add(*buts)
    return mrkup

#This function is used to know when a bot is running.
def initiate():
    print("The bot is running!")


### Your Functions ###

def myFunction(arg1, arg2):
    return arg1, arg2


### Preparation functions ###

initiate()
myFunction("arg1", "arg2")


########################################################################################################################

### Handlers ###

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    data = call.data
    message = call.message
    chatid = message.chat.id

    if data == "data1":
        print("Function for data1 callback here")
    elif data == "data2":
        print("Function for data1 callback here")
    else:
        print("No callback found")

@bot.message_handler(commands=["start"])
def handle_start(mes):
    bot.send_message(mes.chat.id, "Welcome message 1. (Copy and paste for more welcome messages")

@bot.message_handler(commands=['help'])
def handle_help(mes):
    help_text = "The following commands are available: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(mes.chat.id, help_text)

@bot.message_handler(content_types=['text'])
def handle_text(mes):
    # DEBUGGING
    print("["+mes.from_who.first_name+"]: " + str(mes.text))
    # DEBUGGING
    text = mes.text

    if text == "Hello":
        print("What happens if user enters \"Hello\". Combine with reply markups to create functions")
    elif text == "Bye":
        print("What happens if user enters \"Bye\". Combine with reply markups to create functions")
    else:
        bot.send_message(mes.chat.id, "Unknown command. See \"/help\" for available commands!")


bot.polling()
