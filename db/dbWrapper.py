import pymongo
import mongoengine as mongo
from db.Documents import *
import datetime
import dns # required for connecting with SRV

mongo.connect(db="smartMirrorDatabase", host="mongodb+srv://admin:tfgadmin@cluster0.cjbui.mongodb.net")

def saveNote(title, pinned, text, date, rgb):    
    noteToSave = Notes(_id=update_counter("notesid"), title=title, pinned=pinned, text=text, date=date, rgb=rgb)
    noteToSave.save()
    print("La nota " + title + " se ha guardado")

def getAllNotes():
    return Notes.objects

def findNoteById (noteId):
    return Notes.objects.get(_id=noteId)

def update_counter(sequenceName):
    contador=Counters.objects.get(_id=sequenceName)
    Counters(_id=sequenceName, cont=contador.cont+1).save()
    return contador.cont+1

def deleteNoteById(noteid):
    Notes.objects(_id=noteid).delete()

####################################

def getInfoDayHora():
    return infoDayHora.objects

def saveInfoDayHora(id, formato, color):    
    noteToSave = infoDayHora(_id=id, formato=formato, color=color)
    noteToSave.save()
    print("La hora se ha actualizado")


def getInfoDayFecha():
    return infoDayFecha.objects[0]

def saveInfoDayFecha(id, formato, color):    
    noteToSave = infoDayFecha(_id=id, formato=formato, color=color)
    noteToSave.save()
    print("La fecha se ha actualizado")


def getInfoDayTemp():
    return infoDayTemp.objects[0]

def saveInfoDayTemp(id, formato, color):    
    noteToSave = infoDayTemp(_id=id, formato=formato, color=color)
    noteToSave.save()
    print("La temperatura se ha actualizado")


def getInfoDayClima():
    return infoDayClima.objects

def saveInfoDayClima(id, formato):    
    noteToSave = infoDayClima(_id=id, formato=formato)
    noteToSave.save()
    print("El clima se ha actualizado")

# saveNote("Escuela", True, "Tengo que recoger al niño de la escuela", datetime.date(2021, 1, 21), [224, 187, 228,1])
# saveNote("prueba", False, "vaya dia de meirda", datetime.date(2021, 1, 21), [125, 150, 176,1])
# saveNote("eat the rich", True, "eat the rich", datetime.date(2021, 1, 21), [140, 183, 141,1])
# saveNote("Agua", True, "cambiarle el agua al perro", datetime.date(2021, 1, 21), [149, 125, 173,1])

print(getAllNotes())
# print(findNoteById(2).text)
saveInfoDayClima("hora", "sdfsdfsf")
