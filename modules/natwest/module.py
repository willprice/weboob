# -*- coding: utf-8 -*-

# Copyright(C) 2015      Will Price
#
# This file is part of weboob.
#
# weboob is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# weboob is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with weboob. If not, see <http://www.gnu.org/licenses/>.


from weboob.tools.backend import Module
from weboob.capabilities.bank import CapBank

from .browser import NatwestBrowser


__all__ = ['NatwestModule']


class NatwestModule(Module, CapBank):
    NAME = 'natwest'
    DESCRIPTION = u'natwest website'
    MAINTAINER = u'Will Price'
    EMAIL = 'will.price94@gmail.com'
    LICENSE = 'AGPLv3+'
    VERSION = '1.1'

    BROWSER = NatwestBrowser

    def _restrict_level(self, split_path, lmax):
        raise NotImplementedError()

    def get_account(self, id):
        """
        Get an account from its ID.

        :param id: ID of the account
        :type id: :class:`str`
        :rtype: :class:`Account`
        :raises: :class:`AccountNotFound`
        """
        raise NotImplementedError()

    def get_collection(self, objs, split_path):
        """
        Get a collection for a given split path.
        If the path is invalid (i.e. can't be handled by this module),
        it should return None.
        """
        raise NotImplementedError()

    def iter_accounts(self):
        """
        Iter accounts.

        :rtype: iter[:class:`Account`]
        """
        raise NotImplementedError()

    def iter_coming(self, account):
        """
        Iter coming transactions on a specific account.

        :param account: account to get coming transactions
        :type account: :class:`Account`
        :rtype: iter[:class:`Transaction`]
        :raises: :class:`AccountNotFound`
        """
        raise NotImplementedError()

    def iter_history(self, account):
        """
        Iter history of transactions on a specific account.

        :param account: account to get history
        :type account: :class:`Account`
        :rtype: iter[:class:`Transaction`]
        :raises: :class:`AccountNotFound`
        """
        raise NotImplementedError()

    def iter_investment(self, account):
        """
        Iter investment of a market account

        :param account: account to get investments
        :type account: :class:`Account`
        :rtype: iter[:class:`Investment`]
        :raises: :class:`AccountNotFound`
        """
        raise NotImplementedError()

    def iter_resources(self, objs, split_path):
        """
        Iter resources.

        Default implementation of this method is to return on top-level
        all accounts (by calling :func:`iter_accounts`).

        :param objs: type of objects to get
        :type objs: tuple[:class:`BaseObject`]
        :param split_path: path to discover
        :type split_path: :class:`list`
        :rtype: iter[:class:`BaseObject`]
        """
        raise NotImplementedError()

    def iter_resources_flat(self, objs, split_path, clean_only):
        """
        Call iter_resources() to fetch all resources in the tree.
        If clean_only is True, do not explore paths, only remove them.
        split_path is used to set the starting path.
        """
        raise NotImplementedError()

    def iter_transfer_recipients(self, account):
        """
        Iter recipients availables for a transfer from a specific account.

        :param account: account which initiate the transfer
        :type account: :class:`Account`
        :rtype: iter[:class:`Recipient`]
        :raises: :class:`AccountNotFound`
        """
        raise NotImplementedError()

    def transfer(self, account, recipient, amount, reason):
        """
        Make a transfer from an account to a recipient.

        :param account: account to take money
        :type account: :class:`Account`
        :param recipient: account to send money
        :type recipient: :class:`Recipient`
        :param amount: amount
        :type amount: :class:`decimal.Decimal`
        :param reason: reason of transfer
        :type reason: :class:`unicode`
        :rtype: :class:`Transfer`
        :raises: :class:`AccountNotFound`, :class:`TransferError`
        """
        raise NotImplementedError()

    def validate_collection(self, objs, collection):
        """
        Tests if a collection is valid.
        For compatibility reasons, and to provide a default way, it checks if
        the collection has at least one object in it. However, it is not very
        efficient or exact, and you are encouraged to override this method.
        You can replace the collection object entirely by returning a new one.
        """
        raise NotImplementedError()
