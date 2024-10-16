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
        "n6": {"oberes Abmaß": +10, "Unteres Abmaß": +4},
        "r6": {"oberes Abmaß": +16, "Unteres Abmaß": +10},
        "s6": {"oberes Abmaß": +20, "Unteres Abmaß": +14},
    },
    "3-6": {
        "H6": {"oberes Abmaß": +8, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +12, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +18, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +75, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -10, "Unteres Abmaß": -18},
        "g6": {"oberes Abmaß": -4, "Unteres Abmaß": -12},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -8},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -30},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -75},
        "j6": {"oberes Abmaß": +6, "Unteres Abmaß": -2},
        "k6": {"oberes Abmaß": +9, "Unteres Abmaß": +1},
        "m6": {"oberes Abmaß": +12, "Unteres Abmaß": +4},
        "n6": {"oberes Abmaß": +16, "Unteres Abmaß": +8},
        "r6": {"oberes Abmaß": +23, "Unteres Abmaß": +15},
        "s6": {"oberes Abmaß": +27, "Unteres Abmaß": +19},
    },
    "6-10": {
        "H6": {"oberes Abmaß": +9, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +15, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +22, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +90, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -13, "Unteres Abmaß": -22},
        "g6": {"oberes Abmaß": -5, "Unteres Abmaß": -14},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -9},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -36},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -90},
        "j6": {"oberes Abmaß": +7, "Unteres Abmaß": -2},
        "k6": {"oberes Abmaß": +10, "Unteres Abmaß": +1},
        "m6": {"oberes Abmaß": +15, "Unteres Abmaß": +6},
        "n6": {"oberes Abmaß": +19, "Unteres Abmaß": +10},
        "r6": {"oberes Abmaß": +28, "Unteres Abmaß": +19},
        "s6": {"oberes Abmaß": +32, "Unteres Abmaß": +23},
    },
    "10-18": {
        "H6": {"oberes Abmaß": +11, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +18, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +27, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +110, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -16, "Unteres Abmaß": -27},
        "g6": {"oberes Abmaß": -6, "Unteres Abmaß": -17},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -11},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -43},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -110},
        "j6": {"oberes Abmaß": +8, "Unteres Abmaß": -3},
        "k6": {"oberes Abmaß": +12, "Unteres Abmaß": +1},
        "m6": {"oberes Abmaß": +18, "Unteres Abmaß": +7},
        "n6": {"oberes Abmaß": +23, "Unteres Abmaß": +12},
        "r6": {"oberes Abmaß": +34, "Unteres Abmaß": +23},
        "s6": {"oberes Abmaß": +39, "Unteres Abmaß": +28},
    },
    "18-30": {
        "H6": {"oberes Abmaß": +13, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +21, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +33, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +130, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -20, "Unteres Abmaß": -33},
        "g6": {"oberes Abmaß": -7, "Unteres Abmaß": -20},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -13},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -52},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -130},
        "j6": {"oberes Abmaß": +9, "Unteres Abmaß": -4},
        "k6": {"oberes Abmaß": +15, "Unteres Abmaß": +2},
        "m6": {"oberes Abmaß": +21, "Unteres Abmaß": +8},
        "n6": {"oberes Abmaß": +28, "Unteres Abmaß": +15},
        "r6": {"oberes Abmaß": +41, "Unteres Abmaß": +28},
        "s6": {"oberes Abmaß": +48, "Unteres Abmaß": +35},
    },
    "30-50": {
        "H6": {"oberes Abmaß": +16, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +25, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +39, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +160, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -25, "Unteres Abmaß": -41},
        "g6": {"oberes Abmaß": -9, "Unteres Abmaß": -25},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -16},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -62},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -160},
        "j6": {"oberes Abmaß": +11, "Unteres Abmaß": -5},
        "k6": {"oberes Abmaß": +18, "Unteres Abmaß": +2},
        "m6": {"oberes Abmaß": +25, "Unteres Abmaß": +9},
        "n6": {"oberes Abmaß": +33, "Unteres Abmaß": +17},
        "r6": {"oberes Abmaß": +50, "Unteres Abmaß": +34},
        "s6": {"oberes Abmaß": +59, "Unteres Abmaß": +43},
    },
    "50-65": {
        "H6": {"oberes Abmaß": +19, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +30, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +46, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +190, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -30, "Unteres Abmaß": -49},
        "g6": {"oberes Abmaß": -10, "Unteres Abmaß": -29},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -19},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -74},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -190},
        "j6": {"oberes Abmaß": +12, "Unteres Abmaß": -7},
        "k6": {"oberes Abmaß": +21, "Unteres Abmaß": +2},
        "m6": {"oberes Abmaß": +30, "Unteres Abmaß": +11},
        "n6": {"oberes Abmaß": +39, "Unteres Abmaß": +20},
        "r6": {"oberes Abmaß": +60, "Unteres Abmaß": +41},
        "s6": {"oberes Abmaß": +72, "Unteres Abmaß": +53},
    },
    "65-80": {
        "H6": {"oberes Abmaß": +19, "Unteres Abmaß": 0},
        "H7": {"oberes Abmaß": +30, "Unteres Abmaß": 0},
        "H8": {"oberes Abmaß": +46, "Unteres Abmaß": 0},
        "H11": {"oberes Abmaß": +190, "Unteres Abmaß": 0},
        "f6": {"oberes Abmaß": -30, "Unteres Abmaß": -49},
        "g6": {"oberes Abmaß": -10, "Unteres Abmaß": -29},
        "h6": {"oberes Abmaß": 0, "Unteres Abmaß": -19},
        "h9": {"oberes Abmaß": 0, "Unteres Abmaß": -74},
        "h11": {"oberes Abmaß": 0, "Unteres Abmaß": -190},
        "j6": {"oberes Abmaß": +12, "Unteres Abmaß": -7},
        "k6": {"oberes Abmaß": +21, "Unteres Abmaß": +2},
        "m6": {"oberes Abmaß": +30, "Unteres Abmaß": +11},
        "n6": {"oberes Abmaß": +39, "Unteres Abmaß": +20},
        "r6": {"oberes Abmaß": +62, "Unteres Abmaß": +43},
        "s6": {"oberes Abmaß": +78, "Unteres Abmaß": +59},
    }
}
while True:
    try:
        user_input = int(input("Wählen Sie bitte eine Option aus: \n"+"1. Programm starten"+"\n"+" 2. Programm beenden\n"))
        if user_input == 1:
            print("Programm startet...")
        elif user_input == 2:
            print(byeText.renderText("Auf Wiedersehen :)"))
            break
        else:
            print("Die ausgewählte Option existiert nicht. Bitte wählen Sie eine gültige Option aus!")
    except ValueError:
        print("Nur Zahlen sind erlaubt!")
    except Exception:
        print("Unbestimmter Fehler!")