from Products.CMFCore.utils import getToolByName
from collective.base.adapter import Adapter
from collective.cart.shopping.adapter.interface import ShoppingSite as BaseShoppingSite
from collective.cart.shopping.interfaces import ICustomerInfo
from five import grok
from slt.content.interfaces import IMember


class ShoppingSite(BaseShoppingSite):
    """Adapter for shopping site"""

    def link_to_order_for_customer(self, number):
        """Link to order for customer

        :param number: Cart ID
        :type number: int

        :rtype: str
        """
        membership = getToolByName(self.context, 'portal_membership')
        return '{}?order_number={}'.format(membership.getHomeUrl(), number)


class Member(Adapter):
    """Member related adapter"""

    grok.provides(IMember)

    @property
    def area(self):
        """MemberArea content type for member."""
        membership = getToolByName(self.context, 'portal_membership')
        return membership.getHomeFolder()

    @property
    def default_billing_info(self):
        """Default billing info."""
        if self.area.default_billing_info:
            return self.get_brain(UID=self.area.default_billing_info)

    @property
    def default_shipping_info(self):
        """Default shipping info."""
        if self.area.default_shipping_info:
            return self.get_brain(UID=self.area.default_shipping_info)

    @property
    def infos(self):
        """All the address infos."""
        if self.area:
            path = '/'.join(self.area.getPhysicalPath())
            return self.get_brains(ICustomerInfo, path=path, depth=1)

    def rest_of_infos(self, uuid):
        """All the address infos except for the info with the uuid."""
        return [info for info in self.infos if info.UID != uuid]
