# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/http_new_client_created.py

This file defines the HttpClientRequest class.

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
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.http import HttpMethod, HttpRequest
from typing import Dict


class HttpClientRequest(HttpRequest):
    """
    Base class for client-related HTTP event.

    Class name: HttpClientRequest

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
        Creates a new HttpClientRequest.
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
    def entity_id(self) -> str:
        """
        Retrieves the id of the entity.
        :return: Such value.
        :rtype: str
        """
        return self.retrieve_param("id", None)

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

        return event_class(
            email=self.email,
            address=self.address,
            contact=self.contact,
            phone=self.phone,
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


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
