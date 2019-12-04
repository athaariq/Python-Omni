import os
## --------------------------------------
class Config(object):
    @property
    def OMNI_USER_PATH(self):
        return (os.path.join(os.environ['APPDATA'], 'Omni Automated Query File'))
    ## --
