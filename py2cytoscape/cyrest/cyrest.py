from .base import *
from .commands import *
from .command import *
from .cybrowser import *
from .session import *
from .network import *
from .node import *
from .vizmap import *
from .diffusion import *
from .idmapper import *
from .edge import *
from .group import *

import copy

class cyclient(object):
    """
    A CyREST client.

    :param host: CyREST host server address. default='localhost'
    :param port: CyREST port number. default=1234
    :param version: CyREST version. default='v1'

    returns: a cyclient object.
    """

    def __init__(self, host=HOST, port=PORT, version=VERSION):
        self.__url = 'http://' + host + ':' + str(port) + '/' + version + '/'
        self.commands=commands(self.__url)
        self.command=command(self.__url)
        self.cybrowser=cybrowser(self.__url)
        self.session=session(self.__url)
        self.network=network(self.__url)
        self.node=node(sefl.__url)
        self.vizmap=vizmap(sel.__url)
        self.diffusion(sel.__url)
        self.edge(sel.__url)
        self.group(sel.__url)

    def status(self):
        """
        Checks the status of your CyREST server.
        """
        try:
            response=api(url=self.__url,method="GET")
        except Exception as e:
            print('Could not get status from CyREST: ' + str(e))
        else:
            print('CyREST online!')

    def copy(self):
        """
        Creates a copy of the cyclient object.
        """
        return copy.deepcopy(self)
