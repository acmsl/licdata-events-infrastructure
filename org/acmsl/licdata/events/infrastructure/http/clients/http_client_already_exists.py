# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/clients/http_new_client_requested.py

This file defines the HttpClientAlreadyExists class.

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
from org.acmsl.licdata.events.clients import ClientAlreadyExists
from pythoneda.shared.infrastructure.http import HttpMethod
from typing import Dict, Type


class HttpClientAlreadyExists(HttpBaseClientEvent):
    """
    HTTP interface for ClientAlreadyExists

    Class name: HttpClientAlreadyExists

    Responsibilities:
        - Define the HTTP interface for the ClientAlreadyExists event.

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
        event: ClientAlreadyExists,
    ):
        """
        Creates a new HttpClientAlreadyExists.
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
            httpMethod, queryStringParameters, headers, pathParameters, body, event
        )

    @classmethod
    def event_class(cls) -> Type[ClientAlreadyExists]:
        """
        Retrieves the class of the event.
        :return: The class.
        :type: Type[org.acmsl.licdata.event.clients.ClientAlreadyExists]
        """
        return ClientAlreadyExists


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
