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
from .http_base_client_event import HttpBaseClientEvent
import json
from org.acmsl.licdata.events.clients import NewClientCreated, NewClientRequested
from pythoneda.shared import BaseObject
from typing import Dict, Type


class HttpNewClientCreated(BaseObject):
    """
    HTTP interface for NewClientCreated

    Class name: HttpNewClientCreated

    Responsibilities:
        - Define the HTTP interface for the NewClientCreated event.

    Collaborators:
        - None
    """

    def __init__(self, event: NewClientCreated, sourceEvent: NewClientRequested):
        """
        Creates a new HttpNewClientCreated.
        :param event: The domain event, generated after a NewClientRequested event.
        :type event: org.acmsl.licdata.events.clients.BaseClientEvent
        :param sourceEvent: The initial new-client-requested event.
        :type sourceEvent: org.acmsl.licdata.events.clients.NewClientRequested
        """
        super().__init__()
        self._event = event
        self._source_event = sourceEvent

    @property
    def event(self) -> NewClientCreated:
        """
        Retrieves the event.
        :return: The event.
        :type: org.acmsl.licdata.events.clients.NewClientCreated
        """
        return self._event

    @property
    def source_event(self) -> NewClientRequested:
        """
        Retrieves the source event.
        :return: The source event.
        :type: org.acmsl.licdata.events.clients.NewClientRequested
        """
        return self._source_event

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
        :type: Dict
        """
        return json.dumps(
            {
                "id": self._event.id,
                "email": self._event.email,
                "address": self._event.address,
                "contact": self._event.contact,
                "phone": self._event.phone,
            }
        )

    @property
    def headers(self) -> Dict:
        """
        Retrieves the headers.
        :return: The headers.
        :type: Dict
        """
        return {"Location": f"/clients/{self._event.id}"}

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
