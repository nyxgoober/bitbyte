# BitByte Discord Bot

This repository contains the **BDScript 2 source code** for the BitByte Discord Bot.

> [!IMPORTANT]
> This project is written for **Bot Designer for Discord (BDFD)** and is not directly self-hostable.  
> It is intended for transparency, learning, and Share Code reference.

![GitHub Stars](https://img.shields.io/github/stars/nyxgoober/bitbyte)
Please star this repository if you found it helpful or interesting.

---

## Pseudo File Extensions

To better organize the project, the following pseudo-extensions are used:

- `.bds` → **BDScript 2 command files**
- `.var` → **Bot variable definitions / stored data structures**

These are not required by GitHub, but are used for clarity and structure.

## 📂 Project Structure

```
/Moderation/
  ban.bds
  mute.bds
  unmute.bds
  unban.bds
  ...

/Utilities/
  userinfo.bds
  avatar.bds
  calc.bds
  ...

/Bot/
  commands.bds
  run.bds
  ...

/Miscellaneous/
  ping.bds
  info.bds
  ...

/Variables/
  byte_key.var
  isAdmin.var
  isInBlacklist.var
  ...
```

---

## Overview

### 🛡️ Moderation
Commands related to server control and moderation actions such as banning, kicking, muting, and warnings.

### ⚙️ Utilities
General-purpose commands that provide useful information or tools like ping checks, avatars, and server info.

### 🤖 Bot
Meta commands related to the bot such as eval or help reference.

### 🎲 Miscellaneous
Non-essential commands such as latency checks and bot information.

### 📦 Variables
Stores persistent bot data including configuration, user data, economy (in the future), and psudeo-functions.

## Notes

- All `.bds` files represent **BDScript 2 command logic used inside BDFD**
- All `.var` files represent **logical data structures used by the bot**
- This repository is for **documentation and educational purposes only**
- To run the bot, use the **Share Code feature in Bot Designer for Discord**.
---
### BDFD Share Code:
```D9dh837pYCWl9759DnkKdyFFS```
