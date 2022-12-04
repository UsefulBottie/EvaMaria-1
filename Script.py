class script(object):
    START_TXT = """Hey hey hey {} dostum 💖
Ben İçerik botuyum, veritabanımdaki içerikleri kullanman için yapıldım.

Beni kullanmak çok basit, beni grubuna ekle ve admin yap. 
Hepsi bu kadar! Mesaj yazma yerine @filtercontent yaz ve bir boşluk bırak ve isteiğin içeriği yaz...🤓🤪


⚠️Daha fazlası için /help yazmayı unutma!

😎 @birmuhendisinkanallari'nın amme hizmetidir.

©️ Maintained By @GuruBhai11"""
    HELP_TXT = """
    🙋🏻‍♂️   Selamlar  {} 🤓

○  Inline mod ile satır içi arama yap
 Bu mod bütün gruplarda çalışır. Mesaj yazma yerine @filtercontent yaz ve bir boşluk bırak sonra izlemek istediğin içeriğin adını gir.

○ Mevcut Komutlar
     
 /start - Yaşıyo muyuz usta bi bak bakalım...
 /info - Kullanıcı hakkında bilgi
 /id - Kullanıcının IDsi
 /stats - Database hakkında bilgi  
 /broadcast - Broadcast (Sadece admin için)

😎 @birmuhendisinkanallari'nın amme hizmetidir.

©️ @cinarmecnun tarafından düzenlendi"""
    ABOUT_TXT = """✯ Kullanıcı Adı: {}
✯ Geliştirici: <a href=https://t.me/birmuhendisinkanallari>Bir Mühendisin Kanalları</a>
✯ Modüller: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ Programlama Dili: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳atabase: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱ot 𝚂erveri: www.render.com
"""
    SOURCE_TXT = """<b>NOT:</b>
- Eva Maria açık kaynaklı bir projedir. 
- Repo - <a href=https://github.com/AM-ROBOTS/EvaMaria>Eva Maria</a>
"""
    SUPPORT_TXT = """<b>İletişim ve Banka Bilgileri:</b>
• IBAN: @cinarmecnun ile iletişime geçebilirsiniz. 
• Patreon - https://www.patreon.com/lustersoftware
• Github - https://github.com/Furkan-izgi 

<b>DEVS:</b>
- <a href=https://t.me/Am_RoBots>ᴀᴍ_ᴛᴇᴄʜ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/sources_cods)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ Toplam İçerik Sayısı: <code>{}</code>
★ TOPLAM KULLANICI: <code>{}</code>
★ TOPLAM CHATLER: <code>{}</code>
★ KULLANILAN HAFIZA: <code>{}</code> 
★ KALAN HAFIZA: <code>{}</code> """
    LOG_TEXT_G = """⚠️ #YeniGrup tespit edildi. Kıpırdama sakın! 📸
Grup = {}(<code>{}</code>)
Toplam Üye Sayısı = <code>{}</code>
Ekleyen kişi - {}
"""
    LOG_TEXT_P = """⚠️ #YeniKullanıcı olduğun yerde kal! 📸
ID - <code>{}</code>
Kullanıcı Adı - {}
"""
