import matplotlib.pyplot as plt  #그래프를 그리기 위한 matplotlib의 pyplot
import numpy as np

xpoints = np.array([0,6]) # x축에 사용할 데이터
ypoints = np.array([1,250]) # y축에 사용할 데이터

plt.plot(xpoints,ypoints) # xpoints와 ypoints를 연결하여 선 그래프 그
plt.show() # 그래프 출력


y2points = np.array([3,8,1,10]) # y축에 사용할 데이터를 배열로 생성

# o → 데이터 지점을 원형으로 표시
# : → 점선으로 연결
# r → 빨간색(red)
plt.plot(y2points, 'o:r')
plt.show()
