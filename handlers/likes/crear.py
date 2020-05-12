# Nuevo libro
import datetime
import time
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from models.libro import Libro
from models.usuario import Usuario
from models.like import Like



class CrearLikeHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        
        valores_plantilla = {}
        
        if self.request.GET.keys():
            usuario = Usuario.recuperar(self.request, "id_usuario")
            libro = Libro.recuperar(self.request, "id_libro")

            like = Like(libro=libro.key, usuario=usuario.key)
            tiene_likes = Like.query(Like.libro == libro.key, Like.usuario == usuario.key)

            if libro.creador == usuario.key:
                print("NO PUEDES DAR LIKE A TU LIBRO")
            else:    
                if tiene_likes.count() == 0:
                    print("LE DISTE LIKE")
                    like.put()
                else:
                    print("YA TIENE TU LIKE")
            
            return self.redirect('/?id={}'.format(usuario.key.urlsafe()), body={"mira": "pepe"})
        else:
            self.redirect('/')

        


app = webapp2.WSGIApplication([
    ('/likes/crear', CrearLikeHandler)
], debug=True)
