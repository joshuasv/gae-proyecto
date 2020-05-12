"""
    Entidad Usuario
        nombre  text
        email   text
"""

from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

    @staticmethod
    def recuperar(request, identifier):
        try:
            id = request.GET[identifier]
        except KeyError:
            id = ""
        return ndb.Key(urlsafe=id).get()