
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit, QListWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QInputDialog
import json
app = QApplication([])
main = QWidget()
main.resize(800, 600)
main.setWindowTitle('Умные заметки')
button1 = QPushButton('Создать заметку')
button2 = QPushButton('Удалить заметку')
button3 = QPushButton('Сохранить заметку')
button4 = QPushButton('Добавить к заметке')
button5 = QPushButton('Открепить от заметки')
button6 = QPushButton('Искать заметки по тегу')
text1 = QLabel('Список заметок')
text2 = QLabel('Список тегов')
low = QLineEdit()
low.setPlaceholderText('Введите тег..')
text = QTextEdit()
list1 = QListWidget()
list2 = QListWidget()

line = QVBoxLayout()
line.addWidget(text)

line2 = QVBoxLayout()
line2.addWidget(text1)
line2.addWidget(list1)
line3 = QHBoxLayout()
line3.addWidget(button1)
line3.addWidget(button2)
line2.addLayout(line3)
line2.addWidget(button3)

line2.addWidget(text2)
line2.addWidget(list2)
line2.addWidget(low)
line4 = QHBoxLayout()
line4.addWidget(button4)
line4.addWidget(button5)


line2.addLayout(line4)
line2.addWidget(button6)
line5 = QHBoxLayout()
line5.addLayout(line, stretch=2)
line5.addLayout(line2, stretch=1)
main.setLayout(line5)
notes = {
    'Название заметки' :
    {
        'текст' : 'Очень важный текст заметки',
        'теги' : ['черновик', 'мысли']
    }
}
with open('f.json', 'w', encoding='utf-8') as file:
    json.dump(notes, file, ensure_ascii=True)

def show_results():
    name = list1.selectedItems()[0].text()
    text.setText(notes[name]['текст'])
    list2.clear()
    list2.addItems(notes[name]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(
        main, 'Добавить заметку', 'Название заметки: '
    )
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        list1.addItem(note_name)
        list1.addItems(notes[note_name]['теги'])
        with open('f.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=True)

def del_note(): 
    if list1.selectedItems(): #проверяем заметку
        key = list1.selectedItems()[0].text() #получаем название
        del notes[key] #удаляем заметку
        text.clear()
        list1.clear()
        list2.clear()
        list1.addItems(notes)
        with open('notes_data.json', 'w', encoding='utf-8') as file:
           json.dump(notes, file, sort_keys=True, ensure_ascii=False) 

def add_tags():
    if list1.selectedItems():
        key = list1.selectedItems()[0].text()
        tag = low.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            low.clear()
        with open('f.json', 'w', encoding='utf-8')  as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print('Заметка для добавления тега не выбрана!')

def save_note():
    if list1.selectedItems():
        key = list1.selectedItems()[0].text()
        notes[key]['текст'] = text.toPlainText()
        with open('f.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_tag():
    if list1.selectedItems():
        key = list1.selectedItems()[0].text() #Название заметки
        tag = list2.selectedItems()[0].text()  #получаем название
        notes[key]['теги'].remove(tag)
        list2.clear()
        list2.addItems(notes[key]['теги'])
        with open('f.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def search_tag():
    tag = low.text()
    if button6.text() == 'Искать заметки по тегу' and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        button6.setText('Сбросить поиск')
        list1.clear()
        list2.clear()
        list1.addItems(notes_filtered)
    elif button6.text() == "Сбросить поиск":
        text.clear()
        list1.clear()
        list2.clear()
        list1.addItems(notes)
        button6.setText('Искать заметки по тегу')
    else:
        pass

with open('f.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)
list1.addItems(notes)
list1.itemClicked.connect(show_results)
button1.clicked.connect(add_note)
button2.clicked.connect(del_note)
button3.clicked.connect(save_note)
button4.clicked.connect(add_tags)
button5.clicked.connect(del_tag)
button6.clicked.connect(search_tag)
main.show()
app.exec_()
