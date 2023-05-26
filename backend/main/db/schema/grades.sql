CREATE TABLE IF NOT EXISTS `grades` (
  `id`        	   INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `scale`          VARCHAR(20) NOT NULL,
  `grade`		   VARCHAR(20) NOT NULL,
  `numeric_grade`  SMALLINT NOT NULL,
  `description`    VARCHAR(256),
  CONSTRAINT unique_scale_grade UNIQUE (scale, grade, numeric_grade)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;