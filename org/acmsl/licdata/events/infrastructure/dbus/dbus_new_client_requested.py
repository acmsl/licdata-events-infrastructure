# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/artifact/events/infrastructure/dbus/dbus_new_client_requested.py

This file defines the DbusNewClientRequested class.

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
from dbus_next import Message
from dbus_next.service import ServiceInterface, signal
import json
from org.acmsl.licdata.events import NewClientRequested
from pythoneda.shared import BaseObject
from org.acmsl.licdata.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusNewClientRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for NewClientRequested

    Class name: DbusNewClientRequested

    Responsibilities:
        - Define the d-bus interface for the NewClientRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusNewClientRequested.
        """
        super().__init__("Licdata_NewClientRequested")

    @signal()
    def NewClientRequested(self, email: "s", address: "s", contact: "s", phone: "s"):
        """
        Defines the NewClientRequested d-bus signal.
        :param email: The email.
        :type email: str
        :param address: The address.
        :type address: str
        :param contact: The contact information.
        :type contact: str
        :param phone: The phone.
        :type phone: str
        """
        pass

    @classmethod
    def path(cls) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    @classmethod
    def transform(cls, event: NewClientRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: org.acmsl.licdata.events.NewClientRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.email,
            event.address,
            event.contact,
            event.phone,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: NewClientRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: org.acmsl.licdata.events.NewClientRequested
        :return: The signature.
        :rtype: str
        """
        return "ssssss"

    @classmethod
    def parse(cls, message: Message) -> NewClientRequested:
        """
        Parses given d-bus message containing a NewClientRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The NewClientRequested event.
        :rtype: org.acmsl.licdata.events.NewClientRequested
        """
        email, address, contact, phone, prev_event_ids, event_id = message.body
        return NewClientRequested(
            email,
            address,
            contact,
            phone,
            json.loads(prev_event_ids),
            event_id,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
