# Análisis y decisiones pedagógicas

Documento que justifica la estructura del programa de Ciencias de la Computación I: por qué se han elegido veintiún temas, cómo se reparten entre los cinco bloques oficiales y qué criterios metodológicos rigen el bloque de programación.

## Criterios editoriales

- Solo se incluye teoría: no hay prácticas, cuestionarios ni ponderaciones. Las prácticas y las pruebas de evaluación se desarrollarán por separado.
- Las páginas son autónomas, adaptables a móvil, imprimibles y navegables con teclado.
- Cada tema incluye pregunta guía, objetivos, conceptos desarrollados, ejemplos, glosario o resumen.
- No se incluyen marcadores de imágenes inexistentes: no se publican materiales incompletos.
- Se incluyen enlaces a fuentes curriculares y técnicas.
- La estructura de bloques reproduce literalmente la del currículo oficial; la agrupación en temas es la decisión propia de esta asignatura.

## Reparto general: veintiún temas

El currículo de 1.º fija cinco bloques con pesos muy desiguales. El reparto elegido es 3 + 4 + 3 + 5 + 6:

| Bloque | Temas | Nº |
| --- | --- | --- |
| A. Evolución histórica | 1–3 | 3 |
| B. Los sistemas informáticos | 4–7 | 4 |
| C. Software de sistema y de utilidad | 8–10 | 3 |
| D. Elaboración y difusión de la información | 11–15 | 5 |
| E. Programación | 16–21 | 6 |

La programación recibe el mayor número de temas porque concentra tres de los diez criterios de evaluación, es el bloque que la orden pide impartir «desde un enfoque eminentemente práctico» y es el único cuyo aprendizaje se construye por acumulación: cada tema depende del anterior. El bloque histórico recibe el menor número porque su contenido es extenso en enumeraciones pero homogéneo en dificultad.

## Bloque A — Decisión: tres temas

La secuencia responde a tres preguntas consecutivas:

1. **¿Qué es calculable y quién lo demostró?** Algoritmos, máquina de Turing, álgebra de Boole y computabilidad.
2. **¿Con qué máquinas se ha calculado a lo largo de la historia?** Del ábaco al circuito integrado.
3. **¿Qué ha cambiado en la sociedad?** Revolución digital, era de la información e impacto social.

### Por qué no dos o cuatro

- **Dos temas** obligarían a mezclar la fundamentación teórica con la cronología, o la cronología con el análisis social; en ambos casos una unidad quedaría desproporcionada.
- **Cuatro temas** fragmentarían la cronología en dos mitades sin una frontera conceptual clara.
- **Tres temas** separan lo que tiene naturaleza distinta: teoría, tecnología y sociedad.

### Decisiones de contenido

- Las tarjetas perforadas se estudian con las máquinas que las utilizaron (Tema 2) y no con los lenguajes de programación, con los que solo comparten la idea de instrucción almacenada.
- Los lenguajes de programación, la computación gráfica y los simuladores se llevan al Tema 3, donde sirven para explicar la revolución digital.
- La inteligencia artificial aparece dos veces con niveles distintos: como hito histórico en el Tema 2 y como fenómeno actual en el Tema 3.
- El álgebra de Boole se introduce en su papel fundacional; su uso operativo llega en el Tema 18, con las condiciones y los operadores lógicos de Python.

## Bloque B — Decisión: cuatro temas

La secuencia responde a cuatro preguntas consecutivas:

1. **¿De qué está hecho un sistema informático y cómo se mide la información?** Elementos, clasificación y representación binaria.
2. **¿Cómo se organiza por dentro?** Arquitectura de von Neumann, CPU, memoria y buses.
3. **¿Cómo se conecta y cómo arranca?** Placa base, firmware, alimentación y secuencia de arranque.
4. **¿Cómo entra, sale y se conserva la información?** Almacenamiento y periféricos.

### Por qué no tres o cinco

- **Tres temas** obligarían a reunir la placa base, los buses, el firmware y todos los periféricos en una unidad muy larga y enumerativa.
- **Cinco temas** separarían almacenamiento de periféricos, pero dejarían dos unidades cortas con una misma idea central.
- **Cuatro temas** equilibran la carga y permiten que cada unidad tenga una pregunta propia.

### Decisiones de contenido

