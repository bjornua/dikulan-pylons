import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from dikulan.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UserController(BaseController):
    def login(self):
        return render("/pages/login.mako")
    def register(self):
        return render("/pages/register.mako")