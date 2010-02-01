"""Setup the dikulan application"""
import logging, os, sqlite3

from dikulan.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup dikulan here"""
    load_environment(conf.global_conf, conf.local_conf)
    log.debug("Setting up application.")    
    
    
    
    log.debug("Done setting up application.")
