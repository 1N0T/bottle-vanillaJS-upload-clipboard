#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import base64

from bottle import route, run, response, request, abort, error, static_file


#===============================================================================
# Guardamos la imagen de la firma.
#===============================================================================
@route('/upload/', method='POST') 
def post_imagen():
    datos_json = request.body.read()
    if not datos_json:
        return {'status': 'KO', 'mensajes': ['No ha proporcionado datos. '], 'datos': []}
    else:
        objeto_datos = json.loads(datos_json.decode("utf-8"))
        if not 'id'  in objeto_datos   or \
           not 'img' in objeto_datos:
           return {'status': 'KO', 'mensajes': ['Faltan datos obligatorios. '], 'datos': []}
        else:
          file = open("./upload/%s" % (objeto_datos["id"]),"wb")
          file.write(base64.b64decode(objeto_datos["img"].replace("data:image/png;base64,", ""))) 
          file.close()
          
        return {'status': 'OK', 'mensajes': ['Imagen grabada correctamente.'], 'datos': []}
