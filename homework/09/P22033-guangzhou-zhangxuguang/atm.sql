/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50726
Source Host           : localhost:3306
Source Database       : atm

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2019-08-28 00:33:27
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `log_moneys`
-- ----------------------------
DROP TABLE IF EXISTS `log_moneys`;
CREATE TABLE `log_moneys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(30) NOT NULL,
  `ctype` tinyint(2) DEFAULT NULL COMMENT '取出:1;存入:2;转账:3;',
  `change_amount` float(11,0) DEFAULT NULL,
  `creat_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `about` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `userid` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of log_moneys
-- ----------------------------
INSERT INTO `log_moneys` VALUES ('3', 'xuguang', '1', '-20', '2019-08-27 21:39:01', null);
INSERT INTO `log_moneys` VALUES ('4', 'xuguang', '2', '20', '2019-08-27 21:37:11', null);
INSERT INTO `log_moneys` VALUES ('5', 'xuguang', '3', '-30', '2019-08-27 22:03:45', null);
INSERT INTO `log_moneys` VALUES ('6', 'xuguang2', '3', '30', '2019-08-27 22:03:45', null);
INSERT INTO `log_moneys` VALUES ('9', 'xuguang2', '3', '-60', '2019-08-27 22:09:16', 'xuguang');
INSERT INTO `log_moneys` VALUES ('10', 'xuguang', '3', '60', '2019-08-27 22:09:16', 'xuguang2');
INSERT INTO `log_moneys` VALUES ('11', 'xuguang', '2', '10', '2019-08-27 23:07:32', null);
INSERT INTO `log_moneys` VALUES ('12', 'xuguang', '2', '10', '2019-08-27 23:40:47', null);
INSERT INTO `log_moneys` VALUES ('13', 'xuguang', '1', '-30', '2019-08-27 23:41:00', null);

-- ----------------------------
-- Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `userid` varchar(30) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `balance` float(11,0) DEFAULT '5000',
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('xuguang', '123456', '123456', '4980');
INSERT INTO `users` VALUES ('xuguang2', '123456', '1345020', '4970');
INSERT INTO `users` VALUES ('xuguang3', '123456', '121212', '5000');
