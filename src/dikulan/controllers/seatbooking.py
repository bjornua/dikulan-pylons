import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from dikulan.lib.base import BaseController, render

from dikulan.model.seatbooking import seatbooking

log = logging.getLogger(__name__)

class SeatbookingController(BaseController):
    def index(self):
        return render("/pages/seatbooking.mako")

    def statusimage(self):
        return "Temporarily out of action!"
        return seatbooking.get_statusimage(db)

