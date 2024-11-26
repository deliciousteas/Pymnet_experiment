import networkx as nx
import pymnet
from pymnet import *
import matplotlib.pyplot as plt  # 确保 matplotlib 使用的是 pyplot
from pymnet import MultilayerNetwork
# 创建多层网络，参数可以根据需要调整



# net_social = pymnet.MultiplexNetwork(couplings="categorical", fullyInterconnected=False)
# net_social["Alice", "Bob", "Friends"] = 1
# net_social["Alice", "Carol", "Friends"] = 1
# net_social["Bob", "Carol", "Friends"] = 1
# net_social["Alice", "Bob", "Married"] = 1
# # net_social["Carol",2,"Married"]=1
#
# pymnet.draw(net_social,layout='spring',show=True)
# plt.show()


# net=pymnet.MultilayerNetwork(aspects=1,fullyInterconnected=False)
# net.add_node(1,'a')
# net.add_node(10,'a')
# net.add_node(100,'a')
# net.add_node(2,'b')
# net.add_node(20,'b')
# net.add_node(200,'b')
# # net[1,2,'a']=1
# # net[20,30,'b']=1
# # net[1,20,'a','b']=1
# # net[1,2,'b']=1
# net[1,2,'a','b']=1



net = models.er_multilayer(5, 2, 0.2)




fig = draw(net,
           layout="circular",
           layershape="circle",
           nodeColorDict={(0,0):"r",  (0,1):"r",(2,1):'b'},
           layerLabelRule={},
           defaultLayerColor="silver",
           nodeLabelRule={"rule":"name"},
           nodeSizeRule={"rule":"degree", "propscale":0.05},
           # edgeColorRule={"rule":"edgeweight", "colormap":"viridis","scaleby":0.5},
           edgeColorRule={"rule":"edgetype","intra":"r","inter":"b"},
           )
plt.show()