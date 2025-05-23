from datetime import datetime

text = input("Tell me, traveler, how was your day?: ")
docname = datetime.now().strftime("%Y-%m-%d")

with open(docname, "w") as doc:
    doc.write(f"{docname}: {text}\n")

print("Huh! Well that was something! Thank you for your story, see you tomorrow!")