from pyfiglet import Figlet

rechnerText = Figlet()
byeText = Figlet()
print(rechnerText.renderText("Python Toleranzrechner"))

toleranz_tabelle = {
    "1-3": {
        "H6": {"oberes Abmaß": +6, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +10, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +14, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +60, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -6, "Unteres Abmaß": -12},
        "g6": {"oberes Abmaß": -2, "Unteres Abmaß": -8},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -6},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -25},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -60},
        "j6": {"oberes Abmaß": +4, "Unteres Abmaß": -2},
        "k6": {"oberes Abmaß": +6, "Unteres Abmaß": 0},
        "m6": {"oberes Abmaß": +8, "Unteres Abmaß": +2},
        "n6": {"oberes Abmaß": +10 , "Unteres Abmaß": +4},
        "r6": {"oberes Abmaß": +16, "Unteres Abmaß": +10},
        "s6": {"oberes Abmaß": +20, "Unteres Abmaß": +14},
    },



    }
