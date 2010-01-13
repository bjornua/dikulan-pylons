"""Setup the dikulan application"""
import logging, os, sqlite3

from dikulan.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup dikulan here"""
    load_environment(conf.global_conf, conf.local_conf)
    
    if not os.path.exists("data/database.sqlite"):
        log.debug("No database-file present, create new database-file.")
        os.makedirs("data")
        db = sqlite3.connect("data/database.sqlite")
        c = db.cursor()
        
        log.debug("Creating reserved_seats table.")
        c.execute("""
            CREATE TABLE "reserved_seats" (
                "id" INTEGER PRIMARY KEY
            );
        """)
        log.debug("Done creating database.")
        
    else:
        log.debug("It did. Will not touch it then.")
    
    log.debug("Done setting up application.")
