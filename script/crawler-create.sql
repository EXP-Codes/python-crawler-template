CREATE TABLE IF NOT EXISTS `t_crawler` (
  `i_id`       INTEGER PRIMARY KEY AUTOINCREMENT,
  `i_num`      INTEGER,
  `s_name`     TEXT(128),
  `s_url`      TEXT(512)
);