-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost
-- Thời gian đã tạo: Th3 25, 2021 lúc 06:10 PM
-- Phiên bản máy phục vụ: 10.4.14-MariaDB
-- Phiên bản PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlsvlab`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `ghichu`
--

CREATE TABLE `ghichu` (
  `noidung` varchar(1000) NOT NULL,
  `deadline` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hoatdong`
--

CREATE TABLE `hoatdong` (
  `id` varchar(20) NOT NULL,
  `hoten` varchar(50) NOT NULL,
  `mssv` varchar(20) NOT NULL,
  `nhom` varchar(20) NOT NULL,
  `time` varchar(50) NOT NULL,
  `solan` varchar(10) NOT NULL,
  `timeoff` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `hoatdong`
--

INSERT INTO `hoatdong` (`id`, `hoten`, `mssv`, `nhom`, `time`, `solan`, `timeoff`) VALUES
(' B9 48 18 C1\r\n', 'yeye', 'aass', 'ss', '2021-02-24 23:59:54', '5', ''),
(' B9 48 18 C1\r\n', 'yeye', 'aass', 'ss', '2021-02-25 00:00:06', '1', ''),
(' B9 48 18 C1\r\n', 'yeye', 'aass', 'ss', '2021-02-25 00:46:17', '54', ''),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-02-25 00:46:22', '2', '2021-02-28 22:27:25'),
(' B9 48 18 C1\r\n', 'yeye', 'aass', 'ss', '2021-02-25 00:46:23', '55', ''),
(' B9 48 18 C1\r\n', 'yeye', 'aass', 'ss', '2021-02-25 01:00:26', '4', ''),
(' B9 48 18 C1\r\n', 'meongao', 'sss', 'ww', '2021-02-26 23:10:57', '6', '2021-02-27 00:10:57'),
(' B9 48 18 C1\r\n', 'meongao', 'sss', 'ww', '2021-02-26 23:32:11', '7', '2021-02-27 00:32:11'),
(' B9 48 18 C1\r\n', 'meongao', 'sss', 'ww', '2021-02-26 23:55:21', '8', '2021-02-27 00:55:21'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-02-27 15:47:37', '1', '2021-02-28 22:27:25'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-02-27 15:53:48', '2', '2021-02-28 22:27:25'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-05 17:58:47', '6', '2021-03-05 17:58:51'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-05 23:47:48', '6', '2021-03-05 23:48:08'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-05 23:48:28', '7', '2021-03-05 23:48:48'),
(' B9 48 18 C1\r\n', 'hehe', 'dd', 'ss', '2021-03-05 23:50:01', '5', '2021-03-05 23:50:13'),
(' 99 32 28 B9\r\n', 'ww', 'dd', 'sss', '2021-03-05 23:50:13', '1', '2021-03-05 23:50:33'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-06 17:12:40', '5', '2021-03-06 17:13:00'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-06 17:15:56', '3', '2021-03-06 17:16:16'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-06 17:16:06', '4', '2021-03-06 17:16:26'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-06 17:35:37', '2', '2021-03-06 17:35:57'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-06 17:35:40', '3', '2021-03-06 17:36:00'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-06 23:58:41', '3', '2021-03-06 23:59:01'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-06 23:58:48', '4', '2021-03-06 23:59:08'),
(' 99 32 28 B9\r\n', 'meongao', 'dd', 'sss', '2021-03-06 23:58:52', '1', '2021-03-06 23:59:12'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-07 00:00:18', '1', '2021-03-07 00:00:38'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-07 00:00:23', '1', '2021-03-07 00:00:43'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', '12331', '2021-03-07 00:32:34', '1', '2021-03-07 00:32:54'),
(' A9 89 51 B2\r\n', 'Rukawa', '1811119', 'ww', '2021-03-07 00:32:36', '1', '2021-03-07 00:32:56'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-07 00:32:40', '2', '2021-03-07 00:33:00'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-07 00:32:42', '2', '2021-03-07 00:33:02'),
(' A9 89 51 B2\r\n', 'Rukawa', '1811119', 'ww', '2021-03-07 00:47:38', '2', '2021-03-07 00:47:58'),
(' A9 89 51 B2\r\n', 'Rukawa', '1811119', 'ww', '2021-03-07 00:48:54', '3', '2021-03-07 00:49:54'),
(' A9 89 51 B2\r\n', 'Rukawa', '1811119', 'ww', '2021-03-07 01:08:49', '4', '2021-03-07 01:09:13'),
(' A9 89 51 B2\r\n', 'Rukawa', '1811119', 'ww', '2021-03-07 01:29:09', '5', '2021-03-07 01:29:34'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', '12331', '2021-03-08 23:55:39', '1', '2021-03-08 23:55:54'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-08 23:56:18', '1', '2021-03-08 23:56:33'),
(' A9 89 51 B2\r\n', 'Rukawa', '1811119', 'ww', '2021-03-08 23:56:20', '1', '2021-03-08 23:56:35'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', '12331', '2021-03-08 23:56:23', '2', '2021-03-08 23:56:38'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-08 23:56:25', '1', '2021-03-08 23:56:40'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-09 01:17:42', '1', '2021-03-09 01:17:57'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', '12331', '2021-03-09 01:17:47', '1', '2021-03-09 01:18:02'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', '12331', '2021-03-10 00:14:00', '1', '2021-03-10 00:14:15'),
(' B9 48 18 C1\r\n', 'Khong Ten', 'ddss', 'ss', '2021-03-10 11:15:12', '3', '2021-03-10 11:15:27'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'sas', '2021-03-10 11:15:17', '1', '2021-03-10 11:15:31'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', '12331', '2021-03-11 16:03:55', '1', '2021-03-11 16:04:10'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', '12331', '2021-03-11 16:04:22', '2', '2021-03-11 16:04:37'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', '123456789', '2021-03-11 17:11:42', '1', '2021-03-11 17:11:57'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'DD', '2021-03-11 17:13:10', '2', '2021-03-11 17:13:25'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', 'vn_aaa', '2021-03-11 23:33:32', '3', '2021-03-11 23:33:37'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', 'vn_aaa', '2021-03-11 23:38:39', '4', '2021-03-11 23:38:49'),
(' B9 48 18 C1\r\n', 'kokomi', '09089364', 'qqqa', '2021-03-11 23:50:17', '1', '2021-03-11 23:50:27'),
(' B9 48 18 C1\r\n', 'kokomi', '09089364', 'qqqa', '2021-03-11 23:50:31', '2', '2021-03-11 23:50:41'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'Dragonball', '2021-03-11 23:51:07', '1', '2021-03-11 23:51:17'),
(' 69 4D FE B3\r\n', 'Huynh Le Vu Dat', '1811855', 'DD', '2021-03-12 08:21:34', '1', '2021-03-12 08:21:44'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', 'vn_aaa', '2021-03-12 08:21:41', '1', '2021-03-12 08:21:51'),
(' B9 48 18 C1\r\n', 'The Khai', '18111111', 'D5', '2021-03-12 22:08:19', '1', '2021-03-12 22:08:29'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'D5', '2021-03-12 22:14:19', '1', '2021-03-12 22:14:29'),
(' B9 48 18 C1\r\n', 'The Khai', '18111111', 'D5', '2021-03-12 22:14:22', '2', '2021-03-12 22:14:32'),
(' B9 48 18 C1\r\n', 'The Khai', '18111111', 'D5', '2021-03-12 22:43:11', '6', '2021-03-12 22:43:21'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', 'D5', '2021-03-12 23:23:36', '2', '2021-03-12 23:23:46'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'D5', '2021-03-12 23:23:39', '2', '2021-03-12 23:23:49'),
(' 69 4D FE B3\r\n', 'Dat dep trai', '1811855', 'D5', '2021-03-12 23:23:42', '2', '2021-03-12 23:23:52'),
(' B9 48 18 C1\r\n', 'The Khai', '18111111', 'D5', '2021-03-12 23:23:45', '4', '2021-03-12 23:23:55'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'D5', '2021-03-12 23:23:54', '3', '2021-03-12 23:24:04'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', 'D5', '2021-03-12 23:23:56', '3', '2021-03-12 23:24:06'),
(' 99 32 28 B9\r\n', 'Hang Cho', '15999', 'bts', '2021-03-12 23:24:03', '1', '2021-03-12 23:24:13'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', 'D5', '2021-03-12 23:55:02', '4', '2021-03-12 23:55:12'),
(' 99 3C 61 B2\r\n', 'Misuik', 'aasss', 'D5', '2021-03-12 23:56:19', '5', '2021-03-12 23:56:29'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'D5', '2021-03-12 23:56:37', '4', '2021-03-12 23:56:47'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'D5', '2021-03-12 23:57:51', '5', '2021-03-12 23:58:01'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'D5', '2021-03-12 23:58:24', '6', '2021-03-12 23:58:34'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'vuivui', '2021-03-13 11:02:27', '7', '2021-03-13 11:02:47'),
(' B9 48 18 C1\r\n', 'The Khai', '18111111', 'D5', '2021-03-13 12:38:02', '4', '2021-03-13 12:38:22'),
(' 99 32 28 B9\r\n', 'Hang Cho', '15975546', 'bts ', '2021-03-13 12:39:52', '1', '2021-03-13 12:40:04'),
(' 99 32 28 B9\r\n', 'Hang Cho', '15975546', 'bts ', '2021-03-13 12:40:53', '3', '2021-03-13 12:41:13'),
(' 99 32 28 B9\r\n', 'Hang Cho', '15975546965', 'bts ', '2021-03-13 16:26:41', '3', '2021-03-13 16:27:01'),
(' B9 48 18 C1\r\n', 'Chan ho', '43f34443', '23312', '2021-03-13 16:28:33', '6', '2021-03-13 16:28:53'),
(' 99 3C 61 B2\r\n', 'Rukawa', '1278952', 'shoduku', '2021-03-13 16:28:37', '3', '2021-03-13 16:28:57'),
(' 99 3C 61 B2\r\n', 'Rukawa', '1278952', 'shoduku', '2021-03-15 01:34:59', '1', '2021-03-15 01:35:06'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'vuivui', '2021-03-15 10:54:25', '5', '2021-03-15 10:54:31'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-15 12:03:32', '1', '2021-03-15 12:03:47'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'vuivui', '2021-03-15 12:03:34', '2', '2021-03-15 12:03:43'),
(' 99 3C 61 B2\r\n', 'Rukawa', '1278952', 'shoduku', '2021-03-15 12:03:39', '2', '2021-03-15 12:03:54'),
(' 99 3C 61 B2\r\n', 'Rukawa', '1278952', 'shoduku', '2021-03-16 02:03:25', '1', '2021-03-16 02:03:27'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-17 10:05:50', '1', '2021-03-17 10:06:10'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-17 23:40:07', '1', '2021-03-17 23:40:47'),
(' 99 3C 61 B2\r\n', 'rukawa', '22211mm', 'wee', '2021-03-17 23:40:10', '1', '2021-03-17 23:40:50'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-17 23:56:12', '2', '2021-03-17 23:56:52'),
(' B9 48 18 C1\r\n', 'dat2', '21ssee', 'dd', '2021-03-18 01:03:01', '6', '2021-03-18 01:03:21'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-18 01:55:22', '1', '2021-03-18 01:55:42'),
(' B9 48 18 C1\r\n', 'dat2', '21ssee', 'dd', '2021-03-18 02:18:43', '2', '2021-03-18 02:19:03'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-18 23:59:12', '1', '2021-03-18 23:59:32'),
(' B9 48 18 C1\r\n', 'dat2', '21ssee', 'dd', '2021-03-18 23:59:17', '3', '2021-03-18 23:59:37'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-18 23:59:23', '2', '2021-03-18 23:59:43'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-18 23:59:45', '3', '2021-03-19 00:00:05'),
(' B9 48 18 C1\r\n', 'dat2', '21ssee', 'dd', '2021-03-18 23:59:50', '4', '2021-03-19 00:00:10'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-18 23:59:55', '2', '2021-03-19 00:00:15'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-19 14:14:24', '11', '2021-03-19 14:14:44'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-19 14:36:21', '2', '2021-03-19 14:36:41'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-19 14:42:41', '3', '2021-03-19 14:43:01'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-19 14:43:15', '4', '2021-03-19 14:43:35'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-19 21:48:57', '5', '2021-03-19 21:49:17'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-20 02:18:59', '1', '2021-03-20 02:19:19'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-20 02:19:31', '2', '2021-03-20 02:19:51'),
(' B9 48 18 C1\r\n', 'dat2', '21ssee', 'dd', '2021-03-20 12:49:35', '1', '2021-03-20 12:49:55'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-20 12:49:47', '3', '2021-03-20 12:50:07'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-20 12:53:08', '4', '2021-03-20 12:53:28'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-20 13:00:37', '5', '2021-03-20 13:00:57'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-20 20:23:05', '6', '2021-03-20 20:23:25'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-20 20:28:18', '7', '2021-03-20 20:28:38'),
(' B9 48 18 C1\r\n', 'dat2', '21ssee', 'dd', '2021-03-21 00:59:26', '1', '2021-03-21 00:59:41'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-21 02:12:13', '1', '2021-03-21 02:12:33'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-21 12:28:39', '2', '2021-03-21 12:28:59'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-21 12:38:23', '2', '2021-03-21 12:38:27'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-21 13:45:03', '3', '2021-03-21 13:45:23'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-21 13:45:22', '2', '2021-03-21 13:45:42'),
(' 99 3C 61 B2\r\n', 'Linus Torvalds boss', 'maxx', 'Hacking', '2021-03-21 13:45:28', '1', '2021-03-21 13:45:48'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-21 14:05:06', '3', '2021-03-21 14:05:26'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-22 01:47:05', '1', '2021-03-22 01:47:25'),
(' 99 3C 61 B2\r\n', 'Linus Torvalds boss', 'maxx', 'Hacking', '2021-03-22 01:47:13', '1', '2021-03-22 01:47:33'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-22 17:47:38', '2', '2021-03-22 17:47:58'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-22 17:54:04', '3', '2021-03-22 17:54:24'),
(' 99 3C 61 B2\r\n', 'Linus Torvalds boss', 'maxx', 'Hacking', '2021-03-22 17:54:08', '2', '2021-03-22 17:54:28'),
(' B9 48 18 C1\r\n', 'wweq', '3213123', 'ew13', '2021-03-22 17:54:11', '1', '2021-03-22 17:54:31'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-22 17:54:29', '1', '2021-03-22 17:54:49'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-24 00:37:05', '1', '2021-03-24 00:37:25'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-24 22:49:42', '2', '2021-03-24 22:49:49'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-25 00:00:13', '1', '2021-03-25 00:00:26'),
(' B9 48 18 C1\r\n', 'Rukawa', '3213123', 'ew13', '2021-03-25 01:20:38', '1', '2021-03-25 01:20:54'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-25 01:20:51', '2', '2021-03-25 01:21:11'),
(' 99 3C 61 B2\r\n', 'Linus Torvalds boss', 'maxx', 'Hacking', '2021-03-25 01:20:56', '1', '2021-03-25 01:21:16'),
(' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', '2021-03-25 01:20:59', '1', '2021-03-25 01:21:19'),
(' 99 32 28 B9\r\n', 'Hang Cho', '15975546965', 'bts ', '2021-03-25 01:21:03', '1', '2021-03-25 01:21:23'),
(' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', '2021-03-25 01:21:42', '3', '2021-03-25 01:21:52');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hoatdongtemp`
--

CREATE TABLE `hoatdongtemp` (
  `id` varchar(50) NOT NULL,
  `hoten` varchar(50) NOT NULL,
  `time` varchar(50) NOT NULL,
  `mssv` varchar(100) NOT NULL,
  `addressimg` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `login`
--

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `mail` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `login`
--

INSERT INTO `login` (`username`, `password`, `mail`) VALUES
('1', '1', 'asda'),
('2', '2', 'dathuynh001@gmail.com'),
('3', '3', 'scientisttime159@gmail.com');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `luuanhhd`
--

CREATE TABLE `luuanhhd` (
  `image` varchar(10000) NOT NULL,
  `id` varchar(20) NOT NULL,
  `mssv` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `mailcontent`
--

CREATE TABLE `mailcontent` (
  `detai` varchar(50) NOT NULL,
  `chude` varchar(50) NOT NULL,
  `noidung` varchar(1000) NOT NULL,
  `date` varchar(50) NOT NULL,
  `tinhtrang` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `mailcontent`
--

INSERT INTO `mailcontent` (`detai`, `chude`, `noidung`, `date`, `tinhtrang`) VALUES
('bong ro', '100 do', 'nu nephu a ceyo, ne nisumi', '2021-03-19 00:01:05', 'Busy'),
('co tuong', '90 do', 'okla', '2021-03-19 00:01:11', 'Busy'),
('hohap', 'wq', 'qqwewqqwe2\n', '2021-03-20 12:42:39', 'Busy'),
('marathon', '16 do', 'suziki\n', '2021-03-20 13:48:52', 'Busy'),
('marathon', '14 doo', 'spider mannnn112', '2021-03-20 13:49:50', 'Busy'),
('marathon', '1000 do', 'Linuss bosss', '2021-03-20 14:01:25', 'Already'),
('hohap', 'draeger', 'savinar 300\n', '2021-03-20 14:02:41', 'Already'),
('Hackinggg', 'Sql_injection', 'rip fb\n', '2021-03-21 02:20:25', 'Already');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `mnlab`
--

CREATE TABLE `mnlab` (
  `stt` varchar(20) NOT NULL,
  `id` varchar(20) NOT NULL,
  `hoten` varchar(50) NOT NULL,
  `mssv` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `nhom` varchar(50) NOT NULL,
  `gioitinh` varchar(50) NOT NULL,
  `namsinh` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `sdt` varchar(20) NOT NULL,
  `date` varchar(50) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `tendetai` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `mnlab`
--

INSERT INTO `mnlab` (`stt`, `id`, `hoten`, `mssv`, `nhom`, `gioitinh`, `namsinh`, `email`, `sdt`, `date`, `image`, `tendetai`) VALUES
('10', ' 07 10 1F 4A\r\n', 'Anh Phu', '129088', 'bestxulianh', 'Nam', '1997', 'sficty1206@gmail.com', '123', '12/03/2021 13:26:42', '/media/vudat/New Volume/Laptrinh/Python/GUI/working/101387073_1133437943686037_5147233046227812538_n.jpg', 'bong ro'),
('10', ' 69 4D FE B3\r\n', 'Vu Dat', '146546', 'D444', 'Nam', '2000', 'scientisttime159@gmail.com', '1231', '13/03/2021 12:03:10', '/media/vudat/New Volume/Laptrinh/Python/GUI/anhhoitraii.jpg', 'marathon'),
('10', ' 99 32 28 B9\r\n', 'Hang Cho', '15975546965', 'bts ', 'Nu', '2000', 'dathuynh001fish@gmail.com\r\n', '123312', '13/03/2021 12:04:04', '/media/vudat/New Volume/Laptrinh/Python/GUI/working/Boapp/Hinh-Nen-Meo-Ngao-44.jpg', 'marathon'),
('8', ' 99 3C 61 B2\r\n', 'Linus Torvalds boss', 'maxx', 'Hacking', 'Nam', '2000', 'sficty1206@gmail.com', '9911', '21/03/2021 01:55:32', '/media/vudat/New Volume/Laptrinh/Python/GUI/working/Boapp/linus.jpg', 'Hackinggg'),
('6', ' A9 89 51 B2\r\n', 'Tang Tuyet Ngan', '123456', 'bestxulianh', 'Nu', '1999', 'scientisttime159@gmail.com', 'qq', '07/03/2021 00:02:38', '/media/vudat/New Volume/Laptrinh/Python/GUI/121416083_210680180481746_3150337036065360564_o.jpg', 'hohap'),
('9', ' B9 48 18 C1\r\n', 'Rukawa', '3213123', 'ew13', 'Nam', '1990', 'dathuynh001@gmail.com', '3231231', '21/03/2021 12:24:04', '', '');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `qltime`
--

CREATE TABLE `qltime` (
  `hour` varchar(10) NOT NULL,
  `minute` varchar(10) NOT NULL,
  `second` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `qltime`
--

INSERT INTO `qltime` (`hour`, `minute`, `second`) VALUES
('00', '00', '10');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `student`
--

CREATE TABLE `student` (
  `hoten1` varchar(1000) NOT NULL,
  `email` varchar(50) NOT NULL,
  `sdt` varchar(50) NOT NULL,
  `mssv` varchar(15) NOT NULL,
  `lop` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `student`
--

INSERT INTO `student` (`hoten1`, `email`, `sdt`, `mssv`, `lop`) VALUES
('das', '321321', '321', '312', '321312'),
('meo', 'dddd', '0123', '45612', 'ssdd'),
('meo', 'dddd', '0123', '45612', 'ssdd'),
('Dat', 'dathuynh001@gmail.com', '0908936451', '1811855', 'ku18vly1'),
('meo', 'meo@@', '05435', '12123', '1332'),
('[<PIL.ImageTk.PhotoImage object at 0x7f274eceac10>]', '', '', '', '');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `timenotehome`
--

CREATE TABLE `timenotehome` (
  `noidung` varchar(500) NOT NULL,
  `ngay` varchar(10) NOT NULL,
  `thang` varchar(10) NOT NULL,
  `nam` varchar(10) NOT NULL,
  `gio` varchar(10) NOT NULL,
  `phut` varchar(10) NOT NULL,
  `giay` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `timenotehome`
--

INSERT INTO `timenotehome` (`noidung`, `ngay`, `thang`, `nam`, `gio`, `phut`, `giay`) VALUES
('biennangluongdientro', '25', '3', '2021', '23', '59', '59'),
('biennangluongdientro2', '25', '3', '2021', '23', '59', '59'),
('chaobuoisang binh minh', '25', '3', '2021', '23', '59', '59'),
('truyennangluongrfid', '25', '3', '2021', '23', '59', '59'),
('chaobssmnoi', '25', '3', '2021', '23', '59', '59');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `hoatdong`
--
ALTER TABLE `hoatdong`
  ADD PRIMARY KEY (`time`);

--
-- Chỉ mục cho bảng `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`) USING BTREE;

--
-- Chỉ mục cho bảng `mailcontent`
--
ALTER TABLE `mailcontent`
  ADD PRIMARY KEY (`date`);

--
-- Chỉ mục cho bảng `mnlab`
--
ALTER TABLE `mnlab`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `qltime`
--
ALTER TABLE `qltime`
  ADD PRIMARY KEY (`second`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
