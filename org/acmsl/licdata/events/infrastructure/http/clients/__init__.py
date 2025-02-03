# vim: set fileencoding=utf-8
"""
org/acmsl/licdata/events/infrastructure/http/clients/__init__.py

This file ensures org.acmsl.licdata.events.infrastructure.http.clients is a namespace.

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
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .http_client_request import HttpClientRequest
from .http_client_already_exists import HttpClientAlreadyExists
from .http_invalid_new_client_request import HttpInvalidNewClientRequest
from .http_new_client_created import HttpNewClientCreated
from .http_new_client_requested import HttpNewClientRequested
from .http_list_clients_requested import HttpListClientsRequested
from .http_invalid_list_clients_request import HttpInvalidListClientsRequest
from .http_matching_clients_found import HttpMatchingClientsFound
from .http_no_matching_clients_found import HttpNoMatchingClientsFound
from .http_delete_client_requested import HttpDeleteClientRequested
from .http_client_deleted import HttpClientDeleted
from .http_invalid_delete_client_request import HttpInvalidDeleteClientRequest
from .http_client_response_factory import HttpClientResponseFactory

# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
