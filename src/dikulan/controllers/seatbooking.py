import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from dikulan.lib.base import BaseController, render

from dikulan.model.seatbooking import seatbooking
import sqlite3

log = logging.getLogger(__name__)

class SeatbookingController(BaseController):
    def index(self):
        return render("/pages/seatbooking.mako")

    def statusimage(self): 
        db = sqlite3.connect("data/database.sqlite")
        return seatbooking.get_statusimage(db)

