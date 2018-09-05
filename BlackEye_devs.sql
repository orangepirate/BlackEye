-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: BlackEye
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `devs`
--

DROP TABLE IF EXISTS `devs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `devs` (
  `dev_id` int(11) NOT NULL AUTO_INCREMENT,
  `dev_ip` varchar(45) NOT NULL,
  `dev_domain` varchar(45) DEFAULT NULL,
  `dev_hostname` varchar(45) DEFAULT NULL,
  `dev_hosttype` varchar(45) DEFAULT NULL,
  `dev_vendor` varchar(45) DEFAULT NULL,
  `dev_state` varchar(45) DEFAULT NULL,
  `dev_ports` varchar(45) DEFAULT NULL,
  `dev_cpes` varchar(255) DEFAULT NULL,
  `dev_portsprotocals` varchar(255) DEFAULT NULL,
  `update_time` varchar(45) NOT NULL,
  PRIMARY KEY (`dev_id`,`dev_ip`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devs`
--

LOCK TABLES `devs` WRITE;
/*!40000 ALTER TABLE `devs` DISABLE KEYS */;
INSERT INTO `devs` VALUES (1,'117.34.14.240','','','','{}','up','[80, 443]','[\'\', \'\']','[\'tcpwrapped\', \'tcpwrapped\']','Wed Sep  5 10:55:41 2018'),(2,'123.58.182.251','','','','{}','up','[80, 443]','[\'\', \'\']','[\'tcpwrapped\', \'tcpwrapped\']','Wed Sep  5 11:03:20 2018'),(3,'123.58.182.252','','','','{}','up','[80, 443]','[\'\', \'\']','[\'tcpwrapped\', \'tcpwrapped\']','Wed Sep  5 11:03:20 2018');
/*!40000 ALTER TABLE `devs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-05 11:21:12
