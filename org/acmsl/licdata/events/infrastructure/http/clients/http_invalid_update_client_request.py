# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/clients/http_invalid_update_client_request.py

This file defines the HttpInvalidUpdateClientRequest class.

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
    InvalidUpdateClientRequest,
    UpdateClientRequested,
)
from pythoneda.shared.infrastructure.http import HttpResponse
from typing import Dict, Type


class HttpInvalidUpdateClientRequest(HttpResponse):
    """
    HTTP interface for InvalidUpdateClientRequest

    Class name: HttpInvalidUpdateClientRequest

    Responsibilities:
        - Define the HTTP interface for the InvalidUpdateClientRequest event.

    Collaborators:
        - None
    """

    def __init__(
        self, event: InvalidUpdateClientRequest, sourceEvent: UpdateClientRequested
    ):
        """
        Creates a new HttpInvalidUpdateClientRequest.
        :param responseEvent: The domain event, generated after a UpdateClientRequested event.
        :type responseEvent: org.acmsl.licdata.events.clients.InvalidUpdateClientRequest
        :param sourceEvent: The initial update-client-requested event.
        :type sourceEvent: org.acmsl.licdata.events.clients.UpdateClientRequested
        """
        super().__init__(responseEvent=responseEvent, sourceEvent=sourceEvent)

    @property
    def status_code(self) -> int:
        """
        Retrieves the status code.
        :return: The status code.
        :type: int
        """
        return 400

    @property
    def body(self) -> str:
        """
        Retrieves the body.
        :return: The body.
        :type: Dict
        """
        return json.dumps(
            {
                "message": "Invalid update client request",
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
    def event_class(cls) -> Type[InvalidUpdateClientRequest]:
        """
        Retrieves the class of the associated domain event.
        :return: The class.
        :type: Type[org.acmsl.licdata.event.clients.InvalidUpdateClientRequest]
        """
        return InvalidUpdateClientRequest


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
