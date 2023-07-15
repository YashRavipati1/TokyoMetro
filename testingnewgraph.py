import networkx as nx
import matplotlib.pyplot as plt
import json
import random

with open("clean_stations.json") as f:
    data = json.load(f)

with open("secondary.json", "r") as file:
    names = json.load(file)

graph = nx.Graph()
positions = {
    "A01": [206, 1550, "Red"],
    "A02": [325, 1550, "Red"],
    "A03": [455, 1550, "Red"],
    "A04": [570, 1550, "Red"],
    "A05": [685, 1550, "Red"],
    "A06": [832, 1550, "Red"],
    "A07": [972, 1550, "Red"],
    "A08": [1153, 1550, "Red"],
    "A09": [1475, 1434, "Red"],
    "A10": [1598, 1350, "Red"],
    "A11": [1800, 1193, "Red"],
    "A12": [1800, 1020, "Red"],
    "A13": [1800, 950, "Red"],
    "A14": [1800, 820, "Red"],
    "A15": [1800, 725, "Red"],
    "A16": [1800, 608, "Red"],
    "A17": [1800, 490, "Red"],
    "A18": [1908, 380, "Red"],
    "A19": [1950, 325, "Red"],
    "A20": [2009, 280, "Red"],
    "C01": [365, 1110, "Green"],
    "C02": [408, 1110, "Green"],
    "C03": [620, 1110, "Green"],
    "C04": [823, 1230, "Green"],
    "C05": [915, 1230, "Green"],
    "C06": [1037, 1230, "Green"],
    "C07": [1225, 1230, "Green"],
    "C08": [1360, 1230, "Green"],
    "C09": [1526, 1185, "Green"],
    "C10": [1397, 1010, "Green"],
    "C11": [1397, 941, "Green"],
    "C12": [1397, 725, "Green"],
    "C13": [1397, 525, "Green"],
    "C14": [1397, 420, "Green"],
    "C15": [1397, 335, "Green"],
    "C16": [1397, 230, "Green"],
    "C17": [1550, 120, "Green"],
    "C18": [1910, 120, "Green"],
    "C19": [2092, 120, "Green"],
    "C20": [2160, 72, "Green"],
    "E01": [543, 824, "Magenta"],
    "E02": [650, 715, "Magenta"],
    "E03": [783, 676, "Magenta"],
    "E04": [875, 676, "Magenta"],
    "E05": [964, 676, "Magenta"],
    "E06": [1117, 664, "Magenta"],
    "E07": [1231, 489, "Magenta"],
    "E08": [1321, 489, "Magenta"],
    "E09": [1563, 489, "Magenta"],
    "E10": [1712, 489, "Magenta"],
    "E11": [1831, 489, "Magenta"],
    "E12": [1962, 589, "Magenta"],
    "E13": [1998, 726, "Magenta"],
    "E14": [1998, 822, "Magenta"],
    "E15": [1997, 950, "Magenta"],
    "E16": [1997, 1124, "Magenta"],
    "E17": [1949, 1259, "Magenta"],
    "E18": [1868, 1346, "Magenta"],
    "E19": [1624, 1432, "Magenta"],
    "E20": [1506, 1434, "Magenta"],
    "E21": [1218, 1429, "Magenta"],
    "E22": [1059, 1429, "Magenta"],
    "E23": [955, 1320, "Magenta"],
    "E24": [901, 1042, "Magenta"],
    "E25": [742, 1011, "Magenta"],
    "E26": [576, 1013, "Magenta"],
    "E27": [577, 920, "Magenta"],
    "E28": [467, 883, "Magenta"],
    "E29": [394, 886, "Magenta"],
    "E30": [394, 822, "Magenta"],
    "E31": [392, 680, "Magenta"],
    "E32": [362, 548, "Magenta"],
    "E33": [305, 507, "Magenta"],
    "E34": [269, 471, "Magenta"],
    "E35": [222, 423, "Magenta"],
    "E36": [170, 379, "Magenta"],
    "E37": [130, 335, "Magenta"],
    "E38": [93, 299, "Magenta"],
    "Y01": [108, 220, "Gold"],
    "Y02": [178, 220, "Gold"],
    "Y03": [251, 220, "Gold"],
    "Y04": [316, 220, "Gold"],
    "Y05": [389, 220, "Gold"],
    "Y06": [458, 235, "Gold"],
    "Y07": [525, 304, "Gold"],
    "Y08": [591, 367, "Gold"],
    "Y09": [660, 419, "Gold"],
    "Y10": [754, 486, "Gold"],
    "Y11": [879, 486, "Gold"],
    "Y12": [991, 516, "Gold"],
    "Y13": [1129, 667, "Gold"],
    "Y14": [1022, 784, "Gold"],
    "Y15": [1048, 900, "Gold"],
    "Y16": [1143, 992, "Gold"],
    "Y17": [1341, 1129, "Gold"],
    "Y18": [1526, 1185, "Gold"],
    "Y19": [1700, 1129, "Gold"],
    "Y20": [1832, 1129, "Gold"],
    "Y21": [2001, 1129, "Gold"],
    "Y22": [2100, 1129, "Gold"],
    "Y23": [2195, 1129, "Gold"],
    "Y24": [2300, 1129, "Gold"],
    "I01": [574, 1425, "Blue"],
    "I02": [730, 1425, "Blue"],
    "I03": [890, 1425, "Blue"],
    "I04": [1153, 1550, "Blue"],
    "I05": [1321, 1490, "Blue"],
    "I06": [1432, 1379, "Blue"],
    "I07": [1498, 1291, "Blue"],
    "I08": [1526, 1185, "Blue"],
    "I09": [1397, 941, "Blue"],
    "I10": [1270, 725, "Blue"],
    "I11": [1270, 615, "Blue"],
    "I12": [1201, 488, "Blue"],
    "I13": [1104, 391, "Blue"],
    "I14": [1054, 338, "Blue"],
    "I15": [1004, 280, "Blue"],
    "I16": [923, 236, "Blue"],
    "I17": [772, 236, "Blue"],
    "I18": [708, 236, "Blue"],
    "I19": [641, 206, "Blue"],
    "I20": [591, 157, "Blue"],
    "I21": [548, 112, "Blue"],
    "I22": [474, 61, "Blue"],
    "I23": [413, 61, "Blue"],
    "I24": [350, 61, "Blue"],
    "I25": [290, 61, "Blue"],
    "I26": [230, 61, "Blue"],
    "I27": [170, 61, "Blue"],
    "T01": [274, 590, "Sky"],
    "T02": [442, 590, "Sky"],
    "T03": [589, 590, "Sky"],
    "T04": [820, 590, "Sky"],
    "T05": [935, 590, "Sky"],
    "T06": [1129, 667, "Sky"],
    "T07": [1253, 844, "Sky"],
    "T08": [1305, 904, "Sky"],
    "T09": [1397, 941, "Sky"],
    "T10": [1800, 950, "Sky"],
    "T11": [1906, 952, "Sky"],
    "T12": [2013, 952, "Sky"],
    "T13": [2018, 952, "Sky"],
    "T14": [2112, 917, "Sky"],
    "T15": [2141, 887, "Sky"],
    "T16": [2176, 854, "Sky"],
    "T17": [2206, 825, "Sky"],
    "T18": [2240, 795, "Sky"],
    "T19": [2273, 764, "Sky"],
    "T20": [2303, 724, "Sky"],
    "T21": [2338, 695, "Sky"],
    "T22": [2367, 661, "Sky"],
    "T23": [2407, 612, "Sky"],
}
# When getting pixel coords, need to subtact y coord from 1785 (height of image) to get correct coords (otherwise flipped)
for i in positions:
    positions[i][1] = 1785 - positions[i][1]

for node, neighbors in data.items():
    if "A" not in node and "C" not in node and "Y" not in node and "I" not in node and "T" not in node:
        continue
    graph.add_node(node, pos=(positions[node][0], positions[node][1]))
    for neighbor, weight in neighbors.items():
        if "A" in neighbor or "C" in neighbor or "Y" in neighbor or "I" in neighbor or "T" in neighbor:
            graph.add_edge(node, neighbor, weight=weight)

nodes = graph.nodes(data=True)
edges = graph.edges(data=True)
path = ["A01", "A02", "A03"]
color_map_nodes = []
color_map_edges = []
for edge in edges:
    if edge[0] and edge[1] in path:
        color_map_edges.append("orange")
    else:
        color_map_edges.append("0.5")
for node in graph:
    if node in path:
        color_map_nodes.append("orange")
    else:
        color_map_nodes.append("0.5")
pos = {node: attr["pos"] for node, attr in nodes}
names = {key: value for key, value in names.items() if key in nodes and key in path}
nx.draw_networkx(
    graph,
    pos=pos,
    node_size=50,
    labels=names,
    node_color=color_map_nodes,
    edge_color=color_map_edges,
    with_labels=False,
    font_size=8,
)
plt.show()
