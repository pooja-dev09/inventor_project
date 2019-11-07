-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 07, 2019 at 02:01 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.2.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `exchange`
--

-- --------------------------------------------------------

--
-- Table structure for table `addattributes`
--

CREATE TABLE `addattributes` (
  `id` int(11) NOT NULL,
  `AttributeName` varchar(50) NOT NULL,
  `Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addattributes`
--

INSERT INTO `addattributes` (`id`, `AttributeName`, `Status`) VALUES
(1, 'rtew', 'Inactive');

-- --------------------------------------------------------

--
-- Table structure for table `addbrand`
--

CREATE TABLE `addbrand` (
  `id` int(11) NOT NULL,
  `BrandName` varchar(20) NOT NULL,
  `Status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addbrand`
--

INSERT INTO `addbrand` (`id`, `BrandName`, `Status`) VALUES
(2, 'ABCe', 'Active'),
(3, 'ABC', 'Active'),
(4, 'BCD', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `addcategory`
--

CREATE TABLE `addcategory` (
  `id` int(11) NOT NULL,
  `CategoryName` varchar(20) NOT NULL,
  `Status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addcategory`
--

INSERT INTO `addcategory` (`id`, `CategoryName`, `Status`) VALUES
(1, 'Microsoft', 'Active'),
(2, 'Nokia', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `addcompany`
--

CREATE TABLE `addcompany` (
  `id` int(11) NOT NULL,
  `CompanyName` varchar(20) NOT NULL,
  `ChargeAmount` varchar(20) NOT NULL,
  `VatCharge` varchar(20) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `Country` varchar(15) NOT NULL,
  `Message` varchar(30) NOT NULL,
  `Currency` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addcompany`
--

INSERT INTO `addcompany` (`id`, `CompanyName`, `ChargeAmount`, `VatCharge`, `Address`, `phone`, `Country`, `Message`, `Currency`) VALUES
(2, 'kytics', '13', '10', 'Behind tanshiq room', '9937625302', 'India', 'weldone', 'INR');

-- --------------------------------------------------------

--
-- Table structure for table `addorder`
--

CREATE TABLE `addorder` (
  `id` int(50) NOT NULL,
  `CustomerName` varchar(50) NOT NULL,
  `CustomerAddress` varchar(100) NOT NULL,
  `CustomerPhone` varchar(10) NOT NULL,
  `Product` varchar(50) NOT NULL,
  `Qty` varchar(50) NOT NULL,
  `Rate` varchar(50) NOT NULL,
  `Amount` varchar(50) NOT NULL,
  `GrossAmount` varchar(50) NOT NULL,
  `SCharge` varchar(50) NOT NULL,
  `Vat` varchar(50) NOT NULL,
  `Discount` varchar(50) NOT NULL,
  `NetAmount` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addorder`
--

INSERT INTO `addorder` (`id`, `CustomerName`, `CustomerAddress`, `CustomerPhone`, `Product`, `Qty`, `Rate`, `Amount`, `GrossAmount`, `SCharge`, `Vat`, `Discount`, `NetAmount`) VALUES
(3, 'pooja 32', '17', '9853924520', 'sacdcc', 'ddddwdedq', 'dd', 'dddwd', 'fqfdwfeefw', 'asfcaff', 'fcewffewf', 'vgergrgegrg', 'ewfwfewrfefvvg'),
(4, 'pooja 32', '17', '9853924520', 'sacdcc', 'ddddwdedq', 'dd', 'dddwd', 'fqfdwfeefw', 'asfcaff', 'fcewffewf', 'vgergrgegrg', 'ewfwfewrfefvvg'),
(5, 'pooja 121214545478 kumari', 'sasane nagar', '0985392452', '2', 'wwww', 'ddd', 'd', 'dfvdf', 'dfff', 'ddcsdsd', 'scscd', 'sfdfdf');

-- --------------------------------------------------------

--
-- Table structure for table `addproduct`
--

CREATE TABLE `addproduct` (
  `id` int(50) NOT NULL,
  `ProductName` varchar(50) NOT NULL,
  `File` varchar(50) NOT NULL,
  `Sku` varchar(50) NOT NULL,
  `Price` varchar(50) NOT NULL,
  `Qty` varchar(50) NOT NULL,
  `Description` varchar(50) NOT NULL,
  `Brands` varchar(50) NOT NULL,
  `Category` varchar(50) NOT NULL,
  `Store` varchar(50) NOT NULL,
  `Availability` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addproduct`
--

INSERT INTO `addproduct` (`id`, `ProductName`, `File`, `Sku`, `Price`, `Qty`, `Description`, `Brands`, `Category`, `Store`, `Availability`) VALUES
(19, 'lenovo', '66.jpeg', 'qasww', '50000', '7', 'rttttyy			', 'ttt', 'tttttrfefrvvgf', 'tgstrthbrtgrhth', 'srtsrhsrthrshsrh'),
(20, 'shop', 'swati_1.jpeg', 'kepper', '20000', '8', 'hokpkpk			', 'hkjnknkn', 'knkknk', 'nkjnkn', 'nknlk');

-- --------------------------------------------------------

--
-- Table structure for table `addstore`
--

CREATE TABLE `addstore` (
  `id` int(11) NOT NULL,
  `StoreName` varchar(50) NOT NULL,
  `Status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addstore`
--

INSERT INTO `addstore` (`id`, `StoreName`, `Status`) VALUES
(1, 'tanshiq', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `adduser`
--

CREATE TABLE `adduser` (
  `id` int(11) NOT NULL,
  `grouping` varchar(20) NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `FirstName` varchar(20) NOT NULL,
  `LastName` varchar(20) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Gender` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adduser`
--

INSERT INTO `adduser` (`id`, `grouping`, `Username`, `Email`, `Password`, `FirstName`, `LastName`, `Phone`, `Gender`) VALUES
(3, 'Select Group', 'janvi1232', 'janvi12@gmail.com', '0987654321', 'janvi', 'kumari', '8525417845', 'female'),
(4, 'Groupi', 'cicokc', 'poojadas721@gmail.com', '12345678', 'pooja', 'kumari', '8525417845', 'female'),
(5, '', 'suman', 'abc@gmail.com', '12345678', 'suman', 'kumari', '9853924520', 'F'),
(6, '', 'pooja123', 'cricgurugrd@gmail.com', '123456789', 'janvi', 'singh', '9853924520', 'F');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `Username`, `email`, `password`) VALUES
(1, 'pooja', 'poojadas721@gmail.com', '12345678');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addattributes`
--
ALTER TABLE `addattributes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addbrand`
--
ALTER TABLE `addbrand`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addcategory`
--
ALTER TABLE `addcategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addcompany`
--
ALTER TABLE `addcompany`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addorder`
--
ALTER TABLE `addorder`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addproduct`
--
ALTER TABLE `addproduct`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addstore`
--
ALTER TABLE `addstore`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adduser`
--
ALTER TABLE `adduser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addattributes`
--
ALTER TABLE `addattributes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `addbrand`
--
ALTER TABLE `addbrand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `addcategory`
--
ALTER TABLE `addcategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `addcompany`
--
ALTER TABLE `addcompany`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `addorder`
--
ALTER TABLE `addorder`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `addproduct`
--
ALTER TABLE `addproduct`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `addstore`
--
ALTER TABLE `addstore`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `adduser`
--
ALTER TABLE `adduser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
