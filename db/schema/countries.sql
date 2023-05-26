CREATE TABLE IF NOT EXISTS `countries` (
  `id`        	   INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `country`	         VARCHAR(50) DEFAULT NULL,
  CONSTRAINT unique_countries UNIQUE (country)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

