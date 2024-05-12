--
-- Table structure for table `tblproduct`
--

CREATE TABLE `tblproduct` (
  `id` int(8) NOT NULL,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `image` text NOT NULL,
  `price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblproduct`
--

INSERT INTO `tblproduct` (`id`, `name`, `code`, `image`, `price`) VALUES
(1, 'Canoooooo1 3000D Camera', 'Canooo1cAM3000D', 'product-images/camera.png', 1500),
(2, 'Enterprise Hard Disk Drive 100GB SAS', 'hdd100GBExSAS', 'product-images/disk.png', 800),
(3, 'Apooo Watch 12S b Series', 'watchQ12Sb', 'product-images/watch.png', 300),
(4, 'Do11 Laptop 24core/16GB', 'DoLT2416', 'product-images/laptop.png', 800),
(5, 'FLAG{Th3_secret_0f_wh3r3_5tatement_r32few}', 'FLAG', 'product-images/flag.png', 7777);

--
-- Indexes for table `tblproduct`
--
ALTER TABLE `tblproduct`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `product_code` (`code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tblproduct`
--
ALTER TABLE `tblproduct`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;