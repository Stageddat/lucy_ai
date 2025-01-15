def retrieveRecentHistory(limit=20):
    recent_text = ""
    with open("db/messageLog.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines[-limit:]:
        recent_text += line.strip() + "\n"
    return recent_text