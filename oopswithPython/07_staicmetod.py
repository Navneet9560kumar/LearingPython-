class Chaiutils:
    @staticmethod
    def clean_ingredin(text):
        return [item.strip() for item in text.split(",")]

# Fixing input: make it a proper string
raw = "water, milk, ginger, honey"

cleaned = Chaiutils.clean_ingredin(raw)
print(cleaned)
