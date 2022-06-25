#!/usr/bin/env python3
# Heavily inspired by chatmemberbot.py in the examples folder.

from atomicwrites import atomic_write
import json
import logging
import os
import secret  # See secret_template.py
import secrets
import sys
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.ext import CallbackContext, ChatMemberHandler, CommandHandler, Updater

import logic
import msg


logger = logging.getLogger(__name__)

PERMANENCE_FILENAME = 'fidgetcube_data.json'

FIDGETCUBE_STATE = dict()


def load_state():
    global FIDGETCUBE_STATE
    if os.path.exists(PERMANENCE_FILENAME):
        with open(PERMANENCE_FILENAME, 'r') as fp:
            fidgetcube_state = json.load(fp)
        logic.unfuck_state(fidgetcube_state)
        FIDGETCUBE_STATE = fidgetcube_state
        logger.info(f'Loaded: {FIDGETCUBE_STATE}')
    else:
        logger.info(f'Permanence file {PERMANENCE_FILENAME} does not exist; starting from scratch.')
        FIDGETCUBE_STATE = logic.default_state()


def save_state():
    with atomic_write(PERMANENCE_FILENAME, overwrite=True) as fp:
        json.dump(FIDGETCUBE_STATE, fp, separators=',:')
    logger.info(f'Wrote to {PERMANENCE_FILENAME}: {FIDGETCUBE_STATE}')


def message(msg_id):
    return secrets.choice(msg.MESSAGES[msg_id])


def cmd_show_state(update: Update, _context: CallbackContext) -> None:
    if update.effective_user.username != secret.OWNER:
        return

    update.effective_message.reply_text(str(FIDGETCUBE_STATE))


def cmd_start(update: Update, _context: CallbackContext) -> None:
    update.effective_message.reply_text(
        f'Hi {update.effective_user.first_name}!'
        f'\n/count@{secret.BOTNAME} → Zählt eins hoch. Probier es doch mal aus!'
        f'\n/plopp@{secret.BOTNAME} → Mach plopp!'
        f'\n/roll@{secret.BOTNAME} → Würfelt eine ganz doll zufällige Zahl!'
        f'\n/bin_ich_toll@{secret.BOTNAME} → Bist du toll?'
        f'\nViel mehr macht der Bot nicht.'
        f'\nhttps://github.com/BenWiederhake/FidgetCubeBot'
        # For BotFather:
        # count - Hochzählen
        # plopp - Plopp!
        # roll - Es könnte Alles passieren! Oder du rollst eine 4.
    )


def cmd_for(command):
    def cmd_handler(update: Update, _context: CallbackContext):
        if update.message is None or update.message.text is None:
            return  # Don't consider Updates that don't stem from a text message.
        text = update.message.text.split(' ', 1)
        argument = text[1] if len(text) == 2 else ''

        should_save, maybe_response = logic.handle(FIDGETCUBE_STATE, command, argument, update.effective_user.id, update.effective_user.username, update.effective_user.first_name)
        if should_save:
            save_state()
        if maybe_response is None:
            return  # Don't respond at all
        update.effective_message.reply_text(
            message(maybe_response[0]).format(*maybe_response[1:])
        )
    return cmd_handler


def run():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("Alive")

    load_state()

    # Create the Updater and pass it your bot's token.
    updater = Updater(secret.TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("dump_state", cmd_show_state))
    dispatcher.add_handler(CommandHandler("show_state", cmd_show_state))
    dispatcher.add_handler(CommandHandler("start", cmd_start))

    dispatcher.add_handler(CommandHandler("count", cmd_for('count')))
    dispatcher.add_handler(CommandHandler("plopp", cmd_for('plopp')))
    dispatcher.add_handler(CommandHandler("roll", cmd_for('roll')))
    dispatcher.add_handler(CommandHandler("bin_ich_toll", cmd_for('bin_ich_toll')))

    # Start the Bot
    # We pass 'allowed_updates' handle *all* updates including `chat_member` updates
    # To reset this, simply pass `allowed_updates=[]`
    updater.start_polling(allowed_updates=Update.ALL_TYPES)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    logger.info("Begin idle loop")
    updater.idle()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        run()
    elif len(sys.argv) == 2 and sys.argv[1] == '--dry-run':
        print(f'Dry-running from file {PERMANENCE_FILENAME}')
        load_state()
        print(f'Loaded: {FIDGETCUBE_STATE}')
    else:
        print(f'USAGE: {sys.argv[0]} [--dry-run]')
        exit(1)
