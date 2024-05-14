# Windscribe-Port-Forwarding

## Credits
#### Original Credit: https://github.com/Mibo5354, https://gist.github.com/Mibo5354/cf265bc2108edb839e3607d9c9359dfa

Forked from https://github.com/JNuggets/Windscribe-Ephemeral-Port-Script

JNuggets' credits :
This script has been modified from Mibo5454's original to refresh the Windscribe Ephermeral port and set qBittorrents
listening port automatically.

# Disclaimer
Reports of using the script often can lead to account being temporarily disabled. Windscribe support confirmed that it is allowed to use scripts such as this one, but keep it at once a week, don't spam their servers ;).

# Description
This fork updates JNuggets' script with bug fixes, .env functionality for more security and Discord bot capabilities to get a DM when the port is updated (optional) !

## Requirements

* Python (last tested on 3.11.0)
* selenium Package (Last tested on 4.19.0)
* qbittorrent-api Package (last tested on 2024.3.60)
* python-dotenv Package (last tested on 1.0.1)
* discord.py Package (last tested on 2.3.2)

Note : The discord.py package is **not** optional, only the feature is.

## Setup

To use the script, create a .env file in the directory of the python script with the following variables :

```
ws_username=
ws_password=
qbt_username=
qbt_password=
qbt_host=
qbt_port=
bot_token=
discord_userid=
```

Replace :
  * ws_username and ws_password with your Windscribe credentials
  * qbt_username, qbt_password, qbt_host, qbt_port with your qBittorrent credentials
## Optional
If you wish to also get Discord messages for new ports, fill :
  * bot_token with a Discord bot token
  * discord_userid with your Discord User ID

If you don't need the feature, leave the fields blank.

Note : Make sure that the bot has the right to message you ! Try adding it to a Discord server you own and enable DMs from members of that server if you are having issues.
