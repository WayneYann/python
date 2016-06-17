import matplotlib.pyplot as py

x = [1, 4, 5, 9, 7, 15, 27]

py.figure(1)
py.plot(x, lw=3)
py.grid()

ax = py.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
py.tick_params(bottom='off', top='off', left='off', right='off')

py.show()