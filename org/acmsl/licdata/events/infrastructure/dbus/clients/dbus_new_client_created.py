# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/artifact/events/infrastructure/dbus/dbus_new_client_created.py

This file defines the DbusNewClientCreated class.

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
from dbus_next.service import signal
import json
from org.acmsl.licdata.events.clients import NewClientCreated
from org.acmsl.licdata.events.infrastructure.dbus import DBUS_PATH
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.dbus import DbusEvent
from typing import List, Type


class DbusNewClientCreated(DbusEvent):
    """
    D-Bus interface for NewClientCreated

    Class name: DbusNewClientCreated

    Responsibilities:
        - Define the d-bus interface for the NewClientCreated event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusNewClientCreated.
        """
        super().__init__("Licdata_NewClientCreated")

    @signal()
    def NewClientCreated(self, email: "s", address: "s", contact: "s", phone: "s"):
        """
        Defines the NewClientCreated d-bus signal.
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
    def transform(cls, event: NewClientCreated) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: org.acmsl.licdata.events.clients.NewClientCreated
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
    def sign(cls, event: NewClientCreated) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: org.acmsl.licdata.events.clients.NewClientCreated
        :return: The signature.
        :rtype: str
        """
        return "ssssss"

    @classmethod
    def parse(cls, message: Message) -> NewClientCreated:
        """
        Parses given d-bus message containing a NewClientCreated event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The NewClientCreated event.
        :rtype: org.acmsl.licdata.events.clients.NewClientCreated
        """
        email, address, contact, phone, prev_event_ids, event_id = message.body
        return NewClientCreated(
            email,
            address,
            contact,
            phone,
            json.loads(prev_event_ids),
            event_id,
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
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
