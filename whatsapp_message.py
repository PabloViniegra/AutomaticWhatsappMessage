import pyautogui, webbrowser, time, sys

if len(sys.argv) == 4:
    inputNumber = sys.argv[1]
    inputMsg = sys.argv[2]
    inputLoop = sys.argv[3]
    if (inputNumber.startswith('+')):
        webbrowser.open("https://web.whatsapp.com/send?phone=" + inputNumber.strip())
        time.sleep(6)
        for i in range(int(inputLoop)):
            pyautogui.write(inputMsg)
            pyautogui.press("enter")
    else:
        print("ERROR: el número de teléfono ha sido malformado")
        print("SOLUCIÓN: el número de teléfono debe tener [+][prefijo telefónico][número de teléfono]")
        print("EJEMPLO: +34916129875")
        print(("Otra posibilidad es que el tercer argumento no sea un numero"))
        print("Debe introducir: 'python3 whatsapp_message.py [numero de telefono] [mensaje] [número de repeticiones]'")


else:
    print("ERROR: Introdujo  más de dos (2) argumentos. Solo es necesario el número de teléfono")
    print("SOLUCIÓN: Introduce los argumentos correctamente")
    print("Debe introducir: 'python3 whatsapp_message.py [numero de telefono] [mensaje] [número de repeticiones]'")





