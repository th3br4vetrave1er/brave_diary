from datetime import datetime

text = input("Tell me, traveler, how was your day?: ")
filename = datetime.now().strftime("%Y-%m-%d")

with open(filename, "w") as file:
    file.write(f"{filename}: {text}\n")

print("Huh! Well that was something! Thank you for your story, see you tomorrow!")