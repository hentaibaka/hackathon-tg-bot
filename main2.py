from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import keyboard as kb

# Делаем функции асинхронными и используем await для асинхронных вызовов
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Привет! Выберите курс, по которому хотите пройти вопросы:",
        reply_markup=kb.course_keyboard()
    )

async def handle_course_selection(update: Update, context: CallbackContext) -> None:
    course = update.message.text
    if course in kb.COURSES:
        context.user_data['current_course'] = course
        context.user_data['question_index'] = 0
        await ask_question(update, context)
    else:
        await update.message.reply_text("Пожалуйста, выберите курс из предложенных.")

async def ask_question(update: Update, context: CallbackContext) -> None:
    course = context.user_data['current_course']
    index = context.user_data['question_index']
    questions = kb.QUESTIONS[course]
    if index < len(questions):
        await update.message.reply_text(questions[index])
    else:
        await update.message.reply_text("Вы ответили на все вопросы курса!")
        del context.user_data['current_course']
        del context.user_data['question_index']

async def handle_response(update: Update, context: CallbackContext) -> None:
    if 'current_course' in context.user_data:
        context.user_data['question_index'] += 1
        await ask_question(update, context)

def main() -> None:
    application = Application.builder().token('6745658806:AAGSRjiG_UuQC_xz-YLRdY2Pwt08PwG4NQU').build()
    application.add_handler(CommandHandler('start', start))
    # Разделяем обработку сообщений на две разные функции
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.Regex('^(' + '|'.join(kb.COURSES) + ')$'), handle_course_selection))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex('^(' + '|'.join(kb.COURSES) + ')$'), handle_response))

    application.run_polling()

if __name__ == '__main__':
    main()
