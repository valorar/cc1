# Programa de la asignatura — Ciencias de la Computación I

## 1.º de Bachillerato · optativa · Comunidad de Madrid

Documento de referencia de los contenidos teóricos de la asignatura, organizado según los cinco bloques oficiales del currículo. Integra los bloques A, B, C, D y E (temas 1 a 21). No incluye prácticas ni instrumentos de evaluación, que se tratarán por separado.

En el bloque de programación se trabaja con **Python desde la primera sesión**, en **Jupyter Notebook** a través de **Google Colab**, y con **Thonny** como segundo entorno local para la ejecución de programas y la depuración paso a paso.

## Bloque A — Ciencias de la computación. Evolución histórica

### Tema 1. Fundamentos teóricos: algoritmos, lógica y computabilidad

Qué estudian las ciencias de la computación, quiénes sentaron sus bases y hasta dónde llega lo que una máquina puede calcular.

- objeto y alcance de las ciencias de la computación.
- Ada Lovelace, Alan Turing y John von Neumann: aportaciones fundacionales.
- teoría de algoritmos: concepto de algoritmo y propiedades.
- la máquina de Turing como modelo de cómputo.
- álgebra de Boole: variables lógicas y operaciones básicas.
- computación y computabilidad.
- problemas de decisión y problemas indecidibles.
- límites de lo calculable y noción intuitiva de coste.

### Tema 2. De las primeras máquinas de calcular al circuito integrado

Cómo la mecánica, la electricidad y la electrónica fueron sustituyendo al cálculo manual hasta llegar al chip.

- ábaco, logaritmos de Napier y regla deslizante (William Oughtred, 1621).
- la rueda de Pascal o pascalina (Blaise Pascal, 1642).
- la máquina diferencial de Charles Babbage (1822) y la máquina analítica.
- las tarjetas perforadas y la automatización del cálculo.
- la válvula de vacío y el primer ordenador electrónico (ENIAC, 1943‑1946).
- el transistor y la miniaturización de los circuitos.
- el circuito integrado y el chip; generaciones de ordenadores.
- los sensores, la robótica y los primeros sistemas de inteligencia artificial como último eslabón de esta cadena de avances.

### Tema 3. La revolución digital, la era de la información y su impacto social

Cómo el ordenador dejó de ser una máquina de cálculo para convertirse en una infraestructura social, y qué consecuencias tiene ese cambio.

- el comienzo de la revolución digital y la era de la información.
- el nacimiento de Internet como hito de la revolución digital; su evolución como red de servicios se estudia en el Tema 15.
- evolución de los lenguajes de programación.
- la computación gráfica y los simuladores.
- computación y sociedad: impacto en el desarrollo social y económico.
- beneficios y efectos negativos: brecha digital, empleo, privacidad y consumo de recursos.
- la inteligencia artificial actual y el debate sobre sus consecuencias.
- criterios para analizar de forma crítica un avance tecnológico.

## Bloque B — Los sistemas informáticos

### Tema 4. Elementos y clasificación de un sistema informático

Qué piezas forman un sistema informático, qué papel cumple cada una y cómo se mide y se representa la información que manejan.

- concepto de sistema informático y relación entre sus partes.
- subsistema físico (hardware), subsistema lógico (software) y el usuario.
- perfiles humanos: analistas, programadores, operarios y usuarios finales.
- ordenadores personales, sistemas departamentales y grandes ordenadores.
- otros formatos actuales: portátiles, dispositivos móviles, sistemas embebidos y servidores en la nube.
- representación binaria de la información: bit, byte y múltiplos.
- unidades de capacidad, velocidad de transferencia y frecuencia.
- criterios de clasificación: prestaciones, número de usuarios, coste y uso previsto.

### Tema 5. Arquitectura de von Neumann: procesador, memoria y buses

Cómo se organiza internamente un ordenador y por qué esa organización explica su rendimiento.

- arquitectura de von Neumann: procesador, memoria, interfaces de entrada y salida y buses.
- la unidad central de proceso (CPU): unidad de control y unidad aritmético‑lógica.
- ciclo de instrucción, frecuencia de reloj, núcleos y ejecución simultánea.
- memoria principal: RAM y ROM.
- memoria caché y jerarquía de memoria.
- bus de datos, bus de direcciones y bus de control.
- relación entre procesador, memoria y buses en el rendimiento del equipo.
- evolución de la arquitectura de los sistemas informáticos en la historia reciente.

