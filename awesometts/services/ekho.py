# -*- coding: utf-8 -*-

# AwesomeTTS text-to-speech add-on for Anki
#
# Copyright (C) 2010-2014  Anki AwesomeTTS Development Team
# Copyright (C) 2010-2012  Arthur Helfstein Fragoso
# Copyright (C) 2014       Dave Shifflett
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

"""
Service implementation for Ekho text-to-speech engine
"""

__all__ = ['TTS_service']

from os import unlink
import re
from subprocess import check_output, Popen
from awesometts import conf
from awesometts.paths import media_filename
from awesometts.util import STARTUP_INFO, TO_TOKENS


BINARY = 'ekho'
VOICES = None

RE_LIST = re.compile(r'(language|voice).+available', re.IGNORECASE)
RE_VOICE = re.compile(r"'(\w+)'")

def _get_voices():
    voices = sorted({
        (capture, capture)

        for line
        in check_output([BINARY, '--help']).split('\n')
        if RE_LIST.search(line)

        for capture
        in RE_VOICE.findall(line)
    })

    if not voices:
        raise EnvironmentError("No usable output from `ekho --help`")

    return voices

try:
    try:
        VOICES = _get_voices()

    except OSError as os_error:
        from errno import ENOENT

        if os_error.errno != ENOENT:
            raise os_error

except:  # allow recovery from any exception, pylint:disable=W0702
    from sys import stderr
    from traceback import format_exc

    stderr.write(
        "Although you appear to have Ekho, the voice list from the CLI "
        "utility could not be retrieved. Any cards using `ekho` might not "
        "be speakable during this session. If this persists, please open "
        "an issue at <https://github.com/AwesomeTTS/AwesomeTTS/issues>.\n"
        "\n" +
        format_exc()
    )


if VOICES:
    SERVICE = 'ekho'

    def play(text, voice):
        Popen(
            [BINARY, '-v', voice, text],
            startupinfo=STARTUP_INFO,
        ).wait()

    def record(text, voice):
        filename_wav = media_filename(text, SERVICE, voice, 'wav')
        filename_mp3 = media_filename(text, SERVICE, voice, 'mp3')

        Popen(
            [BINARY, '-v', voice, '-t', 'wav', '-o', filename_wav, text],
            startupinfo=STARTUP_INFO,
        ).wait()

        Popen(
            ['lame'] +
            TO_TOKENS(conf.lame_flags) +
            [filename_wav, filename_mp3],
            startupinfo=STARTUP_INFO,
        ).wait()

        unlink(filename_wav)

        return filename_mp3


    TTS_service = {SERVICE: {
        'name': "Ekho",
        'play': play,
        'record': record,
        'voices': VOICES,
    }}
