# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/http_new_client_created.py

This file defines the HttpBaseClientEvent class.

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
from org.acmsl.licdata.events.clients import BaseClientEvent
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.http import HttpEvent, HttpMethod
from typing import Dict


class HttpBaseClientEvent(HttpEvent):
    """
    Base class for client-related HTTP event.

    Class name: HttpBaseClientEvent

    Responsibilities:
        - Define common data and methods for client-related HTTP events.

    Collaborators:
        - None
    """

    def __init__(
        self,
        httpMethod: HttpMethod,
        queryStringParameters: Dict,
        headers: Dict,
        pathParameters: Dict,
        body: Dict,
    ):
        """
        Creates a new HttpBaseClientEvent.
        :param httpMethod: The HTTP method.
        :type httpMethod: pythoneda.shared.infrastructure.http.HttpMethod
        :param queryStringParameters: The query string parameters.
        :type queryStringParameters: Dict
        :param headers: The headers.
        :type headers: Dict
        :param pathParameters: The path parameters.
        :type pathParameters: Dict
        :param body: The body.
        :type body: Dict
        """
        super().__init__(
            httpMethod, queryStringParameters, headers, pathParameters, body
        )

    @property
    def email(self) -> str:
        """
        Retrieves the email.
        :return: Such value.
        :rtype: str
        """
        return self.retrieve_param("email", None)

    @property
    def address(self) -> str:
        """
        Retrieves the address.
        :return: Such value.
        :rtype: str
        """
        return self.retrieve_param("address", None)

    @property
    def contact(self) -> str:
        """
        Retrieves the contact.
        :return: Such value.
        :rtype: str
        """
        return self.retrieve_param("contact", None)

    @property
    def phone(self) -> str:
        """
        Retrieves the phone.
        :return: Such value.
        :rtype: str
        """
        return self.retrieve_param("phone", None)

    def to_event(self) -> Event:
        """
        Retrieves the event.
        :return: The event.
        :rtype: Event
        """
        event_class = self.__class__.event_class()

        return event_class(self.email, self.address, self.contact, self.phone)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
