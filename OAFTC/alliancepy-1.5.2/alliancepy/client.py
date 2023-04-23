import sys

from alliancepy.cache import Cache
from alliancepy.team import Team
from alliancepy.http import request
import logging

# MIT License
#
# Copyright (c) 2020 Yash Karandikar
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

logger = logging.getLogger(__name__)


class Client:
    """
    This is the main client class used for accessing the TOA API. Currently, it only serves up :class:`~.team.Team`
    objects but it will
    expand over time.

    Args:
        api_key (str): Your TOA API key. This is required, otherwise you will not be able to access the database.
        application_name (str): The name of your application. It can just be the name of your script. Defaults to \
        ``sys.argv[0]``
    """

    def __init__(self, api_key: str, application_name: str = None):
        application_name = application_name or sys.argv[0]
        cache = Cache()
        self._headers = {
            "content-type": "application/json",
            "x-toa-key": api_key,
            "x-application-origin": application_name,
        }
        logger.info("Initialized Client object")

    def team(self, team_number: int):
        """Create a :class:`~.team.Team` object.

        Args:
            team_number (int): A valid First Tech Challenge team number.
        Return:
            :class:`~team.Team`: The Team object.
        """
        logger.info(f"Got request for team with team number of {team_number}")
        return Team(team_number=team_number, headers=self._headers)

    @property
    def api_version(self):
        """The version of the API that is currently in use.

        :rtype: int
        """
        data = request("/", headers=self._headers)
        return data["version"]

    def clear_cache(self):
        """Clears the cache. This is useful for long-running applications when the cache gets too big."""
        request("clear", headers=self._headers)