- La representación binaria de la información, el bit, el byte y sus múltiplos se incorporan al Tema 4 aunque el texto oficial no los enumere: sin ellos no pueden explicarse ni la memoria del Tema 5 ni los tipos de datos del Tema 17.
- La codificación de caracteres (ASCII y Unicode) no se estudia aquí, sino en el Tema 19, junto a las cadenas de texto, donde resulta operativa.
- La alimentación y los sistemas de protección ante fallos se agrupan con la placa base porque comparten el mismo plano físico del equipo.
- El montaje y el desmontaje de equipos no se incorporan al programa teórico: corresponden a las prácticas.

## Bloque C — Decisión: tres temas

La secuencia responde a tres preguntas consecutivas:

1. **¿Quién gobierna la máquina?** El sistema operativo.
2. **¿Cómo se le dan instrucciones?** Lenguajes de programación y tipos de programación.
3. **¿Qué otras aplicaciones existen y en qué condiciones se usan?** Software de utilidad, licencias e instalación.

### Por qué no dos o cuatro

- **Dos temas** mezclarían el sistema operativo con los lenguajes o las licencias con los paradigmas de programación, que no comparten nivel de abstracción.
- **Cuatro temas** dejarían unidades demasiado breves: los tipos de programación no sostienen por sí solos un tema a este nivel.
- **Tres temas** respetan los tres subconjuntos naturales del bloque oficial.

### Decisiones de contenido

- El Tema 9 se titula «Lenguajes de programación y tipos de programación» para recoger literalmente los dos epígrafes oficiales, y sitúa Python entre los lenguajes interpretados de alto nivel antes de que el alumnado llegue al Bloque E.
- Los paradigmas se presentan a nivel de reconocimiento con ejemplos breves. La orientación a objetos se estudia en Ciencias de la Computación II, no aquí.
- La instalación y la prueba de aplicaciones se explican como procedimiento y criterios; su ejecución corresponde a las prácticas.

## Bloque D — Decisión: cinco temas

La secuencia responde a cinco preguntas consecutivas:

1. **¿Cómo se elabora un documento profesional?** Procesadores de texto y presentaciones.
2. **¿Cómo se calculan y se consultan datos?** Hojas de cálculo y bases de datos.
3. **¿Cómo trabaja y se organiza un equipo?** Comunicación, nube y gestión de proyectos.
4. **¿Cómo se publica información en la Web?** Diseño, edición y publicación de páginas web.
5. **¿Cómo hemos llegado hasta la Internet actual?** Evolución de la Web e impacto social.

### Por qué no tres o cuatro

- **Tres temas** reunirían toda la ofimática en una sola unidad, pese a que los criterios 3.1 y 3.2 distinguen el manejo adecuado de las funciones avanzadas.
- **Cuatro temas** obligarían a diluir la evolución de Internet dentro del tema de páginas web, mezclando una unidad técnica con otra de análisis social.
- **Cinco temas** mantienen separadas la producción documental, el tratamiento de datos, el trabajo en equipo, la publicación web y la reflexión sobre la Red.

### Decisiones de contenido

- La gestión de proyectos colaborativos recibe epígrafes propios en el Tema 13 porque la orden pide expresamente prestarle mayor atención por ser menos conocida por el alumnado.
- Las herramientas se nombran como ejemplos (Trello, Asana, Monday, Holded) sin convertir el programa en una lista cerrada de productos.
- El Tema 14 trabaja HTML y CSS como lenguajes de estructura y presentación; JavaScript solo se menciona por su función.
- La accesibilidad no se trata como un apartado final, sino como criterio de calidad en los temas 11 y 14.
- Las redes sociales aparecen en el Tema 13 desde el uso y en el Tema 15 desde el análisis; la seguridad y el malware corresponden al Bloque B de Ciencias de la Computación II.
- La edición de imagen, sonido y vídeo no pertenece a este curso: es el Bloque C de 2.º.

## Bloque E — Decisión: seis temas

La secuencia responde a seis preguntas consecutivas:

1. **¿Cómo se pasa de un problema a un programa?** Pensamiento computacional, descomposición y primer código en Jupyter Notebook.
2. **¿Con qué datos trabaja un programa?** Variables, tipos, operadores, entrada y salida.
3. **¿Cómo decide y cómo repite?** Condicionales y bucles.
4. **¿Cómo se manejan muchos datos a la vez?** Listas y cadenas.
5. **¿Cómo se organiza un programa que crece?** Funciones y modularidad.
6. **¿Dónde se ejecuta y cómo se comprueba que funciona?** Entornos, errores, pruebas y depuración.

