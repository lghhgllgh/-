/*
 Navicat MySQL Dump SQL

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 80040 (8.0.40)
 Source Host           : localhost:3306
 Source Schema         : school

 Target Server Type    : MySQL
 Target Server Version : 80040 (8.0.40)
 File Encoding         : 65001

 Date: 07/01/2025 01:08:09
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_login
-- ----------------------------
DROP TABLE IF EXISTS `admin_login`;
CREATE TABLE `admin_login`  (
  `admin_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `admin_pwd` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`admin_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin_login
-- ----------------------------
INSERT INTO `admin_login` VALUES ('admin01', '123456');
INSERT INTO `admin_login` VALUES ('admin02', '123456');

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college`  (
  `col_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `pre_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`col_name`) USING BTREE,
  INDEX `manged_by`(`pre_id` ASC) USING BTREE,
  CONSTRAINT `manged_by` FOREIGN KEY (`pre_id`) REFERENCES `teacher` (`tea_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of college
-- ----------------------------
INSERT INTO `college` VALUES ('船舶工程学院', '01');
INSERT INTO `college` VALUES ('计算机科学与技术学院', '06');
INSERT INTO `college` VALUES ('信息与通信工程学院', '08');

-- ----------------------------
-- Table structure for learn
-- ----------------------------
DROP TABLE IF EXISTS `learn`;
CREATE TABLE `learn`  (
  `stu_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `lesson_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `score` float(255, 0) NULL DEFAULT NULL,
  `class_number` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`, `lesson_id`) USING BTREE,
  INDEX `lesson`(`lesson_id` ASC) USING BTREE,
  CONSTRAINT `lesson` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`lesson_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `stu` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of learn
-- ----------------------------
INSERT INTO `learn` VALUES ('00001', '001', 96, 'C126');
INSERT INTO `learn` VALUES ('00001', '002', 92, '21B2012');
INSERT INTO `learn` VALUES ('00001', '003', 95, '21B3106');
INSERT INTO `learn` VALUES ('00001', '009', 91, '11#4082');
INSERT INTO `learn` VALUES ('00002', '004', 99, 'B420');
INSERT INTO `learn` VALUES ('00003', '005', 88, 'B402');
INSERT INTO `learn` VALUES ('00003', '009', 94, 'E201');
INSERT INTO `learn` VALUES ('00004', '006', 87, 'B502');
INSERT INTO `learn` VALUES ('00005', '007', 91, '体育馆');
INSERT INTO `learn` VALUES ('00006', '008', 98, 'B531');
INSERT INTO `learn` VALUES ('00006', '009', 90, '21B5086');
INSERT INTO `learn` VALUES ('00006', '012', 77, 'A34');

-- ----------------------------
-- Table structure for lesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson`;
CREATE TABLE `lesson`  (
  `lesson_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `lesson_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `credit` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `class_hour` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`lesson_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of lesson
-- ----------------------------
INSERT INTO `lesson` VALUES ('001', '数据库系统', '3', '17');
INSERT INTO `lesson` VALUES ('002', '计算机组成原理', '3', '17');
INSERT INTO `lesson` VALUES ('003', '计算思维', '2', '17');
INSERT INTO `lesson` VALUES ('004', '嵌入式系统', '3.5', '17');
INSERT INTO `lesson` VALUES ('005', '人工智能导论', '2', '17');
INSERT INTO `lesson` VALUES ('006', '算法导论', '3.5', '17');
INSERT INTO `lesson` VALUES ('007', '羽毛球', '2', '16');
INSERT INTO `lesson` VALUES ('008', '软件工程', '3', '17');
INSERT INTO `lesson` VALUES ('009', '高级英语', '2', '17');
INSERT INTO `lesson` VALUES ('010', '信息安全', '3', '17');
INSERT INTO `lesson` VALUES ('011', '毛概', '3', '17');
INSERT INTO `lesson` VALUES ('012', '音乐鉴赏', '1', '9');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stu_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_gender` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_adm_time` date NULL DEFAULT NULL,
  `stu_college` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  UNIQUE INDEX `id_index`(`stu_id` ASC) USING BTREE,
  INDEX `stu_in_col`(`stu_college` ASC) USING BTREE,
  INDEX `stu_name`(`stu_name` ASC) USING BTREE,
  INDEX `stu_adm_time`(`stu_adm_time` ASC) USING BTREE,
  CONSTRAINT `stu_in_col` FOREIGN KEY (`stu_college`) REFERENCES `college` (`col_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('00001', '张三', '男', '2020-09-11', '计算机科学与技术学院');
INSERT INTO `student` VALUES ('00002', '李四', '女', '2020-09-11', '船舶工程学院');
INSERT INTO `student` VALUES ('00003', '刘二', '男', '2021-09-12', '计算机科学与技术学院');
INSERT INTO `student` VALUES ('00004', '赵六', '女', '2021-09-12', '船舶工程学院');
INSERT INTO `student` VALUES ('00005', '王五', '男', '2021-09-12', '信息与通信工程学院');
INSERT INTO `student` VALUES ('00006', '小明', '男', '2019-09-10', '计算机科学与技术学院');

-- ----------------------------
-- Table structure for student_login
-- ----------------------------
DROP TABLE IF EXISTS `student_login`;
CREATE TABLE `student_login`  (
  `stu_id` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `stu_pwd` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  CONSTRAINT `stu_login` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of student_login
-- ----------------------------
INSERT INTO `student_login` VALUES ('00001', '123456');
INSERT INTO `student_login` VALUES ('00002', '123456');
INSERT INTO `student_login` VALUES ('00003', '123456');
INSERT INTO `student_login` VALUES ('00004', '123456');
INSERT INTO `student_login` VALUES ('00005', '123456');
INSERT INTO `student_login` VALUES ('00006', '123456');

-- ----------------------------
-- View structure for stu_les
-- ----------------------------
DROP VIEW IF EXISTS `stu_les`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `stu_les` AS select `student`.`stu_id` AS `stu_id`,`student`.`stu_name` AS `stu_name`,`learn`.`lesson_id` AS `lesson_id`,`learn`.`score` AS `score` from (`student` join `learn`) where (`student`.`stu_id` = `learn`.`stu_id`);

-- ----------------------------
-- Procedure structure for updata_tea1
-- ----------------------------
DROP PROCEDURE IF EXISTS `updata_tea1`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updata_tea1`(in n varchar(255), in t varchar(255), in s INT, in i varchar(20))
BEGIN
IF s < 5000 
THEN
    SIGNAL SQLSTATE '45000';
ELSE 
    UPDATE teacher SET tea_name = n, tea_title = t, tea_salary = s WHERE tea_id = i;
END IF;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updata_teach
-- ----------------------------
DROP PROCEDURE IF EXISTS `updata_teach`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `updata_teach`(in l varchar(20), in e varchar(255), in c varchar(255), in i varchar(20), in le varchar(20))
BEGIN
    UPDATE lesson SET lesson_id = l WHERE lesson_id = le;
    UPDATE teach SET end_way = e, class = c WHERE tea_id = i;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
