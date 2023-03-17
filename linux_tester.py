import pyautogui
import time
 
qwerty = "qwamzmQWAMM§"
azerty = "azq;w;AZQZW@"


trans = str.maketrans(azerty, qwerty)
time.sleep(5)

filename = "output.txt"

x, y = 500, 500

wait_time = 1

with open(filename, "r") as f:
    for line in f:
        # Supprime les caractères de fin de ligne
        #line = str(line.rstrip("\n"))
        line = "PourtousLesMotsmotsdeP@sse0!"
        # Sélectionne le champ de texte
        #pyautogui.click(x, y)

        # Attendre avant d'appuyer sur la touche Entrée
        time.sleep(0.01)
        
        pyautogui.hotkey("ctrlleft", "a")

        # Attendre avant d'appuyer sur la touche Entrée
        time.sleep(0.01)
        
        passwd = line.translate(trans)
        #passwd = line.translate(str.maketrans('azqwAZQW&é"\'(-è_çà)^$Mù,?;:!§1234567890','qwazQWAZ1234567890-[]:\'mM,./?!@#$%^&*()'))
        pyautogui.write(passwd)

        time.sleep(0.01)
        # Simule la pression de la touche Entrée
        pyautogui.press("enter")

