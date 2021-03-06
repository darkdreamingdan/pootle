#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Zuza Software Foundation
#
# This file is part of Pootle.
#
# translate is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# translate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with translate; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

from __future__ import absolute_import

# Python 2.5 (but not 2.6 or 2.7 - who knows about 3.x) gives the following
# "SyntaxError: 'import *' not allowed with 'from .'" with a relative import *
#from .fields import *
#from .filters import *
#from .widgets import *

# Preserve Python 2.5 compatibility for now
from pootle.core.markup.fields import *
from pootle.core.markup.filters import *
from pootle.core.markup.widgets import *
