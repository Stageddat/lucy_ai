def saveMessage(message):
    with open("db/messageLog.txt", "a", encoding="utf-8") as f:
        f.write(message.strip() + "\n")