### Tema 6. La placa base, la alimentación y el arranque del equipo

Cómo se conectan físicamente los componentes, de dónde obtienen energía y qué ocurre desde que se pulsa el botón de encendido.

- la placa base (mainboard): función e integración de los componentes.
- conectores de alimentación, zócalo de CPU y ranuras de RAM.
- chipset: el modelo histórico de puente norte y puente sur y su integración actual en el procesador y en un único chip.
- reloj del sistema y memoria de configuración CMOS.
- firmware: BIOS y UEFI.
- buses de expansión, conectores y puertos más frecuentes en los equipos.
- subsistema de alimentación: fuente, potencia y sistemas de protección ante fallos (SAI).
- secuencia de arranque de un equipo informático y gestor de arranque (bootloader).

### Tema 7. Almacenamiento y periféricos de entrada, salida y comunicación

Cómo se conserva la información y cómo entra y sale del sistema informático.

- dispositivos de almacenamiento: disco duro, unidad de estado sólido, óptico, memoria flash y almacenamiento en red.
- capacidad, velocidad, latencia, volatilidad y fiabilidad.
- dispositivos de entrada.
- dispositivos de salida.
- dispositivos mixtos y dispositivos de comunicación.
- conexión de periféricos: puertos, interfaces y controladores de dispositivo.
- criterios para dimensionar y elegir el equipamiento de un puesto de trabajo.
- mantenimiento básico, consumo energético y ciclo de vida del hardware.

## Bloque C — Software de sistema y de utilidad

### Tema 8. El sistema operativo

Qué hace el software que gestiona la máquina y cómo se organiza el trabajo del usuario sobre él.

- software de sistema y software de aplicación.
- funciones del sistema operativo: procesos, memoria, dispositivos, archivos y usuarios.
- interfaz de línea de comandos e interfaz gráfica de usuario (GUI).
- tipos de sistemas operativos: monousuario y multiusuario, monotarea y multitarea, de escritorio, de servidor, móviles y de tiempo real.
- componentes: núcleo, intérprete de comandos y sistema de archivos.
- organización de archivos y carpetas, rutas y permisos.
- sistemas operativos actuales, arranque múltiple y máquinas virtuales.
- gestión básica: cuentas de usuario, actualizaciones y copias de seguridad.

### Tema 9. Lenguajes de programación y tipos de programación

Cómo se traduce una idea a instrucciones que la máquina ejecuta y qué enfoques existen para escribir programas.

- lenguajes de bajo nivel: código máquina y ensamblador.
- lenguajes de alto nivel y su evolución.
- traducción de programas: compiladores, intérpretes y máquinas virtuales.
- Python como lenguaje interpretado de alto nivel y propósito general.
- programación declarativa e imperativa.
- programación estructurada y programación modular.
- programación orientada a objetos.
- programación orientada a eventos y criterios para elegir lenguaje y enfoque.

### Tema 10. Software de utilidad, licencias e instalación

Qué aplicaciones acompañan al sistema operativo, en qué condiciones se usan y cómo se instalan y valoran.

- software de utilidad y tipos de aplicaciones.
- software libre y software propietario; código abierto.
- tipos de licencia y condiciones de uso.
- requerimientos mínimos y recomendados de una aplicación.
- instalación, configuración, actualización y desinstalación.
- prueba y valoración de una aplicación y búsqueda de alternativas equivalentes.
- aplicaciones de escritorio, portables, web y móviles.
- procedencia del software, riesgos de las descargas y mantenimiento del equipo.

## Bloque D — Elaboración y difusión de la información

### Tema 11. Documentación electrónica: procesadores de texto y presentaciones

Cómo producir documentos y presentaciones bien estructurados, reutilizables y accesibles.

- ofimática y documentación electrónica: suites, formatos y compatibilidad.
- estructura de un documento: estilos, plantillas, secciones y numeración.
- índices automáticos, referencias, citas y bibliografía.
- funciones avanzadas: combinación de correspondencia, formularios y campos.
- presentaciones: guion, patrones de diapositiva, jerarquía visual y elementos multimedia.
- revisión, control de cambios y comentarios sobre un mismo documento.
- exportación a PDF y accesibilidad del documento.
- normas de presentación de trabajos académicos.

### Tema 12. Hojas de cálculo y bases de datos

