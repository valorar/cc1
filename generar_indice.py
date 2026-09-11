# -*- coding: utf-8 -*-
import os, html

BLOQUES = [
 ("bloque_a", "Bloque A", "Ciencias de la computación. Evolución histórica",
  "Desde los fundamentos teóricos del cálculo y la computabilidad hasta las máquinas que los hicieron posibles y el impacto social de la revolución digital.",
  [(1, "Fundamentos teóricos: algoritmos, lógica y computabilidad",
      "Qué estudian las ciencias de la computación, quiénes sentaron sus bases y hasta dónde llega lo que una máquina puede calcular."),
   (2, "De las primeras máquinas de calcular al circuito integrado",
      "Cómo la mecánica, la electricidad y la electrónica fueron sustituyendo al cálculo manual hasta llegar al chip."),
   (3, "La revolución digital, la era de la información y su impacto social",
      "Cómo el ordenador se convirtió en una infraestructura social y qué consecuencias, buenas y malas, ha traído ese cambio.")]),
 ("bloque_b", "Bloque B", "Los sistemas informáticos",
  "Desde los elementos y la clasificación de un equipo hasta su arquitectura interna, la placa base, el arranque y los periféricos.",
  [(4, "Elementos y clasificación de un sistema informático",
      "Qué piezas forman un sistema informático, qué papel cumple cada una y cómo se mide y se representa la información."),
   (5, "Arquitectura de von Neumann: procesador, memoria y buses",
      "Cómo se organiza internamente un ordenador y por qué esa organización explica su rendimiento."),
   (6, "La placa base, la alimentación y el arranque del equipo",
      "Cómo se conectan los componentes, de dónde obtienen energía y qué ocurre desde que se pulsa el botón de encendido."),
   (7, "Almacenamiento y periféricos de entrada, salida y comunicación",
      "Cómo se conserva la información y cómo entra y sale del sistema informático.")]),
 ("bloque_c", "Bloque C", "Software de sistema y de utilidad",
  "Desde el sistema operativo que gobierna la máquina hasta los lenguajes de programación y el software de utilidad con sus licencias.",
  [(8, "El sistema operativo",
      "Qué hace el software que gestiona la máquina y cómo se organiza el trabajo del usuario sobre él."),
   (9, "Lenguajes de programación y tipos de programación",
      "Cómo se traduce una idea a instrucciones que la máquina ejecuta y qué enfoques existen para escribir programas."),
   (10, "Software de utilidad, licencias e instalación",
      "Qué aplicaciones acompañan al sistema operativo, en qué condiciones se usan y cómo se instalan y valoran.")]),
 ("bloque_d", "Bloque D", "Elaboración y difusión de la información",
  "Desde la documentación electrónica y el tratamiento de datos hasta el trabajo colaborativo, la publicación web y la evolución de Internet.",
  [(11, "Documentación electrónica: procesadores de texto y presentaciones",
      "Cómo producir documentos y presentaciones bien estructurados, reutilizables y accesibles."),
   (12, "Hojas de cálculo y bases de datos",
      "Cómo organizar, calcular y consultar datos, y cuándo conviene cada herramienta."),
   (13, "Comunicación, almacenamiento en la nube y gestión de proyectos",
      "Cómo se comunica y se organiza un equipo de trabajo con herramientas digitales."),
   (14, "Diseño, edición y publicación de páginas web",
      "Cómo se construye y se publica un sitio web y qué condiciones debe cumplir para ser útil y accesible."),
   (15, "La evolución de Internet y su impacto social",
      "Cómo ha cambiado Internet desde la consulta de información hasta la red de datos e inteligencia artificial actual.")]),
 ("bloque_e", "Bloque E", "Programación",
  "Desde los primeros programas en Python con Google Colab hasta las estructuras de control, las listas, las funciones y la depuración con Thonny.",
  [(16, "Del problema al programa: algoritmos y primeros pasos con Python",
      "Cómo se pasa de un problema enunciado en palabras a un programa que funciona, con código ejecutable desde la primera sesión."),
   (17, "Datos, variables, operadores, entrada y salida",
      "Cómo se representan y se combinan los datos dentro de un programa y cómo dialoga el programa con quien lo usa."),
   (18, "Estructuras de control: condicionales y bucles",
      "Cómo decide y cómo repite un programa, y cómo se combinan ambas cosas para resolver problemas reales."),
   (19, "Listas y cadenas: trabajar con conjuntos de datos",
      "Cómo guardar muchos datos en una sola variable y cómo recorrerlos, buscarlos y transformarlos."),
   (20, "Funciones y organización de un programa",
      "Cómo dividir un programa en piezas con nombre propio, reutilizables y fáciles de comprobar."),
   (21, "Entornos de programación, pruebas y depuración",
      "Dónde se escribe y se ejecuta un programa, qué ocurre cuando falla y cómo se demuestra que una corrección funciona.")]),
]

DOCS = "/Users/mag/Documents/cc1/cc1/docs"

def card(num, titulo, resumen):
    archivo = "tema%02d.html" % num
    existe = os.path.exists(os.path.join(DOCS, archivo))
    etiqueta = "Tema %02d" % num
    cuerpo = ('<span class="topic-number">%s</span><h2>%s</h2><p>%s</p>'
              % (etiqueta, html.escape(titulo), html.escape(resumen)))
    if existe:
        return ('<a class="topic-card" href="%s">%s<span class="go">Abrir tema →</span></a>'
                % (archivo, cuerpo))
    return ('<div class="topic-card is-pending">%s<span class="go">En preparación</span></div>'
            % cuerpo)

secciones = []
for sid, kicker, titulo, intro, temas in BLOQUES:
    tarjetas = "".join(card(*t) for t in temas)
    secciones.append(
        '<section class="index-section" aria-labelledby="%s"><p class="kicker index-kicker">%s</p>'
        '<h2 id="%s" class="index-heading">%s</h2><p class="index-intro">%s</p>'
        '<div class="topic-grid">%s</div></section>' % (sid, kicker, sid, titulo, intro, tarjetas))

doc = (
'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
'<meta name="description" content="Materiales de Ciencias de la Computación I para 1.º de Bachillerato">'
'<title>Ciencias de la Computación I · 1.º de Bachillerato</title>'
'<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">\n'
'<link rel="stylesheet" href="assets/estilos.css"></head><body><a class="skip" href="#contenido">Saltar al contenido</a>\n'
'<div class="progress" aria-hidden="true"><span></span></div>\n'
'<header class="site-header"><div class="header-inner">\n'
'  <a class="brand" href="index.html"><span class="brand-mark">CC1</span><span>Ciencias de la Computación I<small>1.º de Bachillerato · 2026–2027</small></span></a>\n'
'</div></header>\n'
'<main id="contenido"><section class="hero"><div class="hero-inner hero-index"><div>'
'<p class="kicker">1.º de Bachillerato · Curso 2026–2027</p><h1>Ciencias de la Computación I</h1>'
'<p class="hero-lead">Materiales de teoría organizados por bloques y temas para acompañar el trabajo de la asignatura.</p>'
'</div></div></section>\n'
'<div class="index-shell">' + "\n\n".join(secciones) + '</div></main>\n'
'<footer class="site-footer">Ciencias de la Computación I · 1.º de Bachillerato · Comunidad de Madrid</footer></body></html>\n')

open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(doc)
print("index.html escrito:", len(doc), "bytes")
