create database lagou0508 charset utf8;
use lagou0508;


CREATE TABLE `companies` (
  `cid` int(10) unsigned NOT NULL COMMENT '公司id',
  `name` varchar(16) DEFAULT NULL COMMENT '公司名称',
  `full_name` varchar(32) DEFAULT NULL COMMENT '公司全称',
  `city` varchar(16) DEFAULT NULL COMMENT '城市',
  `logo` varchar(128) DEFAULT NULL COMMENT 'logo',
  `industry` varchar(32) DEFAULT NULL COMMENT '行业领域',
  `finance_stage` varchar(32) DEFAULT NULL COMMENT '融资阶段',
  `scale` varchar(16) DEFAULT NULL COMMENT '公司规模',
  `crawl_time` datetime DEFAULT NULL COMMENT '爬取时间',
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司信息表';


CREATE TABLE `positions` (
  `pid` int(10) unsigned NOT NULL COMMENT '职位id',
  `cid` int(10) unsigned NOT NULL COMMENT '公司id',
  `name` varchar(32) DEFAULT NULL COMMENT '职位名称',
  `city` varchar(16) DEFAULT NULL COMMENT '城市',
  `salary` varchar(16) DEFAULT NULL COMMENT '薪资',
  `workyear` varchar(16) DEFAULT NULL COMMENT '工作经验',
  `education` varchar(16) DEFAULT NULL COMMENT '学历',
  `jobnature` varchar(16) DEFAULT NULL COMMENT '工作时间',
  `temptation` text COMMENT '职位诱惑',
  `description` text COMMENT '职位描述',
  `publish_time` varchar(16) DEFAULT NULL COMMENT '发布时间',
  `crawl_time` datetime DEFAULT NULL COMMENT '爬取时间',
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='职位信息表';

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL COMMENT '用户id',
  `name` varchar(16) NOT NULL COMMENT '用户名',
  `password` varchar(16) DEFAULT NULL COMMENT '密码',
  `email` varchar(32) DEFAULT NULL COMMENT '邮箱',
  `activate` boolean DEFAULT 0 COMMENT '激活状态',
  `pids` text COMMENT '收藏职位id',
  `keywords` text COMMENT '技能关键词',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表';

CREATE TABLE `feedback` (
  `fid` int(10) unsigned NOT NULL COMMENT '反馈id',
  `uid` int(10) unsigned NOT NULL COMMENT '用户id',
  `pid` int(10) unsigned NOT NULL COMMENT '失效职位id',
  `deal` boolean DEFAULT 0 COMMENT '处理状态',
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='反馈表';