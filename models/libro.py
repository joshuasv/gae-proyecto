"""
    Entidad Libro
        titulo      text
        autor       text
        fecha_pub   date
        creador     usuario foreing key
"""

import datetime
from google.appengine.ext import ndb
from .usuario import Usuario


class Libro(ndb.Model):
    titulo = ndb.StringProperty(required=True)
    autor = ndb.StringProperty(required=True)
    fecha_pub = ndb.DateProperty(required=True)
    creador = ndb.KeyProperty(kind=Usuario)
    
    @staticmethod
    def recuperar(request, identifier):
        try:
            id = request.GET[identifier]
        except KeyError:
            id = ""
        return ndb.Key(urlsafe=id).get()