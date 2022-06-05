-- Esta consulta representaría los horarios de todo el curso de un profesor concreto
-- Los inner join se pueden enlazar siempre y cuando haya dos campos con correspondencias en sus valores. Esto se da entre foreign keys pero no es requisito indispensable que sean foreign keys, sino que haya correspondencia

SELECT
CONCAT(p.nombre, ' ', p.apellido_1) AS nombre_completo,
h.dia AS dia,
h.hora AS hora,
a.nombre AS nombre_alumno
FROM profesor p
INNER JOIN clase c
	ON p.codigo = c.profesor
INNER JOIN (horario_plantilla h, alumno a)
	ON c.horario = h.codigo AND c.alumno = a.codigo
WHERE p.nombre = 'Alfredo'
ORDER BY 2, 3 ASC;



SELECT * FROM evaluacion;


-- Consulta para saber las notas de cada alumno
-- Por temas de hacer inserciones a lo bestia todos los alumnos están apuntados a todas las clases
-- Eso crea alguna inconsistencia como que estén apuntados, en este caso, a dos profesores de fagot, pero eso sería cuestión de cambiar las inserciones

-- La otra cosa importante de esta consulta que yo he aprendido es que no es buena idea hacer el inner join de evaluación a clase. Te saca chorrocientos resultados porque hace cruces de manera rara.
-- Por eso lo cruzo directamente con profesor y alumno, que al final lo único que quiero son los nombres

SELECT
concat(a.nombre, ' ', a.apellido_1) AS alumno,
nota_final,
m.nombre AS Instrumento,
CONCAT(p.nombre, ' ', p.apellido_1) AS profesor
FROM evaluacion e
INNER JOIN (alumno a, profesor p)
	ON e.alumno = a.codigo AND e.profesor = p.codigo
INNER JOIN materia m
	ON p.materia = m.codigo
ORDER BY 1;


-- Si el script no funciona en su estado tal cual lo paso, quizá es por alguna expresión que en MySql sea diferente de MariaDB. No creo que sean abundantes ni difíciles de encontrar.