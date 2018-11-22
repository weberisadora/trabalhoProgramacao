# Host: localhost  (Version 5.7.14)
# Date: 2018-11-22 11:32:12
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "horarios"
#

DROP TABLE IF EXISTS `horarios`;
CREATE TABLE `horarios` (
  `idHorario` int(11) NOT NULL AUTO_INCREMENT,
  `horario` time(6) DEFAULT NULL,
  `segunda` varchar(255) DEFAULT NULL,
  `terca` varchar(255) DEFAULT NULL,
  `quarta` varchar(255) DEFAULT NULL,
  `quinta` varchar(255) DEFAULT NULL,
  `sexta` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idHorario`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

#
# Data for table "horarios"
#

/*!40000 ALTER TABLE `horarios` DISABLE KEYS */;
INSERT INTO `horarios` VALUES (1,'08:30:00.000000','Matemática','Português',NULL,NULL,'Química'),(3,'07:30:00.000000',NULL,'huhu',NULL,NULL,NULL);
/*!40000 ALTER TABLE `horarios` ENABLE KEYS */;