Cómo organizar, calcular y consultar datos, y cuándo conviene cada herramienta.

- hoja de cálculo: celdas, rangos, tipos de datos y formatos.
- fórmulas, referencias relativas y absolutas y funciones habituales.
- funciones avanzadas: condicionales, búsqueda, texto y fechas.
- ordenación, filtros, tablas dinámicas y gráficos.
- bases de datos: tabla, registro, campo y clave.
- diseño de una base de datos sencilla; consultas, formularios e informes.
- relación entre hoja de cálculo y base de datos: criterios para elegir una u otra.
- importación y exportación de datos en CSV y calidad de los datos.

### Tema 13. Comunicación, almacenamiento en la nube y gestión de proyectos

Cómo se comunica y se organiza un equipo de trabajo con herramientas digitales.

- software de comunicación: correo electrónico y gestores de agenda.
- mensajería, videoconferencia y entornos virtuales de comunicación en tiempo real.
- redes sociales: usos, oportunidades y riesgos.
- identidad digital, privacidad y normas de comportamiento en línea.
- herramientas de gestión de archivos y almacenamiento en la nube.
- contenidos compartidos, permisos de acceso y edición colaborativa.
- herramientas de gestión de proyectos colaborativos (Trello, Asana, Monday, Holded u otras).
- planificación de un proyecto en equipo: tareas, responsables, plazos y seguimiento.

### Tema 14. Diseño, edición y publicación de páginas web

Cómo se construye y se publica un sitio web y qué condiciones debe cumplir para ser útil y accesible.

- funcionamiento de la Web: cliente, servidor, URL y protocolo HTTP.
- lenguajes de la Web: HTML para la estructura, CSS para la presentación y papel de JavaScript.
- elementos de una página: encabezados, párrafos, listas, enlaces, imágenes y tablas.
- hojas de estilo y diseño adaptable a distintos dispositivos.
- aplicaciones y entornos para crear sitios web: editores de código y gestores de contenidos.
- organización de la información, navegación y presentación de los contenidos.
- publicación de páginas web: alojamiento, dominio y mantenimiento.
- estándares de accesibilidad de la información y buenas prácticas de publicación.

### Tema 15. La evolución de Internet y su impacto social

Cómo ha cambiado Internet desde la consulta de información hasta la red de datos e inteligencia artificial actual.

- de la red de redes a la Web: qué aporta la Web sobre la Internet ya presentada en el Tema 3.
- la web 1.0: acceso instantáneo a la información y sociedad de la información y la comunicación.
- la web 2.0: interoperabilidad, creación colaborativa de contenidos y web social.
- usos y riesgos de las redes sociales y sus aplicaciones.
- la web 3.0: Internet de las cosas, inteligencia artificial en la red y Big Data.
- datos personales, publicidad y modelos de negocio en Internet.
- contraste y verificación de la información; desinformación.
- derechos de autor, licencias libres y atribución de la autoría.

## Bloque E — Programación

### Tema 16. Del problema al programa: algoritmos y primeros pasos con Python

Cómo se pasa de un problema enunciado en palabras a un programa que funciona, trabajando con código Python ejecutable desde la primera sesión.

- elementos de programación: programa, algoritmo, código fuente y ejecución.
- conceptos básicos: ingeniería de software y evolución de la programación.
- propiedades de un algoritmo y tipos: estáticos, probabilísticos y adaptativos.
- pensamiento computacional: descomposición de un problema mayor en otros más pequeños, reconocimiento de patrones y abstracción.
- resolución de problemas mediante programación: del enunciado al programa.
- diagramas de flujo: símbolos y lectura de un diagrama sencillo, de forma breve.
- descripción de algoritmos en lenguaje natural, sin notaciones formales de pseudocódigo.
- Python en Jupyter Notebook con Google Colab: celdas, ejecución y estado de la sesión.
- primer programa: salida por pantalla, comentarios y errores más frecuentes.
- método de trabajo: ejemplos, entradas, salidas esperadas y comprobación de resultados.

### Tema 17. Datos, variables, operadores, entrada y salida

Cómo se representan y se combinan los datos dentro de un programa y cómo dialoga el programa con quien lo usa.

