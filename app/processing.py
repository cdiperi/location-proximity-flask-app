from flask_sqlalchemy import SQLAlchemy
from app import app
from sqlalchemy.inspection import inspect
import json
import decimal

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD!",
    hostname="YOUR_HOSTNAME",
    databasename="YOUR_DATABASE",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class Location(db.Model, Serializer):

    __tablename__ = "LOCATIONS"
    rid = db.Column(db.Integer, primary_key=True)
    Location1 = db.Column(db.String(80))
    Latitude1 = db.Column(db.String(80))
    Longitude1 = db.Column(db.String(80))
    Location2 = db.Column(db.String(80))
    Latitude2 = db.Column(db.String(80))
    Longitude2 = db.Column(db.String(80))
    Distance = db.Column(db.String(80))
    Duration = db.Column(db.String(80))
    Address1 = db.Column(db.String(80))
    Address2 = db.Column(db.String(80))
    Dist = db.Column(db.Integer)
    Sub = db.Column(db.String(5))
    Region1 = db.Column(db.String(80))
    Region2 = db.Column(db.String(80))
    def serialize(self):
        d = Serializer.serialize(self)
        return d

store_list = ['JK1602', 'JK1603', 'JK1604', 'JK1605', 'JK1607', 'JK1608', 'JK1610', 'JK1611', 'JK1612', 'JK1613', 'JK1615', 'JK1616', 'JK1617', 'JK1618', 'JK1620', 'JK1621', 'JK1622', 'JK1624', 'JK1625', 'JK1627', 'JK1628', 'JK1629', 'JK1631', 'JK1634', 'JK1635', 'JK1636', 'JK1637', 'JK1638', 'JK1639', 'JK1642', 'JK1643', 'JK1644', 'JK1645', 'JK1647', 'JK1648', 'JK1649', 'JK1650', 'JK1651', 'JK1652', 'JK1653', 'JK1656', 'JK1657', 'JK1658', 'JK1659', 'JK1660', 'JK1661', 'JK1662', 'JK1663', 'JK1664', 'JK1665', 'JK1666', 'JK1668', 'JK1671', 'JK1673', 'JK1675', 'JK1677', 'JK1679', 'JK1680', 'JK1681', 'JK1682', 'JK1683', 'JK1684', 'JK1685', 'JK1686', 'JK1687', 'JK1689', 'JK1691', 'JK1694', 'JK1695', 'JK1697', 'JK1698', 'JK7002', 'JK7003', 'JK7004', 'JK7005', 'JK7006', 'JK7007', 'JK7009', 'JK7011', 'JK7013', 'JK7014', 'JK7019', 'JK7021', 'JK7023', 'JK7024', 'JK7025', 'JK7028', 'JK7033', 'JK7035', 'JK7036', 'JK7038', 'JK7039', 'JK7040', 'JK7041', 'JK7042', 'JK7044', 'JK7045', 'JK7046', 'JK7047', 'JK7048', 'JK7049', 'JK7055', 'JK7057', 'JK7059', 'JK7062', 'JK7063', 'JK7066', 'JK7067', 'JK7068', 'JK7072', 'JK7076', 'JK7077', 'JK7078', 'JK7079', 'JK7080', 'JK7081', 'JK7082', 'JK7083', 'JK7084', 'JK7085', 'JK7086', 'JK7087', 'JK7088', 'JK7089', 'JK7090', 'JK7091', 'JK7092', 'JK7093', 'JK7094', 'JK7095', 'JK7097', 'JK7098', 'JK7099', 'JK7100', 'JK7101', 'JK7104', 'JK7105', 'JK7106', 'JK7107', 'JK7108', 'JK7109', 'JK7110', 'JK7111', 'JK7112', 'JK7113', 'JK7114', 'JK7117', 'JK7118', 'JK7119', 'JK7120', 'JK7121', 'JK7122', 'JK7123', 'JK7125', 'JK7126', 'JK7127', 'JK7128', 'JK7129', 'JK7130', 'JK7131', 'JK7132', 'JK7133', 'JK7134', 'JK7135', 'JK7136', 'JK7138', 'JK7139', 'JK7140', 'JK7141', 'JK7142', 'JK7143', 'JK7144', 'JK7145', 'JK7147', 'JK7148', 'JK7149', 'JK7150', 'JK7152', 'JK7153', 'JK7154', 'JK7155', 'JK7156', 'JK7157', 'JK7158', 'JK7159', 'JK7160', 'JK7161', 'JK7162', 'JK7163', 'JK7164', 'JK7165', 'JK7166', 'JK7167', 'JK7168', 'JK7169', 'JK7170', 'JK7171', 'JK7172', 'JK7173', 'JK7174', 'JK7175', 'JK7176', 'JK7177', 'JK7178', 'JK7179', 'JK7180', 'JK7181', 'JK7182', 'JK7184', 'JK7185', 'JK7186', 'JK7187', 'JK7188', 'JK7189', 'JK7190', 'JK7191', 'JK7192', 'JK7193', 'JK7194', 'JK7195', 'JK7197', 'JK7198', 'JK7199', 'JK7200', 'JK7201', 'JK7202', 'JK7203', 'JK7204', 'JK7205', 'JK7206', 'JK7207', 'JK7208', 'JK7209', 'JK7210', 'JM1401', 'JM1493', 'JM1504', 'JM1505', 'JM1508', 'JM1514', 'JM1521', 'JM1533', 'JM1539', 'JM1545', 'JM1547', 'JM1549', 'JM1555', 'JM1559', 'JM1565', 'JM1574', 'JM1578', 'JM1588', 'JM1597', 'JM1598', 'JM1600', 'JM1603', 'JM1614', 'JM1627', 'JM1628', 'JM1631', 'JM1637', 'JM1642', 'JM1646', 'JM1649', 'JM1650', 'JM1652', 'JM1653', 'JM1660', 'JM1662', 'JM1664', 'JM1665', 'JM1666', 'JM1670', 'JM1672', 'JM1673', 'JM1677', 'JM1679', 'JM1681', 'JM1683', 'JM1685', 'JM1687', 'JM1690', 'JM1691', 'JM1693', 'JM1697', 'JM1699', 'JM1701', 'JM1702', 'JM1703', 'JM1705', 'JM1706', 'JM1707', 'JM1709', 'JM1710', 'JM1711', 'JM1712', 'JM1713', 'JM1715', 'JM1717', 'JM1718', 'JM1719', 'JM1722', 'JM1723', 'JM1724', 'JM1725', 'JM1726', 'JM1729', 'JM1730', 'JM1731', 'JM1801', 'JM1802', 'JM1803', 'JM1804', 'JM1805', 'JM1808', 'JM1814', 'JM1815', 'JM1816', 'JM1817', 'JM1818', 'JM1819', 'JM1820', 'JM1822', 'JM1823', 'JM1824', 'JM1825', 'JM1831', 'JM1834', 'JM1836', 'JM1837', 'JM1838', 'JM1839', 'JM1840', 'JM1841', 'JM1842', 'JM1843', 'JM1844', 'JM1845', 'JM1846', 'JM1847', 'JM1848', 'JM1849', 'JM1852', 'JM1854', 'JM1855', 'JM1856', 'JM1857', 'JM1861', 'JM2001', 'JM2002', 'JM2004', 'JM2005', 'JM2006', 'JM2007', 'JM2009', 'JM2010', 'JM2011', 'JM2012', 'JM2013', 'JM2014', 'JM2015', 'JM2016', 'JM2017', 'JM2018', 'JM2019', 'JM2020', 'JM2022', 'JM2024', 'JM2025', 'JM2027', 'JM2029', 'JM2033', 'JM2034', 'JM2035', 'JM2038', 'JM2041', 'JM2042', 'JM2043', 'JM2044', 'JM2045', 'JM2046', 'JM2048', 'JM2049', 'JM2051', 'JM2052', 'JM2055', 'JM2057', 'JM2058', 'JM2059', 'JM2060', 'JM2061', 'JM2062', 'JM2063', 'JM2064', 'JM2066', 'JM2067', 'JM2068', 'JM2069', 'JM2070', 'JM2071', 'JM2072', 'JM2073', 'JM2074', 'JM2075', 'JM2076', 'JM2077', 'JM2078', 'JM2079', 'JM2080', 'JM2082', 'JM2083', 'JM2084', 'JM2085', 'JM2086', 'JM2087', 'JM2088', 'JM2089', 'JM2092', 'JM4700', 'JM4800', 'JM4801', 'JM4802', 'JM4803', 'JM4804', 'JM4900', 'JM4901', 'JN0051', 'JN0054', 'JN0055', 'JN0068', 'JN0081', 'JN0100', 'JN0103', 'JN0140', 'JN0154', 'JN0155', 'JN0160', 'JN0162', 'JN0175', 'JN0177', 'JN0179', 'JN0180', 'JN0182', 'JN0191', 'JN0192', 'JN0195', 'JN0198', 'JN0209', 'JN0219', 'JN0222', 'JN0223', 'JN0228', 'JN0234', 'JN0236', 'JN0242', 'JN0243', 'JN0244', 'JN0245', 'JN0246', 'JN0249', 'JN0250', 'JN0251', 'JN0252', 'JN0253', 'JN0254', 'JN0255', 'JN0256', 'JN0263', 'JN0265', 'JN0268', 'JN0269', 'JN0270', 'JN0272', 'JN0274', 'JN0278', 'JN0279', 'JN0281', 'JN0284', 'JN0287', 'JN0297', 'JN0300', 'JN0302', 'JN0303', 'JN0305', 'JN0306', 'JN0307', 'JN0312', 'JN0313', 'JN0315', 'JN0316', 'JN0322', 'JN0325', 'JN0326', 'JN0333', 'JN0334', 'JN0335', 'JN0336', 'JN0337', 'JN0340', 'JN0341', 'JN0342', 'JN0343', 'JN0344', 'JN0355', 'JN0376', 'JN0379', 'JN0383', 'JN0388', 'JN0391', 'JN0392', 'JN0407', 'JN0408', 'JN0409', 'JN0411', 'JN0412', 'JN0413', 'JN0417', 'JN0418', 'JN0419', 'JN0427', 'JN0437', 'JN0442', 'JN0448', 'JN0449', 'JN0454', 'JN0469', 'JN0478', 'JN0479', 'JN0489', 'JN0494', 'JN0497', 'JN0505', 'JN0507', 'JN0508', 'JN0509', 'JN0510', 'JN0511', 'JN0512', 'JN0513', 'JN0514', 'JN0515', 'JN0516', 'JN0517', 'JN0520', 'JN0524', 'JN0525', 'JN0526', 'JN0527', 'JN0528', 'JN0529', 'JN0530', 'JN0532', 'JN0533', 'JN0534', 'JN0536', 'JN0537', 'JN0540', 'JN0541', 'JN0542', 'JN0551', 'JN0553', 'JN0555', 'JN0557', 'JN0558', 'JN0560', 'JN0561', 'JN0562', 'JN0563', 'JN0564', 'JN0565', 'JN0566', 'JN0567', 'JN0568', 'JN0569', 'JN0572', 'JN0573', 'JN0574', 'JN0577', 'JN0580', 'JN0581', 'JN0582', 'JN0583', 'JN0584', 'JN0585', 'JN0586', 'JN0587', 'JN0590', 'JN0591', 'JN0592', 'JN0594', 'JN0596', 'JN0598', 'JN0599', 'JN0700', 'JN0701', 'JN0703', 'JN0707', 'JN0710', 'JN0714', 'JN0716', 'JN0719', 'JN0720', 'JN0721', 'JN0722', 'JN0723', 'JN0724', 'JN0726', 'JN0729', 'JN0730', 'JN0731', 'JN0732', 'JN0733', 'JN0734', 'JN0736', 'JN0737', 'JN0738', 'JN0739', 'JN0740', 'JN0742', 'JN0743', 'JN0744', 'JN0746', 'JN0747', 'JN0751', 'JN0752', 'JN0755', 'JN0756', 'JN0758', 'JN0759', 'JN0760', 'JN0761', 'JN0762', 'JN0763', 'JN0766', 'JN0769', 'JN0770', 'JN0771', 'JN0772', 'JN0774', 'JN0777', 'JN0778', 'JN0780', 'JN0782', 'JN0785', 'JN0786', 'JN0787', 'JN0788', 'JN0789', 'JN0793', 'JN0797', 'JN0798', 'JN0802', 'JN0804', 'JN0807', 'JN0809', 'JN0810', 'JN0811', 'JN0813', 'JN0814', 'JN0815', 'JN0816', 'JN0817', 'JN0819', 'JN0821', 'JN0822', 'JN0823', 'JN0827', 'JN0828', 'JN0829', 'JN0831', 'JN0832', 'JN0833', 'JN0835', 'JN0836', 'JN0837', 'JN0839', 'JN0841', 'JN0842', 'JN0845', 'JN0846', 'JN0848', 'JN0849', 'JN0851', 'JN0854', 'JN0856', 'JN0857', 'JN0858', 'JN0865', 'JN0867', 'JN0868', 'JN0869', 'JN0870', 'JN0871', 'JN0874', 'JN0875', 'JN0876', 'JN0877', 'JN0879', 'JN0880', 'JN0887', 'JN0890', 'JN0892', 'JN0899', 'JN0900', 'JN0901', 'JN0903', 'JN0905', 'JN0908', 'JN0912', 'JN0913', 'JN0914', 'JN0917', 'JN0918', 'JN0919', 'JN0920', 'JN0921', 'JN0922', 'JN0923', 'JN0924', 'JN0925', 'JN0926', 'JN0927', 'JN0928', 'JN0929', 'JN0932', 'JN0933', 'JN0934', 'JN0935', 'JN0938', 'JN0939', 'JN0940', 'JN0942', 'JN0945', 'JN0946', 'JN0947', 'JN0948', 'JN0949', 'JN0950', 'JN0952', 'JN0953', 'JN0954', 'JN0955', 'JN0957', 'JN0958', 'JN0960', 'JN0962', 'JN0963', 'JN0965', 'JN0966', 'JN0969', 'JN0971', 'JN0973', 'JN0974', 'JN0975', 'JN0976', 'JN0978', 'JN0979', 'JN0981', 'JN0982', 'JN0983', 'JN0985', 'JN0986', 'JN0990', 'JN0994', 'JN0995', 'JN0996', 'JN1000', 'JN1002', 'JN1003', 'JN1005', 'JN1008', 'JN1011', 'JN1012', 'JN1015', 'JN1016', 'JN1017', 'JN1019', 'JN1020', 'JN1021', 'JN1023', 'JN1024', 'JN1025', 'JN1027', 'JN1028', 'JN1029', 'JN1031', 'JN1032', 'JN1034', 'JN1035', 'JN1036', 'JN1037', 'JN1038', 'JN1039', 'JN1040', 'JN1041', 'JN1042', 'JN1043', 'JN1045', 'JN1048', 'JN1050', 'JN1051', 'JN1052', 'JN1053', 'JN1055', 'JN1056', 'JN1057', 'JN1060', 'JN1061', 'JN1065', 'JN1066', 'JN1069', 'JN1070', 'JN1072', 'JN1073', 'JN1074', 'JN1076', 'JN1078', 'JN1079', 'JN1081', 'JN1087', 'JN1088', 'JN1089', 'JN1090', 'JN1091', 'JN1093', 'JN1094', 'JN1095', 'JN1096', 'JN1098', 'JN1099', 'JN1103', 'JN1106', 'JN1107', 'JN1108', 'JN1110', 'JN1112', 'JN1113', 'JN1114', 'JN1115', 'JN1116', 'JN1117', 'JN1118', 'JN1119', 'JN1120', 'JN1121', 'JN1122', 'JN1123', 'JN1126', 'JN1127', 'JN1128', 'JN1129', 'JN1130', 'JN1132', 'JN1133', 'JN1134', 'JN1135', 'JN1137', 'JN1138', 'JN1140', 'JN1141', 'JN1142', 'JN1146', 'JN1147', 'JN1148', 'JN1149', 'JN1150', 'JN1151', 'JN1152', 'JN1153', 'JN1154', 'JN1156', 'JN1157', 'JN1158', 'JN1159', 'JN1161', 'JN1162', 'JN1163', 'JN1166', 'JN1167', 'JN1168', 'JN1169', 'JN1170', 'JN1171', 'JN1172', 'JN1174', 'JN1176', 'JN1178', 'JN1180', 'JN1182', 'JN1183', 'JN1185', 'JN1186', 'JN1187', 'JN1188', 'JN1189', 'JN1190', 'JN1193', 'JN1195', 'JN1196', 'JN1197', 'JN1198', 'JN1199', 'JN1201', 'JN1203', 'JN1205', 'JN1206', 'JN1207', 'JN1208', 'JN1210', 'JN1211', 'JN1212', 'JN1213', 'JN1214', 'JN1215', 'JN1217', 'JN1218', 'JN1220', 'JN1221', 'JN1224', 'JN1225', 'JN1226', 'JN1227', 'JN1228', 'JN1230', 'JN1231', 'JN1233', 'JN1237', 'JN1241', 'JN1243', 'JN1244', 'JN1245', 'JN1246', 'JN1247', 'JN1248', 'JN1249', 'JN1250', 'JN1252', 'JN1253', 'JN1256', 'JN1258', 'JN1260', 'JN1262', 'JN1264', 'JN1265', 'JN1270', 'JN1272', 'JN1274', 'JN1275', 'JN1276', 'JN1278', 'JN1279', 'JN1280', 'JN1283', 'JN1284', 'JN1285', 'JN1286', 'JN1288', 'JN1289', 'JN1290', 'JN1291', 'JN1292', 'JN1293', 'JN1294', 'JN1296', 'JN1297', 'JN1299', 'JN1300', 'JN1301', 'JN1302', 'JN1303', 'JN1305', 'JN1307', 'JN1308', 'JN1310', 'JN1311', 'JN1312', 'JN1316', 'JN1317', 'JN1318', 'JN1319', 'JN1320', 'JN1321', 'JN1322', 'JN1323', 'JN1324', 'JN1325', 'JN1326', 'JN1328', 'JN1329', 'JN1330', 'JN1331', 'JN1333', 'JN1335', 'JN1336', 'JN1339', 'JN1344', 'JN1345', 'JN1346', 'JN1347', 'JN1349', 'JN1351', 'JN1353', 'JN1356', 'JN1360', 'JN1361', 'JN1362', 'JN1366', 'JN1368', 'JN1369', 'JN1370', 'JN1374', 'JN1375', 'JN1376', 'JN1378', 'JN1381', 'JN1382', 'JN1384', 'JN1385', 'JN1386', 'JN1387', 'JN1388', 'JN1389', 'JN1391', 'JN1392', 'JN1393', 'JN1396', 'JN1397', 'JN1398', 'JN1399', 'JN1402', 'JN1403', 'JN1404', 'JN1405', 'JN1406', 'JN1407', 'JN1408', 'JN1409', 'JN1410', 'JN1411', 'JN1413', 'JN1414', 'JN1417', 'JN1418', 'JN1419', 'JN1420', 'JN1422', 'JN1423', 'JN1425', 'JN1426', 'JN1428', 'JN1429', 'JN1430', 'JN1431', 'JN1435', 'JN1436', 'JN1438', 'JN1439', 'JN1440', 'JN1444', 'JN1446', 'JN1447', 'JN1449', 'JN1451', 'JN1452', 'JN1453', 'JN1454', 'JN1456', 'JN1457', 'JN1458', 'JN1459', 'JN1460', 'JN1461', 'JN1462', 'JN1463', 'JN1464', 'JN1466', 'JN1467', 'JN1468', 'JN1470', 'JN1472', 'JN1478', 'JN1480', 'JN1482', 'JN1484', 'JN1485', 'JN1487', 'JN1488', 'JN1490', 'JN1493', 'JN1495', 'JN1496', 'JN1507', 'JN1523', 'JN1527', 'JN1546', 'JN1565', 'JN1570', 'JN1574', 'JN1593', 'JN1705', 'JN1712', 'JN1727', 'JN1741', 'JN1750', 'JN1757', 'JN1764', 'JN1776', 'JN1779', 'JN1805', 'JN1824', 'JN1830', 'JN1838', 'JN1853', 'JN1859', 'JN1860', 'JN1864', 'JN1866', 'JN1869', 'JN1872', 'JN1880', 'JN1881', 'JN1883', 'JN1884', 'JN1885', 'JN1886', 'JN1888', 'JN1893', 'JN1895', 'JN1897', 'JN1898', 'JN1911', 'JN1932', 'JN1934', 'JN1943', 'JN1944', 'JN1945', 'JN5001', 'JN5002', 'JN5003', 'JN5004', 'JN5005', 'JN5006', 'JN5007', 'JN5008', 'JN5009', 'JN5010', 'JN5011', 'JN5013', 'JN5014', 'JN5015', 'JN5016', 'JN5017', 'JN5018', 'JN5019', 'JN5024', 'JN5025', 'JN5027', 'JN5028', 'JN5033', 'JN5034', 'JN5036', 'JN5037', 'JN5038', 'JN5039', 'JN5040', 'JN5041', 'JN5042', 'JN5043', 'JN5044', 'JN5045', 'JN5046', 'JN5047', 'JN5049', 'JN5050', 'LB6200', 'LB6201', 'LB6204', 'LB6205', 'LB6208', 'LB6210', 'LB6213', 'LB6215', 'LB6216', 'LB6218', 'LB6219', 'LB6220', 'LB6225', 'LB6229', 'LB6230', 'LB6231', 'LB6232', 'LB6233', 'LB6235', 'LB6236', 'LB6239', 'LB6240', 'LB6241', 'LB6242', 'LB6243', 'LB6245', 'LB6246', 'LB6247', 'LB6250', 'LB6259', 'LB6260', 'LB6261', 'LB6265', 'LB6266', 'LB6267', 'LB6268', 'LB6269', 'LB6270', 'SH3001', 'SH3029', 'UG0009', 'UG0010', 'UG0011', 'UG0012', 'UG0013', 'UG0017', 'UG0023', 'UG0024', 'UG0026', 'UG0033', 'UG0036', 'UG0037', 'UG0039', 'UG0044', 'UG0046', 'UG0048', 'UG0049', 'UG0056', 'UG0057', 'UG0060', 'UG0061', 'UG0067', 'UG0073', 'UG0076', 'UG0080', 'UG0083', 'UG0085', 'UG0096', 'UG0097', 'UG0099', 'UG0101', 'UG0109', 'UG0110', 'UG0111', 'UG0120', 'UG0123', 'UG0124', 'UG0128', 'UG0131', 'UG0137', 'UG0164', 'UG0173', 'UG0176', 'UG0187', 'UG0206', 'UG0225', 'UG0304', 'UG0356', 'UG0373', 'UG0386', 'UG0444', 'UG0472', 'UG0484', 'UG0485', 'UG0488', 'UG0705', 'UG0708', 'UG0805', 'UG0882', 'UG0883', 'UG0884', 'UG0885', 'UG0894', 'UG0944', 'UG1155', 'UG1177', 'UG1442', 'UG1505', 'UG1506', 'UG1524', 'UG1536', 'UG1554', 'UG1583', 'UG1587', 'UG1599', 'UG1744']

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def find_home(store):
    if store in store_list:
        home = Location.query.filter_by(Location1=store).first()
    else:
        home = None
    return home

