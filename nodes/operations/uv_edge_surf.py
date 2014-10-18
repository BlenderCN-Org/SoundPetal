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
from math import pi, sqrt, e

import bpy
from bpy.props import IntProperty, BoolProperty, EnumProperty

from FLOW.core.mechanisms import updateSD
from FLOW.node_tree import FlowCustomTreeNode


class FlowUVEdgeSurf(bpy.types.Node, FlowCustomTreeNode):
    '''
    FlowUVEdgeSurf
    ==================

    UV EdgeSurf takes an argument for number of verts in U and V,
    combined with two booleans to elect to make the surfaces or edgenet
    cyclic in U and/or V.

    '''
    bl_idname = 'FlowUVEdgeSurf'
    bl_label = 'UV EdgeSurf'
    bl_icon = 'OUTLINER_OB_EMPTY'

    num_poly = IntProperty(default=6, min=1, update=updateSD)
    modulo_verts = IntProperty(name='modulo_verts', min=0, step=1, update=updateSD)
    cycle_u = IntProperty(name='cycle_u', min=0, max=1, update=updateSD)
    cycle_v = IntProperty(name='cycle_v', min=0, max=1, update=updateSD)

    topo_options = [
        ("EDGES", "Edges", "", 0),
        ("FACES", "Faces", "", 1),
    ]

    edgesurf = EnumProperty(
        items=topo_options,
        name="Type of topology",
        description="offers choice to make edges or faces",
        default="EDGES",
        update=updateSD)

    def init(self, context):
        self.inputs.new('ArraySocket', "verts")
        self.inputs.new('ScalarSocket', "modulo_verts").prop_name = 'modulo_verts'
        self.inputs.new('ScalarSocket', "cycle u").prop_name = 'cycle_u'
        self.inputs.new('ScalarSocket', "cycle v").prop_name = 'cycle_v'
        self.inputs.new('ScalarSocket', "num_poly").prop_name = 'num_poly'
        self.outputs.new('ArraySocket', 'topology')

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.prop(self, 'edgesurf', expand=True)

    def process(self):
        v = self.inputs['verts'].fget()
        modulo_verts = self.inputs['modulo_verts'].fget(fallback=self.modulo_verts, direct=True)

        ## fix this soon.
        if isinstance(modulo_verts, (list,)):
            if len(modulo_verts) == 1:
                modulo_verts = modulo_verts[0]

        if not v.any():
            return

        if not (len(v.shape) == 2):
            return

        x, _ = v.shape
        y = x // modulo_verts

        # dv = 0 if self.cycle_u == 1 else 1
        # dr = 0 if self.cycle_v == 1 else 1
        

        # p = [(i, i+1, i+y, i+y-1) for i in range(self.num_poly)]
        # p += [[(i*(y-1)), ((i+1)*(y-1)), ((i+2)*(y-1)-1), ((i+1)*(y-1))-1] for i in range(y-dr)]
        # val = np.array(p)
        # print(val)
        # self.outputs[0].fset(val)
        print('xy: {x},{y}:'.format(x=x, y=y))


def register():
    bpy.utils.register_class(FlowUVEdgeSurf)


def unregister():
    bpy.utils.unregister_class(FlowUVEdgeSurf)
