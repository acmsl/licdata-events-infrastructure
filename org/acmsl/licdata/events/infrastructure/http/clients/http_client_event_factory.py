# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/clients/http_client_event_factory.py

This file defines the HttpClientEventFactory class.

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
from org.acmsl.licdata.events.clients import BaseClientEvent, NewClientRequested
from org.acmsl.licdata.events.infrastructure.http.clients import (
    HttpBaseClientEvent,
    HttpNewClientCreated,
    HttpInvalidNewClientRequest,
    HttpClientAlreadyExists,
)
from pythoneda.shared import BaseObject
from typing import Dict


class HttpClientEventFactory(BaseObject):
    """
    Factory for client-related events.

    Class name: HttpClientEventFactory

    Responsibilities:
        - Define factory methods for client-related events from HTTP events.

    Collaborators:
        - None
    """

    _singleton = None

    def __init__(self):
        """
        Creates a new HttpClientEventFactory.
        """
        super().__init__()

    @classmethod
    def instance(cls) -> "HttpClientEventFactory":
        """
        Retrieves the instance.
        :return: Such instance.
        :rtype: org.acmsl.licdata.events.infrastructure.http.clients.HttpClientEventFactory
        """
        if cls._singleton is None:
            cls._singleton = cls()
        return cls._singleton

    def from_new_client_requested(
        self, event: BaseClientEvent, newClientRequested: NewClientRequested
    ) -> HttpBaseClientEvent:
        """
        Creates a HTTP-based event from given domain event.
        :param event: The domain event, generated after a NewClientRequested event.
        :type event: org.acmsl.licdata.events.clients.BaseClientEvent
        :param newClientRequested: The initial new-client-requested event.
        :type newClientRequested: org.acmsl.licdata.events.clients.NewClientRequested
        """
        result = None

        for target in [
            HttpNewClientCreated,
            HttpInvalidNewClientRequest,
            HttpClientAlreadyExists,
        ]:
            if isinstance(event, target.event_class()):
                result = target(event, newClientRequested)
                break

        print(f"Returning {result} from {event}")
        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
