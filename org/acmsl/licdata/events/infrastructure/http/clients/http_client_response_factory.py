# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/clients/http_client_response_factory.py

This file defines the HttpClientResponseFactory class.

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
    DeleteClientRequested,
    FindClientByIdRequested,
    ListClientsRequested,
    NewClientRequested,
    UpdateClientRequested,
)
from org.acmsl.licdata.events.infrastructure.http.clients import (
    HttpClientAlreadyExists,
    HttpClientDeleted,
    HttpClientUpdated,
    HttpInvalidDeleteClientRequest,
    HttpInvalidFindClientByIdRequest,
    HttpInvalidListClientsRequest,
    HttpInvalidNewClientRequest,
    HttpInvalidUpdateClientRequest,
    HttpMatchingClientFound,
    HttpMatchingClientsFound,
    HttpNewClientCreated,
    HttpNoMatchingClientsFound,
)
from pythoneda.shared import BaseObject, Event
from pythoneda.shared.infrastructure.http import HttpResponse
from typing import Dict


class HttpClientResponseFactory(BaseObject):
    """
    Factory for client-related events.

    Class name: HttpClientResponseFactory

    Responsibilities:
        - Define factory methods for client-related HTTP responses.

    Collaborators:
        - None
    """

    _singleton = None

    def __init__(self):
        """
        Creates a new HttpClientResponseFactory.
        """
        super().__init__()

    @classmethod
    def instance(cls) -> "HttpClientResponseFactory":
        """
        Retrieves the instance.
        :return: Such instance.
        :rtype: org.acmsl.licdata.events.infrastructure.http.clients.HttpClientResponseFactory
        """
        if cls._singleton is None:
            cls._singleton = cls()
        return cls._singleton

    def from_new_client_requested(
        self, event: Event, newClientRequested: DeleteClientRequested
    ) -> HttpResponse:
        """
        Creates a HTTP-based event from given domain event.
        :param event: The domain event, generated after a DeleteClientRequested event.
        :type event: pythoneda.shared.Event
        :param newClientRequested: The initial new-client-requested event.
        :type newClientRequested: org.acmsl.licdata.events.clients.DeleteClientRequested
        :return: The HTTP response.
        :rtype: pythoneda.shared.infrastructure.http.HttpResponse
        """
        result = None

        for target in [
            HttpNewClientCreated,
            HttpInvalidNewClientRequest,
            HttpClientAlreadyExists,
        ]:
            if isinstance(event, target.event_class()):
                result = target(responseEvent=event, sourceEvent=newClientRequested)
                break

        return result

    def from_find_client_by_id_requested(
        self, event: Event, findClientByIdRequested: FindClientByIdRequested
    ) -> HttpResponse:
        """
        Creates a HTTP-based event from given domain event.
        :param event: The domain event, generated after a FindClientByIdRequested event.
        :type event: pythoneda.shared.Event
        :param findClientByIdRequested: The initial new-client-requested event.
        :type findClientByIdRequested: org.acmsl.licdata.events.clients.FindClientByIdRequested
        :return: The HTTP response.
        :rtype: pythoneda.shared.infrastructure.http.HttpResponse
        """
        result = None

        for target in [
            HttpMatchingClientFound,
            HttpInvalidFindClientByIdRequest,
            HttpNoMatchingClientsFound,
        ]:
            if isinstance(event, target.event_class()):
                result = target(
                    responseEvent=event, sourceEvent=findClientByIdRequested
                )
                break

        return result

    def from_list_clients_requested(
        self, event: Event, listClientsRequested: ListClientsRequested
    ) -> HttpResponse:
        """
        Creates a HTTP-based event from given domain event.
        :param event: The domain event, generated after a ListClientsRequested event.
        :type event: pythoneda.shared.Event
        :param listClientsRequested: The initial new-client-requested event.
        :type listClientsRequested: org.acmsl.licdata.events.clients.ListClientsRequested
        :return: The HTTP response.
        :rtype: pythoneda.shared.infrastructure.http.HttpResponse
        """
        result = None

        for target in [
            HttpMatchingClientsFound,
            HttpNoMatchingClientsFound,
            HttpInvalidListClientsRequest,
        ]:
            if isinstance(event, target.event_class()):
                result = target(responseEvent=event, sourceEvent=listClientsRequested)
                break

        return result

    def from_delete_client_requested(
        self, event: Event, deleteClientRequested: DeleteClientRequested
    ) -> HttpResponse:
        """
        Creates a HTTP-based event from given domain event.
        :param event: The domain event, generated after a DeleteClientRequested event.
        :type event: pythoneda.shared.Event
        :param deleteClientRequested: The initial new-client-requested event.
        :type deleteClientRequested: org.acmsl.licdata.events.clients.DeleteClientRequested
        :return: The HTTP response.
        :rtype: pythoneda.shared.infrastructure.http.HttpResponse
        """
        result = None

        for target in [
            HttpClientDeleted,
            HttpInvalidDeleteClientRequest,
            HttpNoMatchingClientsFound,
        ]:
            if isinstance(event, target.event_class()):
                result = target(responseEvent=event, sourceEvent=deleteClientRequested)
                break

        return result

    def from_update_client_requested(
        self, event: Event, updateClientRequested: UpdateClientRequested
    ) -> HttpResponse:
        """
        Creates a HTTP-based event from given domain event.
        :param event: The domain event, generated after a UpdateClientRequested event.
        :type event: pythoneda.shared.Event
        :param updateClientRequested: The initial new-client-requested event.
        :type updateClientRequested: org.acmsl.licdata.events.clients.UpdateClientRequested
        :return: The HTTP response.
        :rtype: pythoneda.shared.infrastructure.http.HttpResponse
        """
        result = None

        for target in [
            HttpClientUpdated,
            HttpInvalidUpdateClientRequest,
            HttpNoMatchingClientsFound,
        ]:
            if isinstance(event, target.event_class()):
                result = target(responseEvent=event, sourceEvent=updateClientRequested)
                break

        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
