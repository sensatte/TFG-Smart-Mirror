import pymongo
import mongoengine as mongo
from db.Documents import *
import datetime
import dns  # required for connecting with SRV
import logging

mongo.connect(db="smartMirrorDatabase",
              host="mongodb+srv://admin:tfgadmin@cluster0.cjbui.mongodb.net")


def saveNote(pinned, text, date, rgb):    
    noteToSave = Notes(_id=update_counter("notesid"), pinned=pinned, text=text, date=date, rgb=rgb)
    noteToSave.save()
    print("La nota " + text + " se ha guardado")


def getAllNotes():
    return Notes.objects


def findNoteById(noteId):
    return Notes.objects.get(_id=noteId)


def update_counter(sequenceName):
    contador = Counters.objects.get(_id=sequenceName)
    Counters(_id=sequenceName, cont=contador.cont+1).save()
    return contador.cont+1


def deleteNoteById(noteid):
    Notes.objects(_id=noteid).delete()

####################################

def getHora():
    return Hora.objects[0]

def saveHora(id, formato, color):    
    noteToSave = Hora(_id=id, formato=formato, color=color)
    noteToSave.save()
    print("La hora se ha actualizado")


def getFecha():
    return Fecha.objects[0]

def saveFecha(id, formato, color):    
    noteToSave = Fecha(_id=id, formato=formato, color=color)
    noteToSave.save()
    print("La fecha se ha actualizado")


def getTemp():
    return Temp.objects[0]

def saveTemp(id, formato, color, c_id):    
    noteToSave = Temp(_id=id, formato=formato, color=color, c_id=c_id)
    noteToSave.save()
    print("La temperatura se ha actualizado")


def getClima():
    return Clima.objects[0]

def saveClima(id, formato, c_id):    
    noteToSave = Clima(_id=id, formato=formato, c_id=c_id)
    noteToSave.save()
    print("El clima se ha actualizado")

####################################

def getAllGifs():
    return Gifs.objects

def getPinnedGifs():
    return Gifs.objects(pinned=True)

def findGifById(gifId):
    return Gifs.objects.get(_id=gifId)

def saveGif(source):

    gifToSave = Gifs(
        _id=update_counter("gifsid"),
        source=source,
        pinned=True,
        posX=50,
        posY=50,
        sizeX=.3,
        sizeY=.2,
        rotation=0,
        delay=.1,
    )
    gifToSave.save()
    print("El gif se ha guardado")


def deleteGifById(gifid):
    Gifs.objects(_id=gifid).delete()
####################################

def getAllWeight():
    return Gym.objects

def getWeightByMonth(mes):
    return [x for x in Gym.objects if x.month==mes]

def saveWeight(weight):    
    ultimo=getAllWeight()[len(getAllWeight()) - 1]
    hoy=datetime.date.today()
    if(ultimo.year==hoy.year and ultimo.month==hoy.month and ultimo.day==hoy.day):
        ultimo.weight=weight
        ultimo.save()
        print("El peso " + str(weight) + " se ha actualizado")
    else:
        noteToSave = Gym(weight=weight, year=hoy.year, month=hoy.month, day=hoy.day)
        noteToSave.save()
        print("El peso " + str(weight) + " se ha guardado")

##################################

def saveInternacional(dia, info):
    dayToSave = Internacional(dia=dia, info=info)
    dayToSave.save()

def getInternacionalByDay(dia):
    return Internacional.objects(dia= dia)
# print(getWeightByMonth(2))
# saveNote(True, "Tengo que recoger al niño de la escuela", datetime.date(2021, 1, 21), [224, 187, 228,1])
# saveNote(False, "vaya dia de meirda", datetime.date(2021, 1, 21), [125, 150, 176,1])
# saveNote(True, "eat the rich", datetime.date(2021, 1, 21), [140, 183, 141,1])
# saveNote( True, "cambiarle el agua al perro", datetime.date(2021, 1, 21), [149, 125, 173,1])

# print(getHora().formato)
# print(getFecha().formato)
# print(getTemp().formato)
# print(getClima().formato)

# print(getAllNotes())
# print(findNoteById(2).text)
