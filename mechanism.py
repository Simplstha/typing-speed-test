import random


class GenerateWord:

    def __init__(self):
        self.word_list = ["mist", "observation", "verdant", "popcorn", "acoustics", "cushion", "delight", "suspend",
                          "small",
                          "magic", "outgoing",
                          "sturdy", "zoom", "cherries", " jobless", "slimy", "degree", "ancient", "seashore", "smelly",
                          "towering",
                          "unadvised",
                          "remain", "childlike", "chunky", "paper", "acid", "proud", "damaging", "giants", "wiry",
                          "rhetorical",
                          "rigid",
                          "deafening", "thank", "glow", "pause", "form", "flag", "cheap", "road", "questionable",
                          "ambiguous",
                          "tired", "knowing",
                          "boil", "simple", "meek", "bore", "determined", "switch", "circle", "lush", "rinse",
                          "ceaseless", "crabby",
                          "massive",
                          "yell", "noiseless", "purring", "necessary", "shape", "open", "garrulous", "marvelous",
                          "confused", "rude",
                          "disastrous",
                          "trade", "umbrella", "rush", "stage", "sneaky", "eggnog", "joyous", "sugar", "watery",
                          "pickle", "mice",
                          "report",
                          "fire", "literate", "miss", "distinct", "uptight", "turkey", "vanish", "squash", "puncture",
                          "owe",
                          "icicle", "consist",
                          "toe", "agreement", "limit", "jail", "story", "wrap", "arch", "temporary", "serious",
                          "stomach",
                          "nondescript",
                          "conscious", "surround", "terrify", "tip", "profuse", "debt", "produce", "telephone", "right",
                          "snotty",
                          "bump", "sock",
                          "glove", "magenta", "raspy", "grade", "fragile", "boundary", "behave", "spiteful", "wistful",
                          "downtown",
                          "worthless",
                          "resolute", "educate", "wrathful", "pink", "worried", "tiresome", "moor", "anxious", "boast",
                          "suggest",
                          "gleaming",
                          "dog", "wet", "wire", "left", "satisfying", "hard", "crown", "argue", "hose", "disturbed",
                          "gaze", "blood",
                          "sour",
                          "cultured", "language", "decide", "shaggy", "bumpy", "suspect", "imperfect", "tiger", "crowd",
                          "unfasten",
                          "shade",
                          "squeal", "growth", "waves", "confuse", "volatile", "buzz", "hospital", "shut", "slave",
                          "unarmed",
                          "woebegone",
                          "combative", "impress", "launch", "prepare", "harass", "rustic", "kitty", "busy", "regular",
                          "attractive",
                          "wonderful",
                          "madly", "rice", "travel", "admire", "receipt", "top", "dance", "nasty", "likeable", "shaky",
                          "erect",
                          "fine",
                          "parsimonious", "long", "fallacious", "punishment", "courageous", "veil", "poised", "aunt",
                          "young",
                          "spectacular",
                          "hissing", "deserve", "flower", "equable", "sudden", "carriage", "loutish", "star", "geese",
                          "art",
                          "steadfast", "stamp",
                          "crooked", "cows", "calculator", "connection", "hateful", "name", "writer", "sort", "plate",
                          "rely",
                          "creature",
                          "shelter", "reaction", "observant", "understood", "stingy", "gruesome", "blue", "jar",
                          "average",
                          "materialistic",
                          "educated", "clean", "hope", "bizarre", "pointless", "deserted", "building", "gorgeous",
                          "scene", "gabby",
                          "inject",
                          "supreme", "entertaining", "festive", "scent", "milky", "plot", "unnatural", "notebook",
                          "enormous",
                          "teaching",
                          "numberless", "ubiquitous", "island", "equal", "foregoing", "reading", "return", "wacky",
                          "mouth",
                          "animated", "rebel",
                          "economic", "crazy", "cellar", "war", "fairies", "wood", "bait", "grandfather", "summer",
                          "calm", "canvas",
                          "nosy",
                          "join", "bad", "bewildered", "act", "shake", "wandering", "baby", "burst", "hop", "root",
                          "zesty",
                          "lavish", "accurate",
                          "fit", "identify", "hair"]

    def generate_text(self):
        text = ""
        for i in range (70):
            word = random.choice(self.word_list)
            text += word + "  "
        return text

    def calculate(self, text, in_text):
        score = 0
        text_without_space = text.replace(" ", "")
        text_list = list(text_without_space)
        in_text_without_space = in_text.replace(" ", "")
        in_text_list = list(in_text_without_space)
        index = len(in_text_list) - 1
        to_check_list = text_list[:index]
        for l in in_text_list:
            if l in to_check_list:
                score += 1
            else:
                score += 0
        return score