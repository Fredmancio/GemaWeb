-- Volcando estructura de base de datos para escuela_musica

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP DATABASE IF EXISTS escuela_musica;
CREATE DATABASE IF NOT EXISTS escuela_musica /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE escuela_musica;

-- Volcando estructura para tabla escuela_musica.alumno
CREATE TABLE IF NOT EXISTS alumno (
  `codigo` INTEGER(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `apellido_1` varchar(35) NOT NULL,
  `apellido_2` varchar(35) NOT NULL,
  `email` varchar(35) NOT NULL,
  `password` varchar(102) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla escuela_musica.alumno: ~0 rows (aproximadamente)
-- /*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
-- /*!40000 ALTER TABLE `alumno` ENABLE KEYS */;

-- Volcando estructura para tabla escuela_musica.clase
CREATE TABLE IF NOT EXISTS clase (
  `profesor` int(10) unsigned NOT NULL,
  `alumno` int(10) unsigned NOT NULL,
  `horario` int(10) unsigned NOT NULL,
  `deberes` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`profesor`,`alumno`,`horario`),
  UNIQUE KEY `unq_clase_profesor_horario` (`profesor`,`horario`),
  UNIQUE KEY `unq_clase_alumno_horario` (`alumno`,`horario`),
  KEY `fk_clase_alumno` (`alumno`),
  KEY `fk_clase_horario_plantilla` (`horario`),
  CONSTRAINT `fk_clase_alumno` FOREIGN KEY (`alumno`) REFERENCES `alumno` (`codigo`),
  CONSTRAINT `fk_clase_horario_plantilla` FOREIGN KEY (`horario`) REFERENCES `horario_plantilla` (`codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_clase_profesor` FOREIGN KEY (`profesor`) REFERENCES `profesor` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla escuela_musica.clase: ~0 rows (aproximadamente)
 /*!40000 ALTER TABLE `clase` DISABLE KEYS */;
 /*!40000 ALTER TABLE `clase` ENABLE KEYS */;

-- Volcando estructura para tabla escuela_musica.evaluacion
CREATE TABLE IF NOT EXISTS evaluacion (
  `profesor` int(10) unsigned NOT NULL,
  `alumno` int(10) unsigned NOT NULL,
  `nota_final` varchar(2) DEFAULT NULL,
  `trimestre` int(1) NOT NULL,
  `fecha` date,
  `comportamiento` varchar(2) default ' ',
  `sonido` varchar(2) default ' ',
  `lectura` varchar(2) default ' ',
  `precision` varchar(2) default ' ',
  `tecnica` varchar(2) default ' ',
  `programa` varchar(2) default ' ',
  `estudio` varchar(2) default ' ',
  `comentarios` VARCHAR(100),
  PRIMARY KEY (`profesor`,`alumno`, `trimestre`),
  CONSTRAINT `fk_evaluacion_clase` FOREIGN KEY (`profesor`, `alumno`) REFERENCES `clase` (`profesor`, `alumno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla escuela_musica.evaluacion: ~0 rows (aproximadamente)
 /*!40000 ALTER TABLE `evaluacion` DISABLE KEYS */;
 /*!40000 ALTER TABLE `evaluacion` ENABLE KEYS */;

-- Volcando estructura para tabla escuela_musica.horario_plantilla
CREATE TABLE IF NOT EXISTS horario_plantilla (
  `codigo` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `dia_semana` VARCHAR(10) NOT NULL,
  `hora` time NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


-- Volcando estructura para tabla escuela_musica.materia
CREATE TABLE IF NOT EXISTS materia (
  `codigo` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) NOT NULL,
  `familia` varchar(75) DEFAULT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla escuela_musica.materia: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `materia` DISABLE KEYS */;
/*!40000 ALTER TABLE `materia` ENABLE KEYS */;

-- Volcando estructura para tabla escuela_musica.partitura
CREATE TABLE IF NOT EXISTS partitura (
  `codigo` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(35) NOT NULL,
  `datos` BLOB NOT NULL,
  `profesor` int(10) unsigned NOT NULL,
  PRIMARY KEY (`codigo`),
  CONSTRAINT `fk_partitura_profesor` FOREIGN KEY (`profesor`) REFERENCES `profesor` (`codigo`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla escuela_musica.partitura: ~0 rows (aproximadamente)
 /*!40000 ALTER TABLE `partitura` DISABLE KEYS */;
 /*!40000 ALTER TABLE `partitura` ENABLE KEYS */;

-- Volcando estructura para tabla escuela_musica.profesor
CREATE TABLE IF NOT EXISTS profesor (
  `codigo` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `apellido_1` varchar(35) NULL,
  `apellido_2` varchar(35) NULL,
  `email` varchar(35) NOT NULL,
  `password` varchar(102) NOT NULL,
  `materia` int(10) unsigned NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `fk_profesor_materia` (`materia`),
  CONSTRAINT `fk_profesor_materia` FOREIGN KEY (`materia`) REFERENCES `materia` (`codigo`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla escuela_musica.profesor: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `profesor` DISABLE KEYS */;
/*!40000 ALTER TABLE `profesor` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;


-- Insertamos los datos de las materias
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Violín', 'Cuerda');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Viola', 'Cuerda');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Violonchelo', 'Cuerda');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Contrabajo', 'Cuerda');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Flauta', 'Viento Madera');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Clarinete', 'Viento Madera');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Oboe', 'Viento Madera');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Fagot', 'Viento Madera');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Trompeta', 'Viento Metal');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Trompa', 'Viento Metal');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Trombón', 'Viento Metal');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Tuba', 'Viento Metal');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Batería', 'Percusión');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Canto', 'Voz');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Piano', 'Tecla');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Guitarra', 'Cuerda');
INSERT INTO `escuela_musica`.`materia` (`nombre`, `familia`) VALUES ('Bajo', 'Cuerda');

-- Insertamos los datos de los horarios

INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '16:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '16:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '17:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '17:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '18:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '18:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '19:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '19:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '20:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '20:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '21:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Lunes', '21:30');

INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '16:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '16:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '17:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '17:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '18:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '18:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '19:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '19:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '20:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '20:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '21:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Martes', '21:30');

INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '16:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '16:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '17:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '17:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '18:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '18:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '19:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '19:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '20:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '20:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '21:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Miércoles', '21:30');

INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '16:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '16:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '17:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '17:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '18:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '18:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '19:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '19:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '20:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '20:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '21:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Jueves', '21:30');

INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '16:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '16:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '17:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '17:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '18:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '18:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '19:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '19:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '20:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '20:30');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '21:00');
INSERT INTO `escuela_musica`.`horario_plantilla` (`dia_semana`, `hora`) VALUES ('Viernes', '21:30');

-- Insertamos el administrador
INSERT INTO `escuela_musica`.`profesor` (`codigo`, `nombre`, `email`, `password`, `materia`) VALUES ('1', 'admin', 'admin@gema.com', 'pbkdf2:sha256:260000$TZyMh8aZ1IbWFlX8$62bbc87883b3bea76ca388f310e1e5132305efca98b74f8757320e8bb1e9fe8c', '1');


DELIMITER $$
-- ------------------------------------------
CREATE DEFINER = CURRENT_USER TRIGGER `escuela_musica`.`clase_AFTER_INSERT_1` AFTER INSERT ON `clase` FOR EACH ROW
BEGIN
		DECLARE prof_aux INT;
		DECLARE alum_aux INT;
        DECLARE trime_aux INT;

		
		SET prof_aux := 0;
		SET alum_aux := 0;
        SET trime_aux := 1;
		
		SELECT profesor, alumno  INTO prof_aux, alum_aux FROM evaluacion
		WHERE profesor = NEW.profesor AND alumno = NEW.alumno;
		
		if prof_aux = 0 AND alum_aux = 0 then
			while trime_aux < 4 do
			INSERT INTO evaluacion (profesor, alumno, trimestre)
			VALUES
			(NEW.profesor, NEW.alumno, trime_aux);
            SET trime_aux := trime_aux + 1;
			end while;
		END if;
END;




