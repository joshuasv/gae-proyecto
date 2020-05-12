# Eliminar libro
import time
import webapp2
from webapp2_extras import jinja2
from models.libro import Libro
from models.usuario import Usuario


class ListarLibroHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)

        if self.request.GET.keys():
            usuario = Usuario.recuperar(self.request, "id")
            libros = Libro.query(Libro.creador == usuario.key)
            valores_plantilla = {
                'mis_libros': libros
            }
        else:
            self.response.write(jinja.render_template("/", **valores_plantilla))
        
        libro = Libro.recuperar(self.request)
        libro.key.delete()
        time.sleep(1)

        return self.redirect('/')

        


app = webapp2.WSGIApplication([
    ('/libros', ListarLibroHandler)
], debug=True)