- variables, identificadores y asignación.
- tipos de datos: enteros, reales, cadenas y booleanos.
- conversión de tipos y errores de tipo más habituales.
- operadores aritméticos, relacionales y lógicos; precedencia.
- expresiones y evaluación paso a paso.
- entrada de datos con `input()` y salida con `print()`.
- formato de la salida y cadenas formateadas.
- constantes, nombres significativos y legibilidad del código.

### Tema 18. Estructuras de control: condicionales y bucles

Cómo decide y cómo repite un programa, y cómo se combinan ambas cosas para resolver problemas reales.

- programación estructurada: secuencia, selección e iteración.
- sentencias de programación simples y estructuradas.
- selección con `if`, `elif` y `else`.
- condiciones compuestas y estructuras anidadas.
- bucles con `for`: recorrido de rangos y de secuencias.
- bucles con `while`: condición de parada y bucles infinitos.
- `break`, `continue`, contadores y acumuladores.
- diseño y comprobación de programas que combinan varias estructuras.

### Tema 19. Listas y cadenas: trabajar con conjuntos de datos

Cómo guardar muchos datos en una sola variable y cómo recorrerlos y transformarlos.

- vectores y listas: creación, índices y recorrido.
- añadir, modificar, eliminar y buscar elementos.
- longitud, pertenencia, ordenación y funciones de agregación.
- listas y bucles: recorrido con `for` y acumulación de resultados.
- cadenas de texto como secuencias: acceso, troceado y métodos habituales.
- codificación de caracteres: ASCII y Unicode.
- listas de listas para representar tablas sencillas.
- elección de la estructura de datos adecuada para cada problema.

### Tema 20. Funciones y organización de un programa

Cómo dividir un programa en piezas con nombre propio, reutilizables y fáciles de comprobar.

- concepto de función: definición, llamada y reutilización.
- parámetros, argumentos y valor de retorno.
- ámbito de las variables: local y global.
- funciones de la biblioteca estándar y módulos (`math`, `random`).
- descomposición de un programa en funciones y separación entre cálculo, entrada y presentación.
- documentación de funciones y elección de nombres claros.
- programación modular y reutilización del código.
- desarrollo incremental de un programa completo a partir de funciones.

### Tema 21. Entornos de programación, pruebas y depuración

Dónde se escribe y se ejecuta un programa, qué ocurre cuando falla y cómo se demuestra que una corrección funciona.

- componentes de un entorno de programación: editor, ejecución, consola, depurador y bibliotecas.
- Jupyter Notebook, con Google Colab, como entorno principal: celdas, estado de la sesión y archivos.
- Thonny como entorno local sencillo: archivos `.py`, ejecución y consola.
- ensamblaje o compilación frente a interpretación: qué ocurre al ejecutar un programa.
- tipos de error: sintaxis, ejecución (excepciones) y errores lógicos.
- lectura de mensajes de error y trazas de ejecución.
- depuración paso a paso con Thonny: puntos de interrupción e inspección de variables.
- prueba del programa: casos normales, casos límite y entradas no válidas.

## Cobertura curricular

Los cinco bloques del programa reproducen los cinco bloques de contenidos oficiales de 1.º de Bachillerato y conservan todos sus núcleos expresos.

**Bloque A (temas 1–3).** Se separan los fundamentos teóricos, la cronología de los avances tecnológicos y el análisis del impacto social. Las tarjetas perforadas se estudian en el Tema 2, junto a las máquinas que las utilizaron; los lenguajes de programación, la computación gráfica y los simuladores se tratan en el Tema 3, donde explican la revolución digital en lugar de quedar aislados.

**Bloque B (temas 4–7).** Los cuatro temas cubren los elementos del sistema informático, la clasificación de equipos, la arquitectura de von Neumann, los dispositivos de cómputo, almacenamiento, comunicación, entrada y salida, la placa base completa con su chipset, reloj, CMOS, firmware, buses y puertos, los subsistemas de alimentación y protección ante fallos y la secuencia de arranque con su gestor. La representación binaria de la información y las unidades de medida se incorporan al Tema 4 como base imprescindible para los bloques C y E, aunque el texto oficial no las enumere.

**Bloque C (temas 8–10).** Se mantiene el sistema operativo como unidad propia, se reúnen en un tema los lenguajes de programación y los tipos de programación —declarativa, imperativa, estructurada, modular, orientada a objetos y orientada a eventos— y se dedica un tercer tema al software de utilidad, las licencias, los requerimientos y la instalación. El Tema 9 prepara el Bloque E situando Python entre los lenguajes de alto nivel interpretados.