def find_stores(store, c_list, d_list):
    if store in store_list:
        stores = None
        if 'AL' in c_list:
            if 'm5' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 5).order_by(Location.Dist).all()
            elif 'm10' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 10).order_by(Location.Dist).all()
            elif 'm25' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25).order_by(Location.Dist).all()
            elif 'm50' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 50).order_by(Location.Dist).all()
            else:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25).order_by(Location.Dist).all()
        else:
            if 'JM' in c_list:
                if 'm5' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 5, Location.Sub=='JM').order_by(Location.Dist).all()
                elif 'm10' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 10, Location.Sub=='JM').order_by(Location.Dist).all()
                elif 'm25' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25, Location.Sub=='JM').order_by(Location.Dist).all()
                elif 'm50' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 50, Location.Sub=='JM').order_by(Location.Dist).all()
                else:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25, Location.Sub=='JM').order_by(Location.Dist).all()
            if 'JN' in c_list:
                if 'm5' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 5, Location.Sub!='JM').order_by(Location.Dist).all()
                elif 'm10' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 10, Location.Sub!='JM').order_by(Location.Dist).all()
                elif 'm25' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25, Location.Sub!='JM').order_by(Location.Dist).all()
                elif 'm50' in d_list:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 50, Location.Sub!='JM').order_by(Location.Dist).all()
                else:
                    stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25, Location.Sub!='JM').order_by(Location.Dist).all()
        if stores == None:
            if 'm5' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 5).order_by(Location.Dist).all()
            elif 'm10' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 10).order_by(Location.Dist).all()
            elif 'm25' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25).order_by(Location.Dist).all()
            elif 'm50' in d_list:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 50).order_by(Location.Dist).all()
            else:
                stores = Location.query.filter(Location.Location1==store, Location.Dist <= 25).order_by(Location.Dist).all()
    else:
        stores = None
    return stores


