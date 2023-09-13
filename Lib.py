import os
import datetime

def ShowNotes(file_name,option="none",date=""):
    counter = 0
    if os.path.exists(file_name) and (os.path.getsize(file_name) > 0):
        os.system("CLS")
        with open(file_name,"r") as file:
            data = file.readlines()
            for notes in data:
                notedata = notes.split(";")
                if (date == "") or (date == notedata[3]):
                    print(notedata[0] + " - " + notedata[1] + " - " + notedata[3])
                    counter += 1
        if counter == 0:
            print("Ничего не найдено")
        if option != "none":
            return int(input("Введите ID заметки, которую нужно "+("изменить" if option == "edit" else "удалить")+", или 0 для выхода в главное меню: "))
        else:
            input("\nНажмите эникей")
    else:
        print("Пока нет ни одной заметки...")
        input("\nНажмите эникей")

def AddNote(file_name,old_data=""):
    os.system("CLS")
    if old_data != "":
       print("Старые данные из заметки: ")
       notedata = old_data.split(";")
       print("Заголовок:" + notedata[1])
       print("Тело: " + notedata[2])
       print("Ниже укажите новые данные...")
    with open(file_name,"a") as file:
        if (old_data):
            res = notedata[0] + ";"
        else:
            res = str(NextId(file_name)) + ";"
        res += input("Заголовок: ").replace(";","") + ';'
        res += input("Тело: ").replace(";","") + ';'
        res += str(datetime.date.today()) + ';'
        file.write(res+"\n")
    if old_data == "":
        print("Заметка успешно добавлена")
        input("\nНажмите эникей")

def NextId(file_name):
    next_id = 1
    if os.path.exists(file_name) and (os.path.getsize(file_name) > 0):
        os.system("CLS")
        with open(file_name,"r") as file:
            data = file.readlines()
            for notes in data:
                notedata = notes.split(";")
                if int(notedata[0]) >= next_id:
                    next_id = int(notedata[0]) + 1
    return next_id

def LineNumberById(file_name,id):
    number = 0
    os.system("CLS")
    with open(file_name,"r") as file:
        data = file.readlines()
        for notes in data:
            number += 1
            notedata = notes.split(";")
            if notedata[0] == str(id):
                return number
    return 0

def EditNote(file_name):
    number = LineNumberById(file_name,ShowNotes(file_name,"edit"))
    file = open(file_name,"r")
    data = file.readlines()
    if number > 0:
        file.close()
        AddNote(file_name,data[number-1])
        DeleteNote(file_name,number)
        print("Заметка успешно изменёна")
    else:
        print("Редактирование отменено")
    input("\nНажмите эникей")

def DeleteNote(file_name,from_edit=0):
    if from_edit > 0:
        number = from_edit
    else:
        number = LineNumberById(file_name,ShowNotes(file_name,"delete"))
    file = open(file_name,"r")
    data = file.readlines()
    if number > 0:
        file.close()
        file = open(file_name,"w")
        res = ""
        for line in range(len(data)):
            if number-1 != line:
                res += data[line]
        file.write(res)
        if from_edit == 0:
            print("Заметка успешно удалёна")
            file.close()
            input("\nНажмите эникей")
    else:
        print("Удаление отменено")
        input("\nНажмите эникей")

def ShowNotesOnDate(file_name):
    os.system("CLS")
    ShowNotes(file_name,"none",input("Введите дату в формате ГГГГ-ММ-ДД: "))
        
def MainMenu():
    os.system("CLS")
    print("1 - Показать все заметки")
    print("2 - Показать заметки на нужную дату")
    print("3 - Добавить заметку")
    print("4 - Изменение заметку")
    print("5 - Удаление заметку")
    print("6 - Выход")

def Main(file_name):
    while True:
        os.system("CLS")
        MainMenu()
        try:
            user_choice = int(input("Введите число от 1 до 6: "))
            if user_choice == 1:
                ShowNotes(file_name)
            elif user_choice == 2:
                ShowNotesOnDate(file_name)
            elif user_choice == 3:
                AddNote(file_name)
            elif user_choice == 4:
                EditNote(file_name)
            elif user_choice == 5:
                DeleteNote(file_name)
            elif user_choice == 6:
                print("Всего доброго")
                return
        except ValueError:
            print("Это не число")
            input("\nНажмите эникей")


