import pyautogui
import time
pyautogui.alert('Código sendo executado não usar teclado ou mouse')

pyautogui.PAUSE = 0.5

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://www.ojogodobicho.com/deu_no_poste.htm')
pyautogui.press('enter')

pyautogui.alert('Pronto pode voltar a usar seu computador')


# pyautogui.hotKey('winleft', 'd') ## abre área de trabalho

# detectar lugar onde o mouse está para clicar ou arrastar
# pyautogui.position()

# move o mouse pra determinada posição
# pyautogui.moveTo(number, numer)

# pressionar botão esquerdo do mouse e segurar para arrastar
# pyautogui.mouseDown()

# soltar o botão pra largar o arquivo selecionado
# pyautogui.mouseUp()

