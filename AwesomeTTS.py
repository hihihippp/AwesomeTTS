# -*- coding: utf-8 -*-

# AwesomeTTS text-to-speech add-on for Anki
#
# Copyright (C) 2010-2014  Anki AwesomeTTS Development Team
# Copyright (C) 2010-2013  Arthur Helfstein Fragoso
# Copyright (C) 2013-2014  Dave Shifflett
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Instructions on the AnkiWeb at <https://ankiweb.net/shared/info/301952613>.
# Problems or comments? Visit <https://github.com/AwesomeTTS/AwesomeTTS>.

"""
Entry point for AwesomeTTS add-on from Anki
"""

__all__ = []


if __name__ == "__main__":
    from sys import stderr

    stderr.write(
        "AwesomeTTS is a text-to-speech add-on for Anki.\n"
        "It is not intended to be run directly.\n"
        "To learn more or download Anki, please visit <http://ankisrs.net>.\n"
    )
    exit(1)


import awesometts.main  # imported for side effects, pylint: disable=W0611
