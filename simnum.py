import os
import json
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import jaccard_score

# 假設 all_attack_ids 列表已填充完整
all_attack_ids = ['T1001', 'T1003', 'T1005', 'T1006', 'T1007', 'T1008', 'T1010', 'T1011', 'T1012', 'T1014', 'T1016', 'T1018', 'T1020', 'T1021', 'T1025', 'T1026', 'T1027', 'T1029', 'T1030', 'T1033', 'T1034', 'T1036', 'T1037', 'T1039', 'T1040', 'T1041', 'T1043', 'T1046', 'T1047', 'T1048', 'T1049', 'T1051', 'T1052', 'T1053', 'T1055', 'T1056', 'T1057', 'T1059', 'T1061', 'T1062', 'T1064', 'T1068', 'T1069', 'T1070', 'T1071', 'T1072', 'T1074', 'T1078', 'T1080', 'T1082', 'T1083', 'T1087', 'T1090', 'T1091', 'T1092', 'T1095', 'T1098', 'T1102', 'T1104', 'T1105', 'T1106', 'T1108', 'T1110', 'T1111', 'T1112', 'T1113', 'T1114', 'T1115', 'T1119', 'T1120', 'T1123', 'T1124', 'T1125', 'T1127', 'T1129', 'T1132', 'T1133', 'T1134', 'T1135', 'T1136', 'T1137', 'T1140', 'T1149', 'T1153', 'T1175', 'T1176', 'T1185', 'T1187', 'T1189', 'T1190', 'T1195', 'T1197', 'T1199', 'T1200', 'T1201', 'T1202', 'T1203', 'T1204', 'T1205', 'T1207', 'T1210', 'T1211', 'T1212', 'T1213', 'T1216', 'T1217', 'T1218', 'T1219', 'T1220', 'T1221', 'T1222', 'T1224', 'T1225', 'T1226', 'T1227', 'T1228', 'T1229', 'T1230', 'T1231', 'T1232', 'T1233', 'T1234', 'T1235', 'T1236', 'T1237', 'T1238', 'T1239', 'T1240', 'T1241', 'T1242', 'T1243', 'T1244', 'T1245', 'T1246', 'T1247', 'T1248', 'T1249', 'T1250', 'T1251', 'T1252', 'T1253', 'T1254', 'T1255', 'T1256', 'T1257', 'T1258', 'T1259', 'T1260', 'T1261', 'T1262', 'T1263', 'T1264', 'T1265', 'T1266', 'T1267', 'T1268', 'T1269', 'T1270', 'T1271', 'T1272', 'T1273', 'T1274', 'T1275', 'T1276', 'T1277', 'T1278', 'T1279', 'T1280', 'T1281', 'T1282', 'T1283', 'T1284', 'T1285', 'T1286', 'T1287', 'T1288', 'T1289', 'T1290', 'T1291', 'T1292', 'T1293', 'T1294', 'T1295', 'T1296', 'T1297', 'T1298', 'T1299', 'T1300', 'T1301', 'T1302', 'T1303', 'T1304', 'T1305', 'T1306', 'T1307', 'T1308', 'T1309', 'T1310', 'T1311', 'T1312', 'T1313', 'T1314', 'T1315', 'T1316', 'T1317', 'T1318', 'T1319', 'T1320', 'T1321', 'T1322', 'T1323', 'T1324', 'T1325', 'T1326', 'T1327', 'T1328', 'T1329', 'T1330', 'T1331', 'T1332', 'T1333', 'T1334', 'T1335', 'T1336', 'T1337', 'T1338', 'T1339', 'T1340', 'T1341', 'T1342', 'T1343', 'T1344', 'T1345', 'T1346', 'T1347', 'T1348', 'T1349', 'T1350', 'T1351', 'T1352', 'T1353', 'T1354', 'T1355', 'T1356', 'T1357', 'T1358', 'T1359', 'T1360', 'T1361', 'T1362', 'T1363', 'T1364', 'T1365', 'T1366', 'T1367', 'T1368', 'T1369', 'T1370', 'T1371', 'T1372', 'T1373', 'T1374', 'T1375', 'T1376', 'T1377', 'T1378', 'T1379', 'T1380', 'T1381', 'T1382', 'T1383', 'T1384', 'T1385', 'T1386', 'T1387', 'T1388', 'T1389', 'T1390', 'T1391', 'T1392', 'T1393', 'T1394', 'T1395', 'T1396', 'T1397', 'T1398', 'T1399', 'T1403', 'T1404', 'T1405', 'T1406', 'T1407', 'T1409', 'T1413', 'T1414', 'T1417', 'T1418', 'T1420', 'T1421', 'T1422', 'T1423', 'T1424', 'T1426', 'T1427', 'T1428', 'T1429', 'T1430', 'T1436', 'T1437', 'T1444', 'T1449', 'T1451', 'T1453', 'T1456', 'T1458', 'T1461', 'T1464', 'T1469', 'T1470', 'T1471', 'T1474', 'T1475', 'T1476', 'T1477', 'T1480', 'T1481', 'T1482', 'T1484', 'T1485', 'T1486', 'T1489', 'T1490', 'T1491', 'T1495', 'T1496', 'T1497', 'T1498', 'T1499', 'T1505', 'T1509', 'T1512', 'T1513', 'T1516', 'T1517', 'T1518', 'T1521', 'T1525', 'T1526', 'T1528', 'T1529', 'T1530', 'T1531', 'T1532', 'T1533', 'T1534', 'T1535', 'T1537', 'T1538', 'T1539', 'T1541', 'T1542', 'T1543', 'T1544', 'T1546', 'T1547', 'T1548', 'T1550', 'T1552', 'T1553', 'T1554', 'T1555', 'T1556', 'T1557', 'T1558', 'T1559', 'T1560', 'T1561', 'T1562', 'T1563', 'T1564', 'T1565', 'T1566', 'T1567', 'T1568', 'T1569', 'T1570', 'T1571', 'T1572', 'T1573', 'T1574', 'T1575', 'T1577', 'T1578', 'T1580', 'T1582', 'T1583', 'T1584', 'T1585', 'T1586', 'T1587', 'T1588', 'T1589', 'T1590', 'T1591', 'T1592', 'T1593', 'T1594', 'T1595', 'T1596', 'T1597', 'T1598', 'T1599', 'T1600', 'T1601', 'T1602', 'T1603', 'T1604', 'T1606', 'T1608', 'T1609', 'T1610', 'T1611', 'T1612', 'T1613', 'T1614', 'T1615', 'T1616', 'T1617', 'T1619', 'T1620', 'T1621', 'T1622', 'T1623', 'T1624', 'T1625', 'T1626', 'T1627', 'T1628', 'T1629', 'T1630', 'T1631', 'T1632', 'T1633', 'T1634', 'T1635', 'T1636', 'T1637', 'T1638', 'T1639', 'T1640', 'T1641', 'T1642', 'T1643', 'T1644', 'T1645', 'T1646', 'T1647', 'T1648', 'T1649', 'T1650', 'T1651', 'T1652', 'T1653', 'T1654', 'T1655', 'T1656', 'T1657', 'T1658', 'T1659', 'T1660', 'T1661', 'T1662', 'T1663', 'T1664', 'T1665']

