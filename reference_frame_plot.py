#Copyright 2019 Delft Aerospace Rocket Engineering

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch

class Arrow3D(FancyArrowPatch):

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

fig = plt.figure()
ax = fig.gca(projection='3d')

x_axis = Arrow3D([0.5, 1], [0.5, 0.5], [0.5, 0.5], mutation_scale=20, 
                 lw=1, arrowstyle="-|>", color="r")
y_axis = Arrow3D([0.5, 0.5], [0.5, 1], [0.5, 0.5], 
                 mutation_scale=20, lw=1, arrowstyle="-|>", color="b")
z_axis = Arrow3D([0.5, 0.5], [0.5, 0.5], [0.5, 1], 
                 mutation_scale=20,lw=1, arrowstyle="-|>", color="g")

ax.add_artist(x_axis)
ax.add_artist(y_axis)
ax.add_artist(z_axis)
plt.show()