### Por qué no cuatro o cinco

- **Cuatro temas** obligarían a impartir condicionales, bucles, listas y funciones en dos unidades muy densas, justo donde se produce la mayor parte del abandono en un primer curso de programación.
- **Cinco temas** exigirían fundir listas y cadenas con funciones, o entornos y depuración con el tema introductorio, perdiendo en ambos casos el cierre del bloque.
- **Seis temas** permiten una progresión de dificultad regular y dejan un tema final dedicado a entornos, pruebas y depuración, que el criterio 4.3 exige de forma explícita.

### Decisiones metodológicas

- **Python desde la primera sesión.** El lenguaje es único durante todo el curso. La orden permite escoger cualquier lenguaje y Python es el que da continuidad al Bloque D de Ciencias de la Computación II.
- **Jupyter Notebook con Google Colab como entorno principal.** No requiere instalación, funciona desde cualquier equipo del centro o de casa y permite alternar explicación y código ejecutable en el mismo documento.
- **Thonny como segundo entorno.** Se utiliza de forma acotada en el Tema 21 para mostrar la ejecución de programas en archivos `.py` y, sobre todo, para la depuración paso a paso con puntos de interrupción e inspección de variables, que un notebook no facilita igual de bien.
- **Diagramas de flujo: tratamiento breve.** El currículo oficial los enumera como contenido, así que se presentan sus símbolos y se practica la lectura de un diagrama sencillo. Es suficiente para que el alumnado reconozca la notación cuando aparezca en un libro, en una prueba o en un esquema ajeno. No se convierten en método de diseño ni se exige elaborarlos para cada programa.
- **Pseudocódigo en lenguaje natural, nunca en un lenguaje formal.** Los algoritmos se describen de viva voz o por escrito en español corriente, con ejemplos, entradas y salidas esperadas. No se enseña ninguna notación formal de pseudocódigo ni herramientas del tipo PSeInt: obligan a aprender una sintaxis intermedia, con sus propias reglas y sus propios errores, que después hay que abandonar. Ese esfuerzo se invierte en Python, que es ejecutable desde el primer día y da continuidad a Ciencias de la Computación II. El paso del enunciado al programa se hace directamente en Python, apoyado en casos de prueba y en desarrollo incremental.
- **Los vectores del texto oficial se estudian como listas de Python**, que es su realización natural en el lenguaje elegido.
- **La compilación se explica, no se practica.** El criterio 4.3 menciona la compilación; en un curso basado en Python se aborda como concepto, comparando compiladores, intérpretes y máquinas virtuales en los temas 9 y 21.
- **La programación se concentra en el Bloque E.** No se reparte en pequeñas dosis dentro de los bloques A a D: cada bloque conserva su objeto propio y Python se trabaja de forma continuada en los temas 16 a 21, donde la progresión de dificultad puede sostenerse sesión a sesión.
- **Las pruebas y la depuración aparecen desde el Tema 16** como hábito de trabajo y se formalizan en el Tema 21.
- **No se incluyen** ficheros, diccionarios, clases ni control de versiones: son contenido del Bloque D de Ciencias de la Computación II.

## Relación con Ciencias de la Computación II

El programa se ha escrito comprobando el de 2.º curso para evitar solapamientos y huecos:

- Las redes se anuncian en el Bloque B, pero se desarrollan en CC II.
- La seguridad, el malware y la criptografía no se tratan en 1.º.
- La edición de imagen, sonido y vídeo pertenece al Bloque C de CC II.
- El Bloque E deja asentados variables, tipos, operadores, entrada y salida, condicionales, bucles, listas, cadenas y funciones, que el Tema 14 de CC II reactiva programando en lugar de reexplicar.
- Los diccionarios, las tuplas y los conjuntos no se estudian en 1.º: el texto oficial habla de «variables y vectores», y el Tema 15 de CC II los presenta juntos para enseñar a escoger la colección adecuada. Adelantarlos aquí, sin ficheros ni JSON en los que resulten necesarios, los convertiría en memorización.
- Ficheros, clases, excepciones y entornos móviles corresponden también a CC II.
