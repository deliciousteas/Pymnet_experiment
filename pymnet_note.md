# pymnet可视化笔记

## 源码

```python
import networkx as nx
import pymnet
from pymnet import *
import matplotlib.pyplot as plt  
from pymnet import MultilayerNetwork


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
```

![image-20241120112255170](C:\Users\22779\AppData\Roaming\Typora\typora-user-images\image-20241120112255170.png)

该函数使用 `Matplotlib` 或 `Three.js` 作为绘图后端，支持2D和3D的网络可视化。可能的后端包括：

其中threejs还是实验中，其中如果需要测试threejs，可能存在目录下缺少html文件

## 参数说明

### Layout（布局参数）

| 参数名         | 类型        | 默认值     | 说明                                                         |
| -------------- | ----------- | ---------- | ------------------------------------------------------------ |
| `layout`       | `str`       | `"spring"` | 布局算法，支持`"fr"`（Fruchterman-Reingold）、`"circular"`、`"shell"`等 |
| `alignedNodes` | `bool/None` | `None`     | 是否使每层中相同节点的坐标一致，默认`True`用于多层网络。     |
| `layergap`     | `float`     | `1.0`      | 层间的间距。                                                 |
| `autoscale`    | `bool`      | `True`     | 自动调整图像比例，使图形适应视图窗口。                       |

### Node（节点参数）

| 参数名             | 类型           | 默认值                 | 说明                                       |
| ------------------ | -------------- | ---------------------- | ------------------------------------------ |
| `nodeLabelDict`    | `dict`         | `{}`                   | 定义节点标签的字典。                       |
| `nodeLabelRule`    | `dict`         | `{"rule": "nodename"}` | 节点标签规则，可用`"nodename"`等生成标签。 |
| `defaultNodeLabel` | `str`/`None`   | `None`                 | 默认节点标签。                             |
| `nodeColorDict`    | `dict`         | `{}`                   | 节点颜色定义字典。                         |
| `nodeColorRule`    | `dict`         | `{}`                   | 节点颜色规则。                             |
| `defaultNodeColor` | `str`          | `"black"`              | 默认节点颜色。                             |
| `nodeSizeDict`     | `dict`         | `{}`                   | 节点大小定义字典。                         |
| `nodeSizeRule`     | `dict`         | `{"rule": "scaled"}`   | 节点大小规则，例如按度数缩放。             |
| `defaultNodeSize`  | `float`/`None` | `None`                 | 默认节点大小。                             |

### Edge（边参数）

| 参数名             | 类型    | 默认值                 | 说明                                       |
| ------------------ | ------- | ---------------------- | ------------------------------------------ |
| `edgeColorDict`    | `dict`  | `{}`                   | 边颜色定义字典。                           |
| `edgeColorRule`    | `dict`  | `{}`                   | 边颜色规则。                               |
| `defaultEdgeColor` | `str`   | `"gray"`               | 默认边颜色。                               |
| `edgeWidthDict`    | `dict`  | `{}`                   | 边宽度定义字典。                           |
| `edgeWidthRule`    | `dict`  | `{}`                   | 边宽度规则。                               |
| `defaultEdgeWidth` | `float` | `1.5`                  | 默认边宽度。                               |
| `edgeStyleDict`    | `dict`  | `{}`                   | 边样式定义字典。                           |
| `edgeStyleRule`    | `dict`  | `{"rule": "edgetype"}` | 边样式规则，支持`"intra"`和`"inter"`类型。 |
| `defaultEdgeStyle` | `str`   | `"-"`                  | 默认边样式。                               |

## 参数设置方法

可视化参数通过以下方法进行设置：

1. **直接定义**：通过`Dict`直接为特定元素分配值。
2. **规则生成**：通过`Rule`为元素应用规则动态生成值。
3. **默认值回退**：未定义属性时，回退到默认值`default[property]`。

例如，为层颜色设置属性时，可使用以下三种方式：

- `layerColorDict={"a": "red", "b": "blue"}` 直接定义。
- `layerColorRule={"rule": "name"}` 使用层名生成颜色。
- `defaultLayerColor="#29b7c1"` 设置默认值。

# 参考

[pymnet Visualizing networks](https://mnets.github.io/pymnet/autogen/pymnet.draw.html)