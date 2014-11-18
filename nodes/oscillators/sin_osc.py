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


class UgenSinOsc(SoundPetalUgen):
    ''' UgenSinOsc '''
    bl_idname = 'UgenSinOsc'
    bl_label = 'SinOsc'
    sp_args = "(freq: 440, phase: 0, mul: 1, add: 0)"
    sp_rate = SoundPetalUgen.sp_rate
    modifiers = SoundPetalUgen.modifiers
    modifier_type = SoundPetalUgen.modifier_type


class UgenFSinOsc(SoundPetalUgen):
    ''' UgenFSinOsc '''
    bl_idname = 'UgenFSinOsc'
    bl_label = 'FSinOsc'
    sp_args = "(freq: 440, iphase: 0, mul: 1, add: 0)"
    sp_rate = SoundPetalUgen.sp_rate
    modifiers = SoundPetalUgen.modifiers
    modifier_type = SoundPetalUgen.modifier_type


class UgenSinOscFB(SoundPetalUgen):
    ''' UgenSinOscFB '''
    bl_idname = 'UgenSinOscFB'
    bl_label = 'SinOscFB'
    sp_args = "(freq: 440, feedback: 0, mul: 1, add: 0)"
    sp_rate = SoundPetalUgen.sp_rate
    modifiers = SoundPetalUgen.modifiers
    modifier_type = SoundPetalUgen.modifier_type


def register():
    bpy.utils.register_class(UgenSinOsc)
    bpy.utils.register_class(UgenFSinOsc)
    bpy.utils.register_class(UgenSinOscFB)


def unregister():
    bpy.utils.unregister_class(UgenSinOsc)
    bpy.utils.unregister_class(UgenFSinOsc)
    bpy.utils.unregister_class(UgenSinOscFB)
