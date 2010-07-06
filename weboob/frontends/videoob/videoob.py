# -*- coding: utf-8 -*-


# Copyright(C) 2010  Christophe Benz, Romain Bignon
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.


from weboob.capabilities.video import ICapVideo
from weboob.tools.application import ConsoleApplication


__all__ = ['Videoob']


class Videoob(ConsoleApplication):
    APPNAME = 'videoob'
    VERSION = '0.1'
    COPYRIGHT = 'Copyright(C) 2010 Christophe Benz, Romain Bignon'
    CONFIG = {}

    def add_application_options(self, group):
        group.add_option('--nsfw', action='store_true', help='enable non-suitable for work videos')

    def main(self, argv):
        return self.process_command(*argv[1:])

    @ConsoleApplication.command('Get video information (accept ID or URL)')
    def command_info(self, _id):
        _id, backend_name = self.parse_id(_id)
        names = (backend_name,) if backend_name is not None else None
        self.load_modules(ICapVideo, names=names)
        for backend, video in self.weboob.do('get_video', _id):
            if video is None:
                continue
            self.format(video, backend.name)

    @ConsoleApplication.command('Search videos')
    def command_search(self, pattern=None):
        self.load_modules(ICapVideo)
        self.set_header(u'Search pattern: %s' % pattern if pattern else u'Last videos')
        for backend, video in self.weboob.do('iter_search_results', pattern=pattern, nsfw=self.options.nsfw):
            self.format(video, backend.name)
