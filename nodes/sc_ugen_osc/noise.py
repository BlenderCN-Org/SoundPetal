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

import bpy
from FLOW.node_tree import SoundPetalUgen


class UgenLFNoise0(SoundPetalUgen):
    ''' UgenLFNoise0 '''
    bl_idname = 'UgenLFNoise0'
    bl_label = 'LFNoise0'
    sp_args = "(freq: 500, mul: 1, add: 0)"
    sp_rate = SoundPetalUgen.sp_rate


class UgenLFNoise1(SoundPetalUgen):
    ''' UgenLFNoise1 '''
    bl_idname = 'UgenLFNoise1'
    bl_label = 'LFNoise1'
    sp_args = "(freq: 500, mul: 1, add: 0)"
    sp_rate = SoundPetalUgen.sp_rate


class UgenLFNoise2(SoundPetalUgen):
    ''' UgenLFNoise2 '''
    bl_idname = 'UgenLFNoise2'
    bl_label = 'LFNoise2'
    sp_args = "(freq: 500, mul: 1, add: 0)"
    sp_rate = SoundPetalUgen.sp_rate


def register():
    bpy.utils.register_class(UgenLFNoise0)
    bpy.utils.register_class(UgenLFNoise1)
    bpy.utils.register_class(UgenLFNoise2)


def unregister():
    bpy.utils.unregister_class(UgenLFNoise0)
    bpy.utils.unregister_class(UgenLFNoise1)
    bpy.utils.unregister_class(UgenLFNoise2)