MBC = ['C0011', 'C0004', 'C0002', 'C0014', 'C0003', 'C0012', 'C0001', 'C0005', 'C0068', 'C0069', 'C0059', 'C0027', 'C0031', 'C0021', 'C0029', 'C0028', 'C0061', 'C0019', 'C0032', 'C0024', 'C0060', 'C0025', 'C0026', 'C0053', 'C0058', 'C0030', 'C0020', 'C0016', 'C0045', 'C0046', 'C0016', 'C0048', 'C0047', 'C0049', 'C0063', 'C0051', 'C0056', 'C0050', 'C0052', 'C0037', 'C0023', 'C0057', 'C0007', 'C0008', 'C0044', 'C0006', 'C0010', 'C0009', 'C0040', 'C0042', 'C0043', 'C0017', 'C0038', 'C0064', 'C0065', 'C0066', 'C0054', 'C0072', 'C0041', 'C0055', 'C0022', 'C0018', 'C0039', 'C0070', 'C0071', 'C0033', 'C0034', 'C0036', 'C0035']

def filter_files_by_size(folder, min_size_kb):
    return [file for file in os.listdir(folder) if os.path.getsize(os.path.join(folder, file)) >= min_size_kb * 1024]

def convert_reports_to_binary(report_folder, output_folder, all_attack_ids, MBC, min_size_kb=3):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for report_file in os.listdir(report_folder):
        if report_file.endswith('.txt') and os.path.getsize(os.path.join(report_folder, report_file)) >= min_size_kb * 1024:
            report_path = os.path.join(report_folder, report_file)
            output_path = os.path.join(output_folder, f"{os.path.splitext(report_file)[0]}_binary.json")
            
            attack_array = [0] * len(all_attack_ids)
            MBC_array = [0] * len(MBC)
            
            with open(report_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    for attack_id in all_attack_ids:
                        if attack_id in line:
                            index = all_attack_ids.index(attack_id)
                            attack_array[index] = 1
                    for MBC_id in MBC:
                        if MBC_id in line:
                            index = MBC.index(MBC_id)
                            MBC_array[index] = 1
            
            with open(output_path, 'w', encoding='utf-8') as json_file:
                json.dump({'attack_ids': attack_array, 'MBC': MBC_array}, json_file, indent=4, ensure_ascii=False)
                print(f"已將 {report_file} 轉換為二進制格式 JSON。")

def clear_directory(folder):
    if os.path.exists(folder):
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

# 設定你的報告目錄和二進制輸出目錄
types = ['wannacry']
report_folders = [f'./report/{type}' for type in types]
binary_folders = [f'./binary_reports/{type}' for type in types]

# 清空目錄
for binary_folder in binary_folders:
    clear_directory(binary_folder)

# 轉換所有報告文件為二進制格式 JSON
for report_folder, binary_folder in zip(report_folders, binary_folders):
    convert_reports_to_binary(report_folder, binary_folder, all_attack_ids, MBC)

# 提取特徵
def extract_binary_features(binary_folders):
    features = {}
    for binary_folder in binary_folders:
        json_files = filter_files_by_size(binary_folder, 3)
        for json_file in json_files:
            if json_file.endswith('.json'):
                with open(os.path.join(binary_folder, json_file), 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    sample_id = json_file.split('_')[0]
                    features[sample_id] = data['attack_ids'] + data['MBC']
    return features

# 提取特徵
features = extract_binary_features(binary_folders)
print("提取的特徵:")
for sample_id, feature in features.items():
    print(f"{sample_id}: {feature[:10]}...")  # 只印出前10個元素

# 計算相似度
def calculate_similarity_jaccard(features):
    sample_ids = list(features.keys())
    vectors = np.array(list(features.values()))

    jaccard_matrix = np.zeros((len(sample_ids), len(sample_ids)))
    for i in range(len(sample_ids)):
        for j in range(len(sample_ids)):
            if i != j:
                jaccard_matrix[i][j] = jaccard_score(vectors[i], vectors[j])
            else:
                jaccard_matrix[i][j] = 1.0  # 自身比較設為1

    similarity_dict = {}
    for i, sample_id in enumerate(sample_ids):
        similarity_dict[sample_id] = {}
        for j, other_sample_id in enumerate(sample_ids):
            similarity_dict[sample_id][other_sample_id] = jaccard_matrix[i][j]
    return similarity_dict

# 計算相似度
similarity = calculate_similarity_jaccard(features)

# 視覺化相似度
def visualize_similarity(similarity):
    sample_ids = list(similarity.keys())
    data = pd.DataFrame(similarity).fillna(0)
    sns.heatmap(data, xticklabels=sample_ids, yticklabels=sample_ids, cmap="YlGnBu", annot=True, fmt=".2f")
    plt.title('Sample Similarity Heatmap')
    plt.show()


# 視覺化相似度
visualize_similarity(similarity)

# 生成報告
def generate_report(similarity, output_file='report.txt'):
    with open(output_file, 'w', encoding='utf-8') as file:
        for sample_id, similar_samples in similarity.items():
            file.write(f"Sample ID: {sample_id}\n")
            file.write("Similar Samples:\n")
            for other_sample_id, sim_score in sorted(similar_samples.items(), key=lambda item: item[1], reverse=True):  # 降冪排序
                file.write(f"\t{other_sample_id}: {sim_score:.2f}\n")
            file.write("\n")

# 生成報告
generate_report(similarity)
