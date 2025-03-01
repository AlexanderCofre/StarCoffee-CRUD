-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-12-2023 a las 20:30:51
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba4`
--
CREATE DATABASE IF NOT EXISTS `prueba4` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `prueba4`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `identificador` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `rut` varchar(50) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `contrasena` varchar(50) DEFAULT NULL,
  `fecha` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`identificador`, `nombre`, `apellido`, `edad`, `rut`, `telefono`, `contrasena`, `fecha`) VALUES
(1, 'elias', 'briones', 20, '21388643-6', 63883716, '912ec803b2ce49e4a541068d495ab570', '2023-12-19 10:32:21'),
(8, 'Juan', 'Pérez', 30, '12345678-9', 987654321, 'adc83b19e793491b1c6ea0fd8b46cd9f', '2023-01-01 12:34:56'),
(9, 'María', 'Gómez', 25, '98765432-1', 123456789, '89b28c2db24a408c5fa4873fdbced39b', '2023-02-02 10:20:30'),
(10, 'Carlos', 'Sánchez', 35, '23456789-0', 555111222, 'e65e1eb5ff65d1e61780f1e110d6e870', '2023-03-03 08:45:15'),
(11, 'Laura', 'Díaz', 28, '34567890-1', 777888999, '5f4dcc3b5aa765d61d8327deb882cf99', '2023-04-04 14:15:30'),
(12, 'Pedro', 'Martínez', 40, '45678901-2', 111222333, 'b0baee9d279d34fa1dfd71aadb908c3f', '2023-05-05 16:30:45'),
(13, 'Ana', 'López', 22, '56789012-3', 999888777, '62f41ee5c5879a21ef35454e6415f56e', '2023-06-06 18:45:00'),
(14, 'Miguel', 'Rodríguez', 32, '67890123-4', 444555666, 'c1f2ac2b10aefbe5d8d4f049f0126e77', '2023-07-07 20:00:15'),
(15, 'Elena', 'Fernández', 27, '78901234-5', 666777888, 'e65e1eb5ff65d1e61780f1e110d6e870', '2023-08-08 22:15:30'),
(16, 'Diego', 'Hernández', 38, '89012345-6', 222333444, 'e0050424fcf1d548630c41db3204245b', '2023-09-09 00:30:45');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD UNIQUE KEY `identificador` (`identificador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cliente`
--
ALTER TABLE `cliente`
  MODIFY `identificador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
