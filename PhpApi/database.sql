CREATE TABLE `tbl_suspects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` text CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  `suspectid` int(11) NOT NULL,
  `msg` text CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  `rprtTimes` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `id_2` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=armscii8 COLLATE=armscii8_bin AUTO_INCREMENT=27 ;
