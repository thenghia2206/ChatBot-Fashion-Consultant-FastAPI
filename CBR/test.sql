
-- INSERT Áo khoác
-- Áo len
-- Áo Sơ mi
-- Áo gile
-- Áo phông
-- Áo pijama
-- Áo hoodie
-- Vest
-- Áo giữ nhiệt
-- Áo ba lỗ
-- Áo mangto
-- Áo phao
-- Quần âu
-- Quần kaki
-- Quần short
-- Quần boardshort
-- Quần đùi
-- Quần giữ nhiệt (legging)
-- Quần bò (Jean)
-- Quần jogger
-- Quần cargo
-- Quần pijama
-- Quần baggy
-- Quần thể thao
-- Chân Váy
-- "Váy
-- "
-- "Đầm
-- "
-- Áo Jean
-- Quần gió
-- Áo thun
-- Quần thun

CREATE TABLE `trithuc`.`quanao` (
  `id` INT NOT NULL,
  `ten` LONGTEXT NOT NULL,
  PRIMARY KEY (`id`));

INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('1', 'Áo kaki');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('2', 'Áo blazer');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('3', 'Áo khoác');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('4', 'Áo len');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('5', 'Áo Sơ mi');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('6', 'Áo gile');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('7', 'Áo phông');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('8', 'Áo pijama');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('9', 'Áo hoodie');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('10', 'Vest');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('11', 'Áo giữ nhiệt');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('12', 'Áo ba lỗ');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('13', 'Áo mangto');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('14', 'Áo phao');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('15', 'Quần âu');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('16', 'Quần kaki');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('17', 'Quần short');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('18', 'Quần boardshort');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('19', 'Quần đùi');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('20', 'Quần giữ nhiệt (legging)');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('21', 'Quần bò (Jean)');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('22', 'Quần jogger');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('23', 'Quần cargo');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('24', 'Quần pijama');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('25', 'Quần baggy');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('26', 'Quần thể thao');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('27', 'Chân Váy');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('28', 'Váy');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('29', 'Đầm');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('30', 'Áo Jean');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('31', 'Quần gió');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('32', 'Áo thun');
INSERT INTO `trithuc`.`quanao` (`id`, `ten`) VALUES ('33', 'Quần thun');


-- Cotton
-- Nhung
-- Lụa
-- Jean
-- Kaki
-- Lông cừu
-- Nỉ
-- Len
-- Da cá sấu
-- Lụa tơ tằm
-- Bông 
-- Gió
-- Thun
-- Lanh
-- Đũi
-- Dạ
-- Tuýt
-- Vải sợi che
-- Xô
-- Modal

CREATE TABLE `trithuc`.`vai` (
  `id` INT NOT NULL,
  `ten` LONGTEXT NULL,
  PRIMARY KEY (`id`));


INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('1', 'Cotton');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('2', 'Nhung');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('3', 'Lụa');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('4', 'Jean');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('5', 'Kaki');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('6', 'Lông cừu');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('7', 'Nỉ');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('8', 'Len');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('9', 'Da cá sấu');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('10', 'Lụa tơ tằm');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('11', 'Bông');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('12', 'Gió');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('13', 'Thun');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('14', 'Lanh');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('15', 'Đũi');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('16', 'Dạ');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('17', 'Tuýt');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('18', 'Vải sợi che');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('19', 'Xô');
INSERT INTO `trithuc`.`vai` (`id`, `ten`) VALUES ('20', 'Modal');



