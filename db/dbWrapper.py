import pymongo
import mongoengine as mongo
from db.Documents import Notes, Counters, Gifs
import datetime
import dns  # required for connecting with SRV
import logging

mongo.connect(db="smartMirrorDatabase",
              host="mongodb+srv://admin:tfgadmin@cluster0.cjbui.mongodb.net")


def saveNote(title, pinned, text, date, rgb):

    noteToSave = Notes(_id=update_counter("notesid"), title=title,
                       pinned=pinned, text=text, date=date, rgb=rgb)
    noteToSave.save()
    print("La nota " + title + "se ha guardado")


def getAllNotes():
    return Notes.objects


def findNoteById(noteId):
    return Notes.objects.get(_id=noteId)


def update_counter(sequenceName):
    contador = Counters.objects.get(_id=sequenceName)
    Counters(_id=sequenceName, cont=contador.cont+1).save()
    return contador.cont+1


# saveNote("Escuela", True, "Tengo que recoger al niño de la escuela", datetime.date(2021, 1, 21), "224", "187", "228")
# saveNote("prueba", False, "vaya dia de meirda", datetime.date(2021, 1, 21), "125", "150", "176")
# saveNote("eat the rich", True, "eat the rich", datetime.date(2021, 1, 21), "140", "183", "141")
# saveNote("Agua", True, "cambiarle el agua al perro", datetime.date(2021, 1, 21), "149", "125", "173")

# print(getAllNotes())
# print(findNoteById(2).text)

def getAllGifs():
    return Gifs.objects


def updateGif(_id, source, pos, size_hint, rotation=0):
    gifToSave = Gifs(
        _id=_id,
        source=source,
        posX=pos[0],
        posY=pos[1],
        sizeX=size_hint[0],
        sizeY=size_hint[1],
        rotation=rotation)

    gifToSave.save()
    logging.info('DB: Updated gif with id: '+str(_id))
