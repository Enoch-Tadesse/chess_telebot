from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import chessAPI


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, "hello sir")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id, "help is on the way sir.")


async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    lb = chessAPI.get_leaderboards()
    await context.bot.send_message(chat_id, lb)


async def stats(update: Update, context):
    chat_id = update.effective_chat.id
    if context.args:
        text = chessAPI.get_player_stats(context.args[0])
        await context.bot.send_message(chat_id, text)
    else:
        await context.bot.send_message(chat_id, "A valid chess.com username is required. E.g. '/stats hikaru'.")


async def get_games(update: Update, context):
    chat_id = update.effective_chat.id
    username = context.args
    if username:
        game_list = chessAPI.get_player_game(username[0])
        game_string = ""
        await context.bot.send_message(chat_id, f"Here is the latest 10 games of {username[0]}.\n")
        for info in game_list:
            game_string = game_string + info + '\n'
        await context.bot.send_message(chat_id, game_string)
    else:
        await context.bot.send_message(chat_id, "A valid chess.com username is required. E.g. '/stats hikaru'.")


if __name__ == '__main__':
    application = ApplicationBuilder().token('7218643432:AAEWVS9zlosNMJqCn8tea2_GQ5iQ3zVW8x8').build()
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    stats_handler = CommandHandler('stats', stats)
    leaderboard_handler = CommandHandler('leaderboard', leaderboard)
    get_games_handler = CommandHandler('game', get_games)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(stats_handler)
    application.add_handler(leaderboard_handler)
    application.add_handler(get_games_handler)
    application.run_polling()