CREATE TABLE `vaiquanao` (
  `id` int NOT NULL,
  `idvai` int NOT NULL,
  `idquanao` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idvai_idx` (`idvai`),
  KEY `idquanao_idx` (`idquanao`),
  CONSTRAINT `idquanao` FOREIGN KEY (`idquanao`) REFERENCES `quanao` (`id`),
  CONSTRAINT `idvai` FOREIGN KEY (`idvai`) REFERENCES `vai` (`id`)
)

INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('1', '1', '15');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('2', '5', '16');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('3', '1', '18');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('4', '4', '21');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('5', '2', '22');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('6', '5', '1');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('7', '1', '7');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('8', '8', '4');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('9', '7', '22');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('10', '14', '2');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('11', '4', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('12', '1', '17');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('13', '8', '20');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('14', '3', '8');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('15', '3', '24');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('16', '4', '30');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('17', '4', '6');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('18', '3', '5');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('19', '5', '5');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('20', '15', '25');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('21', '1', '22');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('22', '15', '4');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('23', '12', '31');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('24', '7', '9');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('25', '16', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('26', '8', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('27', '7', '23');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('28', '1', '25');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('29', '13', '26');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('30', '1', '5');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('31', '1', '10');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('32', '12', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('33', '1', '26');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('34', '1', '12');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('35', '5', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('36', '5', '25');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('37', '5', '15');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('38', '7', '20');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('39', '1', '2');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('40', '13', '11');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('41', '7', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('42', '16', '13');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('43', '9', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('44', '6', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('45', '17', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('46', '13', '20');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('47', '8', '22');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('48', '1', '27');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('49', '3', '27');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('50', '13', '33');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('51', '1', '29');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('52', '3', '29');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('53', '13', '17');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('54', '13', '32');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('55', '13', '27');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('56', '11', '24');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('57', '11', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('58', '1', '3');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('59', '11', '22');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('60', '11', '4');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('61', '14', '5');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('62', '4', '28');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('63', '14', '27');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('64', '1', '33');
INSERT INTO `trithuc`.`vaiquanao` (`id`, `idvai`, `idquanao`) VALUES ('65', '3', '28');




CREATE TABLE `trithuc`.`sanpham` (
  `id` INT NOT NULL,
  `idvaiquanao` INT NOT NULL,
  `tensanpham` LONGTEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `idvaiquanao_idx` (`idvaiquanao` ASC) VISIBLE,
  CONSTRAINT `idvaiquanao`
    FOREIGN KEY (`idvaiquanao`)
    REFERENCES `trithuc`.`vaiquanao` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('1', '1', 'quần âu cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('2', '2', 'quần kaki');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('3', '3', 'quần boardshort');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('4', '4', 'quần jean rách');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('5', '5', 'quần nhung tăm');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('6', '6', 'áo kaki khoác ngoài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('7', '7', 'áo phông thoải mái và năng động');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('8', '6', 'áo kaki màu xanh đậm');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('9', '8', 'áo len nam cổ lọ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('10', '8', 'áo len nam gile');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('11', '9', 'quần jogger nỉ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('12', '1', 'quần tây cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('13', '4', 'quần jean dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('14', '10', 'áo blazer thu hút');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('15', '11', 'áo khoác jean nam màu xanh nhạt');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('16', '8', 'áo len nam cardigan');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('17', '6', 'quần short kaki');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('18', '12', 'quần short vải');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('19', '4', 'quần jean xước');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('20', '13', 'quần len mỏng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('21', '6', 'áo khoác ngoài kaki phối layer');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('22', '7', 'áo polo cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('23', '11', 'áo khoác jean nam hàn quốc');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('24', '8', 'áo len gile');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('25', '12', 'quần ngủ cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('26', '14', 'áo ngủ lụa');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('27', '7', 'áo ngủ cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('28', '8', 'áo len mòng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('29', '12', 'quần short');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('30', '15', 'quần lụa ống xuông');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('31', '6', 'áo khoác kaki');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('32', '16', 'áo jean');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('33', '17', 'áo gile jean mỏng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('34', '18', 'áo sơ mi lụa');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('35', '6', 'quần kaki jogger');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('36', '4', 'quần jean');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('37', '10', 'áo blazer');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('38', '19', 'áo sơ mi kaki');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('39', '7', 'áo phông');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('40', '16', 'áo jean co giãn');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('41', '20', 'quần đũi');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('42', '21', 'quần chinos ống suông');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('43', '4', 'quần jean co giãn');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('44', '15', 'quần pijama');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('45', '22', 'áo vải đũi');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('46', '14', 'áo pijama');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('47', '8', 'ao len nam cardigan');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('48', '12', 'quần cotton đi ngủ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('49', '2', 'quần kaki nam ống đứng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('50', '23', 'quần gió');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('51', '24', 'áo hoodie');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('52', '8', 'áo len cổ lọ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('53', '25', 'áo dạ khoác dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('54', '26', 'áo khoác gió nam mix với áo len');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('55', '16', 'áo khoác jean');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('56', '8', 'áo cardigan');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('57', '4', 'quần short jean');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('58', '27', 'quần nỉ nam');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('59', '24', 'áo hoodie nam');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('60', '28', 'quần daily pants');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('61', '28', 'quần dài cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('62', '12', 'quần short cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('63', '1', 'quần âu');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('64', '29', 'quần dài thể thao');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('65', '30', 'áo sơ mi');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('66', '31', 'áo vest');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('67', '32', 'áo khoác mỏng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('68', '16', 'áo khoắc jean mỏng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('69', '33', 'quần short thể thao');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('70', '33', 'quần thể thao');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('71', '33', 'quần đùi thể thao');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('72', '34', 'áo ba lỗ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('73', '7', 'áo polo');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('74', '30', 'áo sơ mi dài tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('75', '30', 'áo sơ mi ngắn tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('76', '35', 'áo khoác mỏng kaki');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('77', '11', 'áo khoác jean mỏng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('78', '28', 'quần cotton dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('79', '36', 'quần âu kaki');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('80', '19', 'áo sơ mi kaki ngắn tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('81', '7', 'áo thể thao ngắn tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('82', '6', 'áo kaki ngắn tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('83', '18', 'áo sơ mi lụa dài tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('84', '18', 'áo sơ mi lụa ngắn tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('85', '8', 'áo len mỏng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('86', '37', 'quần âu vải kaki');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('87', '2', 'quần kaki dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('88', '38', 'quần nỉ dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('89', '32', 'áo khoác');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('90', '39', 'áo cotton dài tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('91', '8', 'áo len dài tay dày');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('92', '8', 'áo len dài tay mỏng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('93', '40', 'áo giữ nhiệt');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('94', '41', 'áo khoác nỉ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('95', '42', 'áo dạ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('96', '16', 'áo jean dài tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('97', '43', 'áo khoác da');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('98', '44', 'áo khoác lông');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('99', '45', 'áo khoác tuýt dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('100', '46', 'quần giữ nhiệt');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('101', '13', 'quần len dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('102', '47', 'quần ổng lửng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('103', '7', 'áo phông cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('104', '48', 'chân váy dài cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('105', '48', 'chân váy bút chì');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('106', '49', 'chân váy dài lụa.');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('107', '21', 'quần cotton dài co giãn');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('108', '12', 'quần lửng cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('109', '50', 'quần thun dài co giãn');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('110', '50', 'quần thun lửng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('111', '14', 'áo lụa dài tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('112', '18', 'áo lụa ngắn tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('113', '51', 'đầm cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('114', '52', 'đầm lụa');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('115', '2', 'quần kaki dai');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('116', '4', 'quần jean dài ống loe');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('117', '51', 'đầm cotton trơn');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('118', '52', 'đầm lụa trơn');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('119', '12', 'quần short co giãn');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('120', '50', 'quần thun dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('121', '53', 'quần short thun');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('122', '7', 'áo phông thể thao');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('123', '54', 'áo thun thể thao');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('124', '48', 'váy thể thao cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('125', '55', 'váy thun thể thao');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('126', '15', 'quần dài vải lụa');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('127', '18', 'áo ngắn tay vải lụa');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('128', '4', 'quần jean đùi');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('129', '12', 'quần cotton short');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('130', '16', 'áo jean 3 lỗ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('131', '15', 'quần vải lụa dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('132', '34', '3 lỗ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('133', '15', 'quần lụa dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('134', '56', 'quần dài vải bông');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('135', '57', 'áo khoác bông');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('136', '8', 'áo len');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('137', '58', 'áo khoác cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('138', '59', 'quần bông dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('139', '60', 'áo bông dài tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('140', '14', 'áo vải lụa ngắn tay');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('141', '42', 'áo choàng dạ');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('142', '61', 'áo sơ mi vải lanh');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('143', '28', 'quần tây baggy');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('144', '50', 'quẩn thun vải lanh');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('145', '48', 'váy cotton dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('146', '62', 'váy jean đuôi cá');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('147', '63', 'váy vải lanh');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('148', '64', 'quần thun cotton');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('149', '65', 'váy lụa dài');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('150', '15', 'quần lụa ống rộng');
INSERT INTO `trithuc`.`sanpham` (`id`, `idvaiquanao`, `tensanpham`) VALUES ('151', '63', 'váy lanh dài');
