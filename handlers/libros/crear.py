import datetime
import time
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from models.libro import Libro
from models.usuario import Usuario


class CrearLibroHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        
        valores_plantilla = {}
        
        if self.request.GET.keys():
            valores_plantilla['usuario'] = Usuario.recuperar(self.request, "id")
        else:
            self.redirect('/')

        self.response.write(jinja.render_template("crear_libro.html", **valores_plantilla))
    
    def post(self):
        titulo = self.request.get("edTitulo", "")
        autor = self.request.get("edAutor", "")
        str_fecha_pub = self.request.get("edFechaPub", "")

        try:
            fecha_pub = datetime.datetime.strptime(str_fecha_pub, "%Y-%m-%d")

        except ValueError:
            fecha_pub = -1
        
        if self.request.GET.keys():
            usuario = Usuario.recuperar(self.request, "id")
        else:
            self.redirect('/')

        if fecha_pub == -1 or not titulo or not autor:
            return self.redirect('/')
        else:
            libro = Libro(titulo=titulo, autor=autor, fecha_pub=fecha_pub, 
                creador=usuario.key)
            libro.put()
            time.sleep(1)
            return self.redirect('/?id={}'.format(usuario.key.urlsafe()))


app = webapp2.WSGIApplication([
    ('/libros/crear', CrearLibroHandler)
], debug=True)