def get_data(stores):
    d = {}
    i = 0
    for store in stores:
        d[(i)] = store.Location2, store.Latitude2, store.Longitude2, store.Distance, store.Duration, store.Address1, store.Address2, store.Dist, store.Sub, store.Region1, store.Region2
        i += 1
    return d

def make_site(r):
    b1 = """
    <html>
        <head>
            <style>
                h1 { font-family: "Open Sans"; font-size: 18px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px; }
                h3 { font-family: "Open Sans"; font-size: 16px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15.4px; }
                p, input, td { font-family: "Open Sans"; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; }
                button { font-family: "Open Sans"; font-size: 15px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; }
                th { font-family: "Open Sans"; font-size: 15px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 20px; letter-spacing:0.1em;}
                blockquote { font-family: "Open Sans"; font-size: 21px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 30px; }
                pre { font-family: "Open Sans"; font-size: 13px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 18.5714px; }
            </style>
            <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />
            <link rel="stylesheet" link href="/static/css/styles.css">
        </head>
        <body>
            <div class="grid-container">
                <div id="Event" class="Table1">
                    <table id="t01">
                        <tr>
                        <th class="tableexport-string target">Location Code</th>
                            <th class="tableexport-string target">District/Region</th>
                            <th class="tableexport-string target">Street Address</th>
                            <th class="tableexport-string target">Distance</th>
                            <th class="tableexport-string target">Duration</th>
                        </tr>
                        <tr>
                            <td class="tableexport-string target">&nbsp;{{home.Location1}}</td>
                            <td class="tableexport-string target">{{home.Region1}}</td>
                            <td class="tableexport-string target">{{home.Address1}}</td>
                            <td class="tableexport-string target">N/A</td>
                            <td class="tableexport-string target">N/A</td>
                        </tr>"""

    t0 = """
                    </table>
                </div>"""

    t1 = """
                <div class="Search">
                    <h1 style="text-align:center;">Enter Location Code:</h1>
                    <form action="/locate" method="post">
                        <p style="text-align:center;"><input type="text" id="userInput" name="store" placeholder="e.g., JN0255, JM1819" value="{{request.form['store']}}"/></p>
                        <p style="text-align:center;"><input class="main-search" type="submit" value="Find Nearby Stores" /></p>
                        <div class="gap-10"></div>
                        <h3 style="text-align:center;">Select Company:</h3>
                        <div style="padding-left:15px;">
                        <input type="radio" name="company" value="AL" {{cAL}}> All<br>
                        <input type="radio" name="company" value="JN" {{cJN}}> Journey's<br>
                        <input type="radio" name="company" value="JM" {{cJM}}> Johnston & Murphy<br>
                        </div>
                        <div class="gap-20"></div>
                        <h3 style="text-align:center;">Select Distance:</h3>
                        <div style="padding-left:15px;">
                        <input type="radio" name="distance" value="m5" {{cr5}}> 5 miles<br>
                        <input type="radio" name="distance" value="m10" {{cr10}}> 10 miles<br>
                        <input type="radio" name="distance" value="m25" {{cr25}}> 25 miles<br>
                        <input type="radio" name="distance" value="m50" {{cr50}}> 50 miles<br>
                        </div>
                    </form>
                </div>
            </div>"""

    t2 = """
                <div class="Map" id="map">
                    <script>
                        function initMap() {
                        var home = {lat: {{home.Latitude1}}, lng: {{home.Longitude1}}};
                        var c1 = {{count}};
                        var styledMapType = new google.maps.StyledMapType(
                            [
                                {
                                    "elementType": "geometry",
                                    "stylers": [
                                        {
                                            "hue": "#ff4400"
                                        },
                                        {
                                            "saturation": -68
                                        },
                                        {
                                            "lightness": -4
                                        },
                                        {
                                            "gamma": 0.72
                                        }
                                    ]
                                },
                                {
                                    "featureType": "road",
                                    "elementType": "labels.icon"
                                },
                                {
                                    "featureType": "landscape.man_made",
                                    "elementType": "geometry",
                                    "stylers": [
                                        {
                                            "hue": "#0077ff"
                                        },
                                        {
                                            "gamma": 3.1
                                        }
                                    ]
                                },
                                {
                                    "featureType": "water",
                                    "stylers": [
                                        {
                                            "hue": "#00ccff"
                                        },
                                        {
                                            "gamma": 0.44
                                        },
                                        {
                                            "saturation": -33
                                        }
                                    ]
                                },
                                {
                                    "featureType": "poi.park",
                                    "stylers": [
                                        {
                                            "hue": "#44ff00"
                                        },
                                        {
                                            "saturation": -23
                                        }
                                    ]
                                },
                                {
                                    "featureType": "water",
                                    "elementType": "labels.text.fill",
                                    "stylers": [
                                        {
                                            "hue": "#007fff"
                                        },
                                        {
                                            "gamma": 0.77
                                        },
                                        {
                                            "saturation": 65
                                        },
                                        {
                                            "lightness": 99
                                        }
                                    ]
                                },
                                {
                                    "featureType": "water",
                                    "elementType": "labels.text.stroke",
                                    "stylers": [
                                        {
                                            "gamma": 0.11
                                        },
                                        {
                                            "weight": 5.6
                                        },
                                        {
                                            "saturation": 99
                                        },
                                        {
                                            "hue": "#0091ff"
                                        },
                                        {
                                            "lightness": -86
                                        }
                                    ]
                                },
                                {
                                    "featureType": "transit.line",
                                    "elementType": "geometry",
                                    "stylers": [
                                        {
                                            "lightness": -48
                                        },
                                        {
                                            "hue": "#ff5e00"
                                        },
                                        {
                                            "gamma": 1.2
                                        },
                                        {
                                            "saturation": -23
                                        }
                                    ]
                                },
                                {
                                    "featureType": "transit",
                                    "elementType": "labels.text.stroke",
                                    "stylers": [
                                        {
                                            "saturation": -64
                                        },
                                        {
                                            "hue": "#ff9100"
                                        },
                                        {
                                            "lightness": 16
                                        },
                                        {
                                            "gamma": 0.47
                                        },
                                        {
                                            "weight": 2.7
                                        }
                                    ]
                                }
                            ],
                            {name: 'Styled Map'});
                        var map = new google.maps.Map(
                            document.getElementById('map'), {zoom: {{zoom}}, center: home});
                        var contentString = '<div id="content">'+
                                                      '<div id="siteNotice">'+
                                                      '</div>'+
                                                      '<h2 id="firstHeading" class="firstHeading">{{home.Location1}}</h2>'+
                                                      '</div>';
                        var home_marker = new google.maps.Marker({
                                position: home,
                                icon: {
                                path: google.maps.SymbolPath.CIRCLE,
                                scale: 7
                                },
                                draggable: false,
                                map: map
                                });
                        var infowindow = new google.maps.InfoWindow({
                            content: contentString});
                        home_marker.addListener('mouseover', function() {
                            infowindow.open(map, home_marker);
                        });
                        home_marker.addListener('mouseout', function() {
                            infowindow.close(map, home_marker);
                        });"""

    s22 = """
                        if (c1 > {num1}) @
                            var store{num2} = @lat: @@d[{num1}][1]$$, lng: @@d[{num1}][2]$$$;
                            var marker{num2} = new google.maps.Marker(@position: store{num2}, map: map$);
                            var contentString{num2} = '<div id="content">'+
                                                          '<div id="siteNotice">'+
                                                          '</div>'+
                                                          '<h2 id="firstHeading" class="firstHeading">@@d[{num1}][0]$$</h2>'+
                                                          '<div id="bodyContent">'+
                                                          '<dt>Distance:</dt><dd>@@d[{num1}][3]$$ miles</dd>' +
                                                          '<dt>Duration:</dt><dd>@@d[{num1}][4]$$</dd>'+
                                                          '</div>'+
                                                          '</div>';
                            var infowindow{num2} = new google.maps.InfoWindow(@
                                content: contentString{num2}$);
                            marker{num2}.addListener('mouseover', function() @
                                infowindow{num2}.open(map, marker{num2});
                            $);
                            marker{num2}.addListener('mouseout', function() @
                                infowindow{num2}.close(map, marker{num2});
                            $);
                        $;"""
    b2 = """
                            map.mapTypes.set('styled_map', styledMapType);
                            map.setMapTypeId('styled_map');
                        }
                    </script>
                    <script async defer
                        src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
                    </script>
                    <script lang="javascript" src="/static/js/xlsx.core.min.js"></script>
                    <script src="/static/js/FileSaver.js"></script>
                    <script src="/static/js/tableexport.js"></script>
                    <script>
                        var table = TableExport(document.getElementsByTagName("table"), {
                                  headers: true,                      // (Boolean), display table headers (th or td elements) in the <thead>, (default: true)
                                  footers: true,                      // (Boolean), display table footers (th or td elements) in the <tfoot>, (default: false)
                                  formats: ["xlsx"],    // (String[]), filetype(s) for the export, (default: ['xlsx', 'csv', 'txt'])
                                  filename: "{{home.Location1}} {{miles}} {{now}}",                     // (id, String), filename for the downloaded file, (default: 'id')
                                  bootstrap: false,                   // (Boolean), style buttons using bootstrap, (default: true)
                                  exportButtons: true,                // (Boolean), automatically generate the built-in export buttons for each of the specified formats (default: true)
                                  position: "bottom",                 // (top, bottom), position of the caption element relative to table, (default: 'bottom')
                                  ignoreRows: null,                   // (Number, Number[]), row indices to exclude from the exported file(s) (default: null)
                                  ignoreCols: null,                   // (Number, Number[]), column indices to exclude from the exported file(s) (default: null)
                                  trimWhitespace: true,               // (Boolean), remove all leading/trailing newlines, spaces, and tabs from cell text in the exported file(s) (default: false)
                                  RTL: false,                         // (Boolean), set direction of the worksheet to right-to-left (default: false)
                                  sheetname: "{{home.Location1}} {{miles}}"                     // (id, String), sheet name for the exported spreadsheet, (default: 'id')
                                });
                        var exportData = table.getExportData();
                        var xlsxData = exportData.table.xlsx;
                    </script>
                </div>
                <div class="Space"></div>"""

    c3 = """
                        <tr>
                            <td class="tableexport-string target">&nbsp;@@d[{num1}][0]$$</td>
                            <td class="tableexport-string target">@@d[{num1}][10]$$</td>
                            <td class="tableexport-string target">@@d[{num1}][6]$$</td>
                            <td class="tableexport-string target">@@d[{num1}][3]$$ miles</td>
                            <td class="tableexport-string target">@@d[{num1}][4]$$</td>
                        </tr>"""

    c4 = ""

    s23 = ""
    num1 = 0
    num2 = 1

    for i in range(r):
        s23 += s22.format(num1=num1, num2=num2)
        num1 += 1
        num2 += 1

    s24 = s23.replace("@", "{").replace("$", "}")

    num1 = 0
    num2 = 1

    for i in range(r):
        c4 += c3.format(num1=num1, num2=num2)
        num1 += 1
        num2 += 1

    c5 = c4.replace("@", "{").replace("$", "}")

    c9 = """
        </body>
    </html>"""

    website = b1 + c5 + t0 + t2 + s24 + b2 + t1 + c9

    return website


