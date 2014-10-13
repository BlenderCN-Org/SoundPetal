# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import numpy as np
from math import pi, sin, cos

import bpy
from bpy.props import EnumProperty, IntProperty, FloatProperty

from core.mechanisms import updateSD
from node_tree import FlowCustomTreeNode


TWO_PI = 2*pi


def make_geometry(node):
    m = np.arange(0, TWO_PI, TWO_PI/node.num_verts)
    g = np.array([[sin(x)*node.radius, cos(x)*node.radius, 0, 0] for x in m])
    return {0: {'verts': g}, }


class TrigUgen(bpy.types.Node, FlowCustomTreeNode):
    ''' TrigUgen '''
    bl_idname = 'TrigUgen'
    bl_label = 'Trig Ugen'
    bl_icon = 'OUTLINER_OB_EMPTY'

    num_verts = IntProperty(
        name='num_verts',
        min=2, step=1, default=2,
        update=updateSD)

    radius = FloatProperty(
        step=0.2, default=0.4,
        name="distance",
        update=updateSD)

    # axis = EnumProperty()

    def init(self, context):
        self.inputs.new("ScalarSocket", "num_verts").prop_name = "num_verts"
        self.inputs.new("ScalarSocket", "radius").prop_name = "radius"
        self.outputs.new('GeometrySocket', "send")

    def draw_buttons(self, context, layout):
        pass

    def process(self):
        gref = dict(objects=make_geometry(self))
        self.outputs[0].fset(gref)


def register():
    bpy.utils.register_class(TrigUgen)


def unregister():
    bpy.utils.unregister_class(TrigUgen)
