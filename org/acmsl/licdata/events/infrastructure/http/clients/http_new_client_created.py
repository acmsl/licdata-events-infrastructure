# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/http_new_client_created.py

This file defines the HttpNewClientCreated class.

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
import json
from org.acmsl.licdata.events.clients import NewClientCreated, NewClientRequested
from pythoneda.shared.infrastructure.http import HttpResponse
from typing import Dict, Type


class HttpNewClientCreated(HttpResponse):
    """
    HTTP interface for NewClientCreated

    Class name: HttpNewClientCreated

    Responsibilities:
        - Define the HTTP interface for the NewClientCreated event.

    Collaborators:
        - None
    """

    def __init__(
        self, responseEvent: NewClientCreated, sourceEvent: NewClientRequested
    ):
        """
        Creates a new HttpNewClientCreated.
        :param responseEvent: The domain event, generated after a NewClientRequested event.
        :type responseEvent: org.acmsl.licdata.events.clients.NewClientCreated
        :param sourceEvent: The initial new-client-requested event.
        :type sourceEvent: org.acmsl.licdata.events.clients.NewClientRequested
        """
        super().__init__(responseEvent=responseEvent, sourceEvent=sourceEvent)

    @property
    def status_code(self) -> int:
        """
        Retrieves the status code.
        :return: The status code.
        :type: int
        """
        return 201

    @property
    def body(self) -> str:
        """
        Retrieves the body.
        :return: The body.
        :rtype: str
        """
        result = {}
        result["id"] = self._response_event.entity_id
        result["email"] = self._response_event.email
        if self._response_event.address is not None:
            result["address"] = self._response_event.address
        if self._response_event.contact is not None:
            result["contact"] = self._response_event.contact
        if self._response_event.phone is not None:
            result["phone"] = self._response_event.phone

        return json.dumps(result)

    @property
    def headers(self) -> Dict:
        """
        Retrieves the headers.
        :return: The headers.
        :type: Dict
        """
        return {"Location": f"/clients/{self._response_event.entity_id}"}

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
    def event_class(cls) -> Type[NewClientCreated]:
        """
        Retrieves the class of the event.
        :return: The class.
        :type: Type[org.acmsl.licdata.event.clients.NewClientCreated]
        """
        return NewClientCreated


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