def make_test_site(r):
    b1 = """
    <html>
        <head>
            <style>
                h1 { font-family: "Open Sans"; font-size: 18px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 26.4px; }
                h3 { font-family: "Open Sans"; font-size: 16px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 15.4px; }
                p, input, td { font-family: "Open Sans"; font-size: 14px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; }
                button { font-family: "Open Sans"; font-size: 15px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 20px; }
                th { font-family: "Open Sans"; font-size: 15px; font-style: normal; font-variant: normal; font-weight: 700; line-height: 20px; letter-spacing:0.1em;}
                blockquote { font-family: "Open Sans"; font-size: 21px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 30px; }
                pre { font-family: "Open Sans"; font-size: 13px; font-style: normal; font-variant: normal; font-weight: 400; line-height: 18.5714px; }
            </style>
            <link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />
            <link rel="stylesheet" link href="/static/css/test_styles.css">
        </head>
        <body>
            <div class="grid-container">
                <div id="Event" class="Table1">
                    <table id="t01">
                        <tr>
                        <th class="tableexport-string target">Location Code</th>
                            <th class="tableexport-string target">District/Region</th>
                            <th class="tableexport-string target">Street Address</th>
                            <th class="tableexport-string target">Distance</th>
                            <th class="tableexport-string target">Duration</th>
                        </tr>
                        <tr>
                            <td class="tableexport-string target">&nbsp;{{home.Location1}}</td>
                            <td class="tableexport-string target">{{home.Region1}}</td>
                            <td class="tableexport-string target">{{home.Address1}}</td>
                            <td class="tableexport-string target">N/A</td>
                            <td class="tableexport-string target">N/A</td>
                        </tr>"""

    t0 = """
                    </table>
                </div>"""

    t1 = """
                <div class="Search">
                    <h1 style="text-align:center;">Enter Location Code:</h1>
                    <form action="/test/locate" method="post">
                        <p style="text-align:center;"><input type="text" id="userInput" name="store" placeholder="e.g., JN0255, JM1819" value="{{request.form['store']}}"/></p>
                        <p style="text-align:center;"><input class="main-search" type="submit" value="Find Nearby Stores" /></p>
                        <div class="gap-10"></div>
                        <h3 style="text-align:center;">Select Company:</h3>
                        <div style="padding-left:15px;">
                        <input type="radio" name="company" value="AL" {{cAL}}> All<br>
                        <input type="radio" name="company" value="JN" {{cJN}}> Journey's<br>
                        <input type="radio" name="company" value="JM" {{cJM}}> Johnston & Murphy<br>
                        </div>
                        <div class="gap-20"></div>
                        <h3 style="text-align:center;">Select Distance:</h3>
                        <div style="padding-left:15px;">
                        <input type="radio" name="distance" value="m5" {{cr5}}> 5 miles<br>
                        <input type="radio" name="distance" value="m10" {{cr10}}> 10 miles<br>
                        <input type="radio" name="distance" value="m25" {{cr25}}> 25 miles<br>
                        <input type="radio" name="distance" value="m50" {{cr50}}> 50 miles<br>
                        </div>
                    </form>
                </div>
            </div>"""

    t2 = """
                <div class="Map" id="map">
                    <script>
                        function initMap() {
                        var home = {lat: {{home.Latitude1}}, lng: {{home.Longitude1}}};
                        var c1 = {{count}};
                        var styledMapType = new google.maps.StyledMapType(
                            [
                              {elementType: 'geometry', stylers: [{color: '#ebe3cd'}]},
                              {elementType: 'labels.text.fill', stylers: [{color: '#523735'}]},
                              {elementType: 'labels.text.stroke', stylers: [{color: '#f5f1e6'}]},
                              {
                                featureType: 'administrative',
                                elementType: 'geometry.stroke',
                                stylers: [{color: '#c9b2a6'}]
                              },
                              {
                                featureType: 'administrative.land_parcel',
                                elementType: 'geometry.stroke',
                                stylers: [{color: '#dcd2be'}]
                              },
                              {
                                featureType: 'administrative.land_parcel',
                                elementType: 'labels.text.fill',
                                stylers: [{color: '#ae9e90'}]
                              },
                              {
                                featureType: 'landscape.natural',
                                elementType: 'geometry',
                                stylers: [{color: '#dfd2ae'}]
                              },
                              {
                                featureType: 'poi',
                                elementType: 'geometry',
                                stylers: [{color: '#dfd2ae'}]
                              },
                              {
                                featureType: 'poi',
                                elementType: 'labels.text.fill',
                                stylers: [{color: '#93817c'}]
                              },
                              {
                                featureType: 'poi.park',
                                elementType: 'geometry.fill',
                                stylers: [{color: '#a5b076'}]
                              },
                              {
                                featureType: 'poi.park',
                                elementType: 'labels.text.fill',
                                stylers: [{color: '#447530'}]
                              },
                              {
                                featureType: 'road',
                                elementType: 'geometry',
                                stylers: [{color: '#f5f1e6'}]
                              },
                              {
                                featureType: 'road.arterial',
                                elementType: 'geometry',
                                stylers: [{color: '#fdfcf8'}]
                              },
                              {
                                featureType: 'road.highway',
                                elementType: 'geometry',
                                stylers: [{color: '#f8c967'}]
                              },
                              {
                                featureType: 'road.highway',
                                elementType: 'geometry.stroke',
                                stylers: [{color: '#e9bc62'}]
                              },
                              {
                                featureType: 'road.highway.controlled_access',
                                elementType: 'geometry',
                                stylers: [{color: '#e98d58'}]
                              },
                              {
                                featureType: 'road.highway.controlled_access',
                                elementType: 'geometry.stroke',
                                stylers: [{color: '#db8555'}]
                              },
                              {
                                featureType: 'road.local',
                                elementType: 'labels.text.fill',
                                stylers: [{color: '#806b63'}]
                              },
                              {
                                featureType: 'transit.line',
                                elementType: 'geometry',
                                stylers: [{color: '#dfd2ae'}]
                              },
                              {
                                featureType: 'transit.line',
                                elementType: 'labels.text.fill',
                                stylers: [{color: '#8f7d77'}]
                              },
                              {
                                featureType: 'transit.line',
                                elementType: 'labels.text.stroke',
                                stylers: [{color: '#ebe3cd'}]
                              },
                              {
                                featureType: 'transit.station',
                                elementType: 'geometry',
                                stylers: [{color: '#dfd2ae'}]
                              },
                              {
                                featureType: 'water',
                                elementType: 'geometry.fill',
                                stylers: [{color: '#b9d3c2'}]
                              },
                              {
                                featureType: 'water',
                                elementType: 'labels.text.fill',
                                stylers: [{color: '#92998d'}]
                              }
                            ],
                            {name: 'Styled Map'});
                        var map = new google.maps.Map(
                            document.getElementById('map'), {zoom: {{zoom}}, center: home});
                        var contentString = '<div id="content">'+
                                                      '<div id="siteNotice">'+
                                                      '</div>'+
                                                      '<h2 id="firstHeading" class="firstHeading">{{home.Location1}}</h2>'+
                                                      '</div>';
                        var home_marker = new google.maps.Marker({
                                position: home,
                                icon: {
                                path: google.maps.SymbolPath.CIRCLE,
                                scale: 7
                                },
                                draggable: false,
                                map: map
                                });
                        var infowindow = new google.maps.InfoWindow({
                            content: contentString});
                        home_marker.addListener('mouseover', function() {
                            infowindow.open(map, home_marker);
                        });
                        home_marker.addListener('mouseout', function() {
                            infowindow.close(map, home_marker);
                        });"""

    s22 = """
                        if (c1 > {num1}) @
                            var store{num2} = @lat: @@d[{num1}][1]$$, lng: @@d[{num1}][2]$$$;
                            var marker{num2} = new google.maps.Marker(@position: store{num2}, map: map$);
                            var contentString{num2} = '<div id="content">'+
                                                          '<div id="siteNotice">'+
                                                          '</div>'+
                                                          '<h2 id="firstHeading" class="firstHeading">@@d[{num1}][0]$$</h2>'+
                                                          '<div id="bodyContent">'+
                                                          '<dt>Distance:</dt><dd>@@d[{num1}][3]$$ miles</dd>' +
                                                          '<dt>Duration:</dt><dd>@@d[{num1}][4]$$</dd>'+
                                                          '</div>'+
                                                          '</div>';
                            var infowindow{num2} = new google.maps.InfoWindow(@
                                content: contentString{num2}$);
                            marker{num2}.addListener('mouseover', function() @
                                infowindow{num2}.open(map, marker{num2});
                            $);
                            marker{num2}.addListener('mouseout', function() @
                                infowindow{num2}.close(map, marker{num2});
                            $);
                        $;"""
    b2 = """
                            map.mapTypes.set('styled_map', styledMapType);
                            map.setMapTypeId('styled_map');
                        }
                    </script>
                    <script async defer
                        src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
                    </script>
                    <script lang="javascript" src="/static/js/xlsx.core.min.js"></script>
                    <script src="/static/js/FileSaver.js"></script>
                    <script src="/static/js/tableexport.js"></script>
                    <script>
                        var table = TableExport(document.getElementsByTagName("table"), {
                                  headers: true,                      // (Boolean), display table headers (th or td elements) in the <thead>, (default: true)
                                  footers: true,                      // (Boolean), display table footers (th or td elements) in the <tfoot>, (default: false)
                                  formats: ["xlsx"],    // (String[]), filetype(s) for the export, (default: ['xlsx', 'csv', 'txt'])
                                  filename: "{{home.Location1}} {{miles}} {{now}}",                     // (id, String), filename for the downloaded file, (default: 'id')
                                  bootstrap: false,                   // (Boolean), style buttons using bootstrap, (default: true)
                                  exportButtons: true,                // (Boolean), automatically generate the built-in export buttons for each of the specified formats (default: true)
                                  position: "bottom",                 // (top, bottom), position of the caption element relative to table, (default: 'bottom')
                                  ignoreRows: null,                   // (Number, Number[]), row indices to exclude from the exported file(s) (default: null)
                                  ignoreCols: null,                   // (Number, Number[]), column indices to exclude from the exported file(s) (default: null)
                                  trimWhitespace: true,               // (Boolean), remove all leading/trailing newlines, spaces, and tabs from cell text in the exported file(s) (default: false)
                                  RTL: false,                         // (Boolean), set direction of the worksheet to right-to-left (default: false)
                                  sheetname: "{{home.Location1}} {{miles}}"                     // (id, String), sheet name for the exported spreadsheet, (default: 'id')
                                });
                        var exportData = table.getExportData();
                        var xlsxData = exportData.table.xlsx;
                    </script>
                </div>
                <div class="Space"></div>"""

    c3 = """
                        <tr>
                            <td class="tableexport-string target">&nbsp;@@d[{num1}][0]$$</td>
                            <td class="tableexport-string target">@@d[{num1}][10]$$</td>
                            <td class="tableexport-string target">@@d[{num1}][6]$$</td>
                            <td class="tableexport-string target">@@d[{num1}][3]$$ miles</td>
                            <td class="tableexport-string target">@@d[{num1}][4]$$</td>
                        </tr>"""

    c4 = ""

    s23 = ""
    num1 = 0
    num2 = 1

    for i in range(r):
        s23 += s22.format(num1=num1, num2=num2)
        num1 += 1
        num2 += 1

    s24 = s23.replace("@", "{").replace("$", "}")

    num1 = 0
    num2 = 1

    for i in range(r):
        c4 += c3.format(num1=num1, num2=num2)
        num1 += 1
        num2 += 1

    c5 = c4.replace("@", "{").replace("$", "}")

    c9 = """
        </body>
    </html>"""

    website = b1 + c5 + t0 + t2 + s24 + b2 + t1 + c9

    return website
