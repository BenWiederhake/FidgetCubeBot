# FidgetCubeBot

> You can count on me. And much more.

This is gonna be so annoying.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [TODOs](#todos)
- [NOTDOs](#notdos)
- [Contribute](#contribute)

## Install

```console
$ # Install Python3 somehow
$ pip3 install --user -r requirements.txt
```

That should be it.

## Usage

- Copy `secret_template.py` to `secret.py`
- Create your bot
    * This means you have to talk to the `@BotFather`: https://web.telegram.org/z/#93372553
    * Do `/newbot`, edit it as much as you like (i.e. description, photo)
    * For the commands, paste the following as-is:
      ```
      count - Hochzählen
      plopp - Plopp!
      roll - Es könnte Alles passieren! Oder du rollst eine 4.
      ```
    * Invite him into the group chat(s) you like
    * Afterwards, set the bot to "Allow groups: No"
    * Copy the API token
- Fill in your own username, the bot name, and the API token in `secret.py`
- Run `bot.py`. I like to run it as `./bot.py 2>&1 | tee bot_$(date +%s).log`, because that works inside screen and I still have arbitrary scrollback.
- You can Ctrl-C the bot at any time and restart it later. The state is made permanent in `fidgetcube_data.json`

## TODOs

Not much, maybe add more message variants?

## NOTDOs

* Dunno

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/FidgetCubeBot/issues/new) or submit PRs.
