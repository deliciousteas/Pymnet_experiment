import networkx as nx
import pymnet
import matplotlib.pyplot as plt
import ifcopenshell
import pandas as pd

# 读取 IFC 文件
model = ifcopenshell.open("D:\\dzg\\090thesis\\091dataset\\shuinuan.ifc")

# 获取 IFC 构件列表
IfcPipeSegment_list = model.by_type("IfcPipeSegment")
IfcPipeFitting_list = model.by_type("IfcPipeFitting")

# 记录构件 ID
IfcPipeFitting_list = [i.id() for i in IfcPipeFitting_list]
IfcPipeSegment_list = [i.id() for i in IfcPipeSegment_list]

# 读取空间包含关系，保存为字典
IfcRelContainedInSpatialStructure_list = model.by_type("IfcRelContainedInSpatialStructure")
SpatialStrucutre_dic = {}
for rel in IfcRelContainedInSpatialStructure_list:
    RelatingStructure = rel.RelatingStructure.id()
    RelatedElements = [element.id() for element in rel.RelatedElements]
    SpatialStrucutre_dic[RelatingStructure] = RelatedElements


SpatialStrucutre_dic_value_list=list(SpatialStrucutre_dic.values())[0]
Storey_id1=list(SpatialStrucutre_dic.keys())[0]
Storey_id2=list(SpatialStrucutre_dic.keys())[1]
Storey_id1_list=SpatialStrucutre_dic.get(Storey_id1)
Storey_id2_list=SpatialStrucutre_dic.get(Storey_id2)

net=pymnet.MultilayerNetwork(aspects=1,fullyInterconnected=False)
for i in range(len(Storey_id1_list)):
    net.add_node(Storey_id1_list[i],str(Storey_id1))

for i in range(len(Storey_id2_list)):
    net.add_node(Storey_id2_list[i],str(Storey_id2))

data = pd.read_csv('D:/dzg/090thesis/092output/bnx_graph_mesh_all.csv')
csv_dict={}
index_num=data.index
for i in index_num:
    if data['ID1'][i] not in csv_dict:
        csv_dict[data['ID1'][i]]=[data['ID2'][i]]
    else:
        csv_dict[data['ID1'][i]].append(data['ID2'][i])

    if data['ID2'][i] not in csv_dict:
        csv_dict[data['ID2'][i]]=[data['ID1'][i]]
    else:
        csv_dict[data['ID2'][i]].append(data['ID1'][i])

# 添加边关系
for node1, neighbors in csv_dict.items():
    for node2 in neighbors:
        if node1 in Storey_id1_list and node2 in Storey_id1_list:
            net[node1, node2, str(Storey_id1)] = 1
        elif node1 in Storey_id2_list and node2 in Storey_id2_list:
            net[node1, node2, str(Storey_id2)] = 1
        elif node1 in Storey_id1_list and node2 in Storey_id2_list:
            net[node1, node2, str(Storey_id1), str(Storey_id2)] = 1
        elif node1 in Storey_id2_list and node2 in Storey_id1_list:
            net[node1, node2, str(Storey_id2), str(Storey_id1)] = 1

# 绘制网络
pymnet.draw(net,
            layout='spring',
            layershape='circle',
            elev=30,
            autoscale=True,
            defaultLayerColor="silver",
            nodeLabelRule={},
            nodeSizeRule={"rule":"degree", "propscale":0.05},
            defaultLayerLabelLoc=(0.9,0.9),
            #edgeColorRule={"rule":"edgeweight", "colormap":"viridis","scaleby":0.5},
            edgeColorRule={"rule":"edgetype","intra":"r","inter":"b"},
            show=True)
plt.show()


# #对边关系构建
# pymnet.draw(net,layout='spring',show=True)
# plt.show()

