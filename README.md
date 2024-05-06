# strat-roulette-bot

<details>
  <summary>A Discord bot for playing Strat Roulette in CS:GO/CS2.</summary>

  Strat Roulette is an alternative way to play Counter-Strike that revolves around completing a different challenge every round. See [Jon Sandman's YouTube video](https://youtu.be/LgCC2TMRjB0?si=NNLmFQ-hbuzg6jmH) about it.

  I wrote this bot as an experiment in Python, which I had barely used since uni. I wanted something that would let me play with a bunch of different libraries and be fun to use.

  The bot:
  * parses data from the game to detect when a new round is starting.
  * scrapes a strat from [strat-roulette.github.io](https://strat-roulette.github.io/).
  * uses text to speech to generate a recording of someone reading the strat aloud.
  * sends and plays the strat in Discord.
</details>

![bot](https://github.com/tiggerdine/strat-roulette-bot/assets/9384949/cfd8c372-b66a-47e4-8734-7dbbf027cfe1)

## Setup

(Have the latest version of Python.)

Copy `gamestate_integration_stratroulette.cfg` to your game's config folder (`C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg`).

Create a Discord bot:
* Create a new application (e.g. "Strat Roulette Bot") in the [Discord Developer Portal](https://discord.com/developers/applications).
* Go to "Settings" -> "Bot" -> "Token", reset the token, and copy it.
* Set the `STRAT_ROULETTE_DISCORD_BOT_TOKEN` environment variable to the token you just copied.

Add the bot to your server:
* Go to "Settings" -> "OAuth2" -> "OAuth2 URL Generator", select the "bot" scope, and copy the generated URL.
* Open the URL you just copied in your browser.
* Select the server you want to add the bot to, and click "Authorise".

Install FFmpeg:
* Download the latest version of [FFmpeg](https://ffmpeg.org/).
* Extract it to `C:/ffmpeg`, so the path to `ffmpeg.exe` is `C:/ffmpeg/bin/ffmpeg.exe`.
* (If you want to extract it elsewhere, just change `exe` in `config.ini`.)

### [Optional] ElevenLabs TTS

By default, the bot uses the [pyttsx3](https://github.com/nateshmbhat/pyttsx3) text to speech, but it can also use [ElevenLabs](https://elevenlabs.io/). ElevenLabs sounds much more realistic, but it requires an account, and the free plan has a quota of 10,000 characters per month (enough for about 50 strats, or about two games of CS2).

If you want to use ElevenLabs TTS:
* [Create an account](https://elevenlabs.io/app/sign-up).
* Go to "My Account" -> "Profile + API key", reveal the key, and copy it.
* Set the `ELEVEN_API_KEY` environment variable to the key you just copied.
* In `config.ini`, change `tts` to `elevenlabs`.

## Usage

Join a voice channel and run `bot.py`.

## Future work

* Add a configuration UI.
* Bundle everything into a single exe.
* Support different voices.
* ???

# Resources

I used the [Valve Developer Community](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration) and [Bkid's Reddit post](https://www.reddit.com/r/GlobalOffensive/comments/cjhcpy/game_state_integration_a_very_large_and_indepth/) to learn about GSI.

The [Python docs](https://docs.python.org/3/) and [PyPI](https://pypi.org/)

## License

[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
