# Eliminar libro
import time
import webapp2
from webapp2_extras import jinja2
from models.libro import Libro


class EliminarLibroHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        
        libro = Libro.recuperar(self.request, "id")
        libro.key.delete()
        time.sleep(1)

        return self.redirect('/')

        


app = webapp2.WSGIApplication([
    ('/libros/eliminar', EliminarLibroHandler)
], debug=True)
