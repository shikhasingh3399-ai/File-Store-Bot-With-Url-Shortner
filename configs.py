import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "22315574"))
  API_HASH = os.environ.get("API_HASH", "8140b32da5b476a7850fd7082fc0e408")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8434463762:AAGW_ShS0ddK_CdcHVzKqMp4cFguNtZUJKg")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "AnimeHaven3399_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002882679129"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "8423919788"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://shikhasingh3399:6ZZNI25JKO9XjTQe@cluster0.klo8ayj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002530783070")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002731660368"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│🤖 ᴍʏ ɴᴀᴍᴇ: Mᴏɴᴋᴇʏ.D.Lᴜғғʏ
◈ ᴏᴡɴᴇʀ:[Cʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/MonkeyD_Luffy4)
◈ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: [Cʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Anime_Hindi_Official_series)
◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ: [Cʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/+fWXDRskiHnA1ODQ1)
◈ ᴢᴇɴɪʜ ᴄᴜᴛs: [Cʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/Zenith_Cuts455)
◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: [Cʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/MonkeyD_Luffy4)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Mᴏɴᴋᴇʏ D. Lᴜғғʏ](https://t.me/MonkeyD_Luffy4)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/MonkeyD_Luffy4)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
