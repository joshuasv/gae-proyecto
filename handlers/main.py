#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import datetime
import time
import webapp2
from webapp2_extras.users import users
from webapp2_extras import jinja2
from models.libro import Libro
from models.usuario import Usuario
from models.like import Like

def create():
    fecha_pub = datetime.datetime.strptime("2012-10-3", "%Y-%m-%d")
    for i in range(3):
        usuario = Usuario(nombre="Nuevo{}".format(i), email="nuevo{}@nuevo.com".format(i))
        usuario.put()
    time.sleep(2)
    usuario0 = Usuario.query(Usuario.nombre=="Nuevo0").get()
    usuario1 = Usuario.query(Usuario.nombre=="Nuevo1").get()
    usuario2 = Usuario.query(Usuario.nombre=="Nuevo2").get()

    for i in range(3):
        libro = Libro(titulo="Titulo{}".format(i), autor="Autor{}".format(i),
            fecha_pub=fecha_pub, creador=usuario0.key)
        libro.put()
    for i in range(3):
        libro = Libro(titulo="Titulo{}".format(i+3), autor="Autor{}".format(i+3),
            fecha_pub=fecha_pub, creador=usuario1.key)
        libro.put()
    for i in range(3):
        libro = Libro(titulo="Titulo{}".format(i+6), autor="Autor{}".format(i+6),
            fecha_pub=fecha_pub, creador=usuario2.key)
        libro.put()

def delete():
    libros = Libro.query()
    for l in libros:
        l.key.delete()

    usuarios = Usuario.query()
    for u in usuarios:
        u.key.delete()


class MainHandler(webapp2.RequestHandler):

    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        libros = Libro.query()
        likes = Like.query()
        usuarios = Usuario.query()

        valores_plantilla = {
            'usuarios': usuarios,
            'libros': libros,
            'likes': {libro.key: Like.numero_likes_libro(libro) for libro in libros},
            'likes_usuarios': {libro.key: Like.usuarios_likes_libro(libro) for libro in libros}
        }
        
        Like.usuarios_likes_libro(Libro.query(Libro.titulo=="Titulo1").get())

        # Todos los usuarios que le dieron like al libro.
        if self.request.GET.keys():
            valores_plantilla['usuario'] = Usuario.recuperar(self.request, "id")
            valores_plantilla['mis_libros'] = Libro.query(Libro.creador == valores_plantilla['usuario'].key)

        self.response.write(jinja.render_template("index.html", **valores_plantilla))


# create()


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


