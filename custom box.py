import matplotlib.pyplot as plt
import numpy as np


from matplotlib.path import Path

def custom_box_style(x0, y0, width, height, mutation_size):
    mypad = .5
    pad = mypad
# width and height with padding added. 
    width = width 
    height = height + 1 * mypad
# boundary of the padded box
    x0, y0 = x0 - pad, y0 - pad
    x1, y1 = x0 + width, y0 + height
# return the new path
    return Path([(x0, y0), (x1, y0), (x1, y1), (x0, y1),
                 (x0-pad, (y0+y1)/2), (x0, y0), (x0, y0)],
                closed=True)

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, .95, "Vela Dynamics LLC", size=5, va="center", ha="center", rotation=0,
        bbox=dict(boxstyle=custom_box_style, alpha=0.1))

plt.show()