**Bloque D (temas 11–15).** Los cinco temas cubren la ofimática y la documentación electrónica, las funciones avanzadas, el software de comunicación, la gestión de archivos y el almacenamiento en la nube, las herramientas de gestión de proyectos colaborativos, el diseño, la edición y la publicación de páginas web con sus estándares de accesibilidad, y la evolución de Internet en sus tres etapas con su impacto social. La orden señala expresamente que debe prestarse mayor atención a las herramientas de gestión de proyectos colaborativos y a las funciones avanzadas de la ofimática, por lo que ambas reciben epígrafes propios.

**Bloque E (temas 16–21).** Los seis temas cubren los elementos de programación, los conceptos básicos, los tipos de algoritmos, los diagramas de flujo y el pseudocódigo, la resolución de problemas por descomposición, las estructuras básicas de la programación estructurada, los entornos de programación y la metodología de desarrollo completa: sentencias simples y estructuradas, sintaxis y codificación con variables, vectores, expresiones condicionales, selección, bucles y funciones, ensamblaje o compilación y prueba y depuración del programa. Los diagramas de flujo se presentan de forma breve para que el alumnado sepa leerlos, y los algoritmos se describen en lenguaje natural; el trabajo se realiza siempre escribiendo y ejecutando Python.

### Contenidos de ampliación

Los siguientes contenidos no figuran literalmente en el texto oficial y se incorporan de forma deliberada porque sostienen otros saberes del propio curso o actualizan el currículo. Se señalan aquí para que puedan distinguirse en cualquier momento de los saberes básicos:

- representación binaria de la información y unidades de medida (Tema 4).
- formatos actuales de equipos —portátiles, dispositivos móviles, sistemas embebidos y servidores en la nube— y máquinas virtuales (temas 4 y 8).
- mantenimiento básico, consumo energético y ciclo de vida del hardware (Tema 7).
- normas de presentación de trabajos académicos (Tema 11).
- contraste y verificación de la información, derechos de autor y licencias libres (Tema 15).
- codificación de caracteres ASCII y Unicode (Tema 19).
- documentación de funciones y uso de módulos de la biblioteca estándar (Tema 20).

Todo lo demás procede de los contenidos enumerados en el Anexo IV: la máquina de Turing, los problemas indecidibles, el álgebra de Boole, el chipset, la memoria CMOS, el firmware, el gestor de arranque, los sistemas de protección ante fallos, la programación orientada a objetos y a eventos, los diagramas de flujo, el pseudocódigo y la compilación aparecen en el texto oficial y no son añadidos de este programa.

## Alineación con los criterios de evaluación

- Bloque A (temas 1–3): criterio 1.1.
- Bloque B (temas 4–7): criterios 1.2, 1.3 y 2.1.
- Bloque C (temas 8–10): criterio 1.2, en su vertiente de subsistema lógico, con apoyo a 4.2 y 4.3.
- Bloque D (temas 11–15): criterios 3.1, 3.2 y 3.3.
- Bloque E (temas 16–21): criterios 4.1, 4.2 y 4.3.

## Continuidad con Ciencias de la Computación II

El programa se diseña para enlazar con el de 2.º de Bachillerato:

- El Bloque B prepara el estudio de las redes informáticas del Bloque A de CC II.
- El Bloque D anticipa el trabajo con imagen, sonido y vídeo del Bloque C de CC II y deja establecidas las cuestiones de licencias, autoría y accesibilidad.
- El Bloque E deja asentados variables, tipos, operadores, entrada y salida, condicionales, bucles, listas, cadenas y funciones en Python, que el Bloque D de CC II reactiva sin volver a explicarlos como unidades independientes.
- Jupyter Notebook con Google Colab y Thonny son los mismos entornos en los dos cursos.

## Fuentes curriculares mantenidas

- [Orden 1736/2023, de 19 de mayo, Anexo IV](https://www.bocm.es/boletin/CM_Orden_BOCM/2023/05/31/BOCM-20230531-18.PDF).
- [Decreto 64/2022, de 20 de julio](https://www.bocm.es/boletin/CM_Orden_BOCM/2022/07/26/BOCM-20220726-1.PDF).
- [Picuino: transcripción navegable del currículo](https://www.picuino.com/es/ley-ciencias-computacion-bach.html). Recurso de consulta.
