import notas

# lista
nomes = ['Alex', 'Simone', 'Bernardo', 'César', 'Alexandra', 'Joabe', 'Lucas', 'Beltiza', 'Aldeídes', 'Juscelino', 'Daniel', 'Daniela', 'Andreza', 'Luciana', 'Tereza', 'Rubenilde', 'Carolina', 'Pedro', 'Renata', 'Renato', 'Adalberto', 'Paulo', 'Bruna', 'Rafael', 'Rafaela', 'Rogério', 'Edriano', 'Rita', 'Cenira', 'Juliana']
nomes.sort()

nome = input('Digite o nome a ser pesquisado: ').capitalize()

try:
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')

import pyautogui as auto
import time
import os

auto.PAUSE = 0.5

auto.hotkey('ctrl', 'j')
auto.hotkey('ctrl', 'j')
auto.press('enter')
auto.write('git init')
auto.press('enter')
auto.write('git add .')
auto.press('enter')
auto.write('git config --global user.name "Gugamaral"')
auto.press('enter')
auto.write('git config --global user.email "guamaral@gmail.com"')
auto.press('enter')
auto.write('git commit -m "Versão 1.0"')
auto.press('enter')
auto.write('git branch -M main')
auto.press('enter')
auto.write('git remote add origin https://github.com/Gugamaral/alunos_notas.git')
auto.press('enter')
auto.write('git push -u origin main')
auto.press('enter')

time.sleep(3)
auto.click('\t')
auto.click('\t')
auto.click('\t')
auto.click('\t')
auto.click('\t')
auto.press('enter')

auto.write('pip install cx_Freeze')
auto.press('enter')

auto.write('cxfreeze main.py --target-dir pasta-autoguit')
auto.press('enter')