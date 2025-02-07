# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/http_matching_client_found.py

This file defines the HttpMatchingClientFound class.

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
from org.acmsl.licdata.events.clients import ListClientsRequested, MatchingClientFound
from pythoneda.shared.infrastructure.http import HttpResponse
from typing import Dict, Type


class HttpMatchingClientFound(HttpResponse):
    """
    HTTP interface for MatchingClientFound

    Class name: HttpMatchingClientFound

    Responsibilities:
        - Define the HTTP interface for the MatchingClientFound event.

    Collaborators:
        - None
    """

    def __init__(
        self, responseEvent: MatchingClientFound, sourceEvent: ListClientsRequested
    ):
        """
        Creates a new HttpMatchingClientFound.
        :param responseEvent: The domain event, generated after a ListClientsRequested event.
        :type responseEvent: org.acmsl.licdata.events.clients.MatchingClientFound
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
        return 200

    @property
    def body(self) -> Dict:
        """
        Retrieves the body.
        :return: The body.
        :type: Dict
        """
        import json

        return json.dumps(self.response_event.matching_client.to_dict())

    @property
    def headers(self) -> Dict:
        """
        Retrieves the headers.
        :return: The headers.
        :type: Dict
        """
        return {"Location": f"/clients/{self.response_event.matching_client.id}"}

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
    def event_class(cls) -> Type[MatchingClientFound]:
        """
        Retrieves the class of the event.
        :return: The class.
        :type: Type[org.acmsl.licdata.events.clients.MatchingClientFound]
        """
        return MatchingClientFound


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
