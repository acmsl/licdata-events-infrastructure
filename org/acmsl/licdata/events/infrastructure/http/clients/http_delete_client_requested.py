# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/http_delete_client_requested.py

This file defines the HttpDeleteClientRequested class.

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
from .http_client_request import HttpClientRequest
from org.acmsl.licdata.events.clients import DeleteClientRequested
from pythoneda.shared.infrastructure.http import HttpMethod
from typing import Dict, Type


class HttpDeleteClientRequested(HttpClientRequest):
    """
    HTTP interface for DeleteClientRequested

    Class name: HttpDeleteClientRequested

    Responsibilities:
        - Define the HTTP interface for the DeleteClientRequested event.

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
        Creates a new HttpDeleteClientRequested.
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

    def to_event(self) -> DeleteClientRequested:
        """
        Retrieves the event.
        :return: The event.
        :rtype: org.acmsl.licdata.events.clients.DeleteClientRequested
        """
        return DeleteClientRequested(entityId=self.entity_id)

    @classmethod
    def event_class(cls) -> Type[DeleteClientRequested]:
        """
        Retrieves the class of the associated domain event.
        :return: The class.
        :type: Type[org.acmsl.licdata.events.clients.DeleteClientRequested]
        """
        return DeleteClientRequested


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
