# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/http_matching_clients_found.py

This file defines the HttpMatchingClientsFound class.

Copyright (C) 2024-today acmsl's Licdata-Events-Infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from org.acmsl.licdata.events.clients import ListClientsRequested, MatchingClientsFound
from pythoneda.shared import Event
from typing import Dict, Type


class HttpMatchingClientsFound(Event):
    """
    HTTP interface for MatchingClientsFound

    Class name: HttpMatchingClientsFound

    Responsibilities:
        - Define the HTTP interface for the MatchingClientsFound event.

    Collaborators:
        - None
    """

    def __init__(self, event: Event, sourceEvent: ListClientsRequested):
        """
        Creates a new HttpMatchingClientsFound.
        :param event: The domain event, generated after a ListClientsRequested event.
        :type event: pythoneda.shared.Event
        :param sourceEvent: The initial list-clients-requested event.
        :type sourceEvent: org.acmsl.licdata.events.clients.ListClientsRequested
        """
        self._event = event
        self._source_event = sourceEvent
        super().__init__()

    @property
    def event(self) -> Event:
        """
        Retrieves the event.
        :return: The event.
        :type: pythoneda.shared.Event
        """
        return self._event

    @property
    def source_event(self) -> ListClientsRequested:
        """
        Retrieves the source event.
        :return: The source event.
        :type: org.acmsl.licdata.events.clients.ListClientsRequested
        """
        return self._source_event

    @property
    def status_code(self) -> int:
        """
        Retrieves the status code.
        :return: The status code.
        :type: int
        """
        return 200

    @property
    def body(self) -> Dict:
        """
        Retrieves the body.
        :return: The body.
        :type: Dict
        """
        import json

        return json.dumps(
            {
                "clients": [c for c in self._event.matching_clients],
                "criteria": self._event.criteria,
            }
        )

    @property
    def headers(self) -> Dict:
        """
        Retrieves the headers.
        :return: The headers.
        :type: Dict
        """
        return {}

    @property
    def mime_type(self) -> str:
        """
        Retrieves the MIME type.
        :return: The MIME type.
        :type: str
        """
        return "application/json"

    @property
    def charset(self) -> str:
        """
        Retrieves the charset.
        :return: The charset.
        :type: str
        """
        return "utf-8"

    @classmethod
    def event_class(cls) -> Type[MatchingClientsFound]:
        """
        Retrieves the class of the event.
        :return: The class.
        :type: Type[org.acmsl.licdata.events.clients.MatchingClientsFound]
        """
        return MatchingClientsFound


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
