"""
    Entidad Like
        fecha_hora  date    
        libro       libro   foreing key
        usuario     usuario foreing key
"""

from google.appengine.ext import ndb
from .usuario import Usuario
from.libro import Libro
 

class Like(ndb.Model):
    fecha_hora = ndb.DateTimeProperty(auto_now_add=True)
    libro = ndb.KeyProperty(kind=Libro)
    usuario = ndb.KeyProperty(kind=Usuario)


    @staticmethod
    def recuperar(request, identifier):
        try:
            id = request.GET[identifier]
        except KeyError:
            id = ""
        return ndb.Key(urlsafe=id).get()

    @staticmethod
    def numero_likes_libro(libro):
        likes = Like.query(Like.libro == libro.key)
        return likes.count()

    @staticmethod
    def usuarios_likes_libro(libro):
        toret = set()
        if libro:
            likes = Like.query(Like.libro == libro.key)
            for like in likes:
                toret.add(like.usuario)
        return toret
        
        



