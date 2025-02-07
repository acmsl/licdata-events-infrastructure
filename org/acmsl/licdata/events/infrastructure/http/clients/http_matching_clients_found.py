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
from org.acmsl.licdata.events.clients import (
    BaseClientEvent,
    ListClientsRequested,
    MatchingClientsFound,
)
from pythoneda.shared.infrastructure.http import HttpResponse
from typing import Dict, Type


class HttpMatchingClientsFound(HttpResponse):
    """
    HTTP interface for MatchingClientsFound

    Class name: HttpMatchingClientsFound

    Responsibilities:
        - Define the HTTP interface for the MatchingClientsFound event.

    Collaborators:
        - None
    """

    def __init__(
        self, responseEvent: MatchingClientsFound, sourceEvent: ListClientsRequested
    ):
        """
        Creates a new HttpMatchingClientsFound.
        :param responseEvent: The domain event, generated after a ListClientsRequested event.
        :type responseEvent: org.acmsl.licdata.events.clients.MatchingClientsFound
        :param sourceEvent: The initial list-clients-requested event.
        :type sourceEvent: org.acmsl.licdata.events.clients.ListClientsRequested
        """
        super().__init__(responseEvent=responseEvent, sourceEvent=sourceEvent)

    @property
    def status_code(self) -> int:
        """
        Retrieves the status code.
        :return: The status code.
        :type: int
        """
        if len(self._response_event.matching_clients) == 0:
            return 204
        else:
            return 200

    @property
    def body(self) -> Dict:
        """
        Retrieves the body.
        :return: The body.
        :type: Dict
        """
        if isinstance(self._source_event, BaseClientEvent):
            # TODO: Fix this
            result = {}
            result["clients"] = [c for c in self._response_event.matching_clients]
            criteria = {}
            if self._source_event.email is not None:
                criteria["email"] = self._source_event.email
            if self._source_event.address is not None:
                criteria["address"] = self._source_event.address
            if self._source_event.contact is not None:
                criteria["contact"] = self._source_event.contact
            if self._source_event.phone is not None:
                criteria["phone"] = self._source_event.phone
            result["criteria"] = criteria
        else:
            result = [c for c in self._response_event.matching_clients]
        import json

        return json.dumps(result)

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
