import random


tips = [
    "пластик ето опасная штука для экологии.",
    "если есть мусор подбери его и выброси кроме если ето токсичный мусор.",
    "ходи пешком либо исползую велосепед .",
    "не кидай мусор в воду."
    
]

def get_random_tip():
    return random.choice(tips)
