from telethon.sync import TelegramClient
from telethon.tl.types import InputMediaPhoto, InputMediaDocument
import sqlite3
import sys
# conn = sqlite3.connect('caminhodobanco')
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM videos order by id desc")
# rows = cursor.fetchall()

api_id = 'xxxxxxxxx'
api_hash = 'xxxxxxxxxxxxxx'

channel_username = '@docanal'

with TelegramClient('session_name', api_id, api_hash) as client:
    sys.exit(1)
    for row in rows:
        id = row[0]
        title = row[1]
        description = row[7]
        video_id = row[5]
        prefix = "pastaraiz"
        fileName = id
        filNameStr = str(fileName)
        if len(filNameStr) < 3:
            filNameStr = str(filNameStr).zfill(3)
        # print(filNameStr)
        sufix = ".mp4"
        if id <= 784:
            fullpath = f"{prefix}{fileName}{sufix}"
            thumbnail = f"pastaRaizDaMiniatura/{id}_standard.jpg"
            print(filNameStr + " - Start")
            file = client.upload_file("pastRaizDovideo/{id}.mp4")
            file = client.upload_file(fullpath)
            client.send_file(channel_username, file, caption=f"#{filNameStr} - {title} - {video_id}",
                            #thumb=thumbnail
                            )
            client.send_message(
                    channel_username, 
                    f"#{filNameStr} \n \n {description} \n \n {video_id} \n \n https://youtu.be/{video_id}",
                    link_preview=False
                    )
            print(filNameStr + " - End")
    # Close the cursor and connection
    cursor.close()
    conn.close()