word_to_emoji = {
    "love": "❤️",
    "fire": "🔥",
    "party": "🎉",
    "idea": "💡",
    "study": "📚",
    "code": "💻",
    "coding": "💻",
    "developer": "👨‍💻",
    "computer": "🖥️",
    "keyboard": "⌨️",
    "engineer": "🧑‍💻",
    "debug": "🛠️",
    "fix": "🔧",
    "bug": "🪲",
    "task": "✅",
    "project": "📂",
    "package": "📦",
    "api": "🔗",
    "test": "🧪",
    "food": "🍕",
    "write": "✍️",
    "videos": "📹",
    "make": "🔨"
}

message = input("Enter your message: ")

updated_words = []

for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = word_to_emoji.get(cleaned, "")
    if emoji:
        updated_words.append(f"{word} {emoji}")
    else:
        updated_words.append(word)

updated_message = " ".join(updated_words)
print("\nEnhanced message:\n")
print(updated_message)
