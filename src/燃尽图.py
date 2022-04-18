# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

x = ["5月1日", "5月2日", "5月3日", "5月4日", "5月5日", "5月6日", "5月7日", "5月8日",
     "5月9日", "5月10日", "5月11日", "5月12日", "5月13日", "5月14日", "5月15日", "5月16日",
     "5月17日", "5月18日", "5月19日", "5月20日", "5月21日", "5月22日", "5月23日",
     "5月24日", "5月25日", "5月26日", "5月27日", "5月28日", "5月29日", "5月30日", "5月31日"]
y1 = np.arange(100, -1, -100. / (len(x) - 1))
y2 = [100, 99, 98, 98, 98, 98, 97, 97, 96, 96, 95, 95, 94, 94, 94,
      94, 93, 93, 92, 92, 91, 91, 90, 80, 70, 50, 30, 20, 10, 5, 0]

x_ticks = ["5月1日", "5月3日", "5月5日", "5月7日", "5月9日", "5月11日", "5月13日", "5月15日",
           "5月17日", "5月19日", "5月21日", "5月23日", "5月25日", "5月27日", "5月29日", "5月31日"]
y_ticks = np.arange(0, 101, 10)

plt.figure(figsize=(15, 6), dpi=100)

plt.title('燃尽图')

plt.xlabel('日期')
plt.ylabel('工作量')

plt.plot(x, y1, linewidth=5)
plt.plot(x, y2, linewidth=5)

plt.yticks(y_ticks)
plt.xticks(x_ticks, rotation=60)

plt.savefig("../images/line.png", dpi=100)
plt.show()
