create database lagou charset utf8;
use lagou;

CREATE TABLE `companies` (
    `cid` INT(10) UNSIGNED NOT NULL PRIMARY KEY COMMENT '公司id',
    `logo` VARCHAR(128) COMMENT 'logo',
    `industry` VARCHAR(32) COMMENT '行业领域',
    `scale` VARCHAR(16) COMMENT '公司规模',
    `finance_stage` VARCHAR(32) COMMENT '融资阶段'
)  ENGINE=INNODB DEFAULT CHARSET=UTF8 COMMENT '公司信息表';


CREATE TABLE `positions` (
    `pid` INT(10) UNSIGNED NOT NULL PRIMARY KEY COMMENT '职位id',
    `cid` INT(10) UNSIGNED NOT NULL COMMENT '公司id',
    `name` VARCHAR(32) COMMENT '职位名称',
    `salary` VARCHAR(16) COMMENT '薪资',
    `city` VARCHAR(16) COMMENT '城市',
    `publish_time` VARCHAR(16) COMMENT '发布时间',
    `c_name` VARCHAR(16) COMMENT '公司名称',
    `c_full_name` VARCHAR(32) COMMENT '公司全称',
    `crawl_time` DATETIME COMMENT '爬取时间'
)  ENGINE=INNODB DEFAULT CHARSET=UTF8 COMMENT '职位信息表';


CREATE TABLE `details` (
    `pid` INT(10) UNSIGNED NOT NULL PRIMARY KEY COMMENT '职位id',
    `workyear` VARCHAR(16) COMMENT '工作经验',
    `education` VARCHAR(16) COMMENT '学历',
    `jobnature` VARCHAR(16) COMMENT '工作时间',
    `temptation` TEXT COMMENT '职位诱惑',
    `description` TEXT COMMENT '职位描述',
    `crawl_time` DATETIME COMMENT '爬取时间'
)  ENGINE=INNODB DEFAULT CHARSET=UTF8 COMMENT '职位信息表';