# Windscribe-Port-Forwarding

## Credits
#### Original Credit: https://github.com/Mibo5354, https://gist.github.com/Mibo5354/cf265bc2108edb839e3607d9c9359dfa

Forked from https://github.com/JNuggets/Windscribe-Ephemeral-Port-Script
JNuggets' credits :
This script has been modified from Mibo5454's original to refresh the Windscribe Ephermeral port and set qBittorrents
listening port automatically.

# Disclaimer
Reports of using the script often can lead to account being temporarily disabled. Reduce usage to the minimum required timeframe

# Description
This fork updates JNUggets' script with bug fixes, .env functionality for more security and Discord bot capabilities to get a DM when the port is updated !

## Requirements

* Python (last tested on 3.11.0)
* selenium Package (Last tested on 4.19.0)
* qbittorrent-api Package (last tested on 2024.3.60)
* python-dotenv Package (last tested on 1.0.1)
* discord.py Package (last tested on 2.3.2)

## Setup

To use the script, fill the variables in the .env file and run the script !

Replace :
  -ws_username and ws_password with your Windscribe credentials
  -qbt_username, qbt_password, qbt_host, qbt_port with your qBittorrent credentials
