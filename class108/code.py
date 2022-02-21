from multiprocessing import Barrier
import random
import plotly.express as px
import plotly.figure_factory as ff

count = []

dice_result = []
for i in range(1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)
    count.append(i)

print(count, dice_result)

#fig = px.bar(x = dice_result, y = count)
#fig.show()

fig = ff.create_distplot([dice_result], ["result"], show_hist= False)
fig.show()