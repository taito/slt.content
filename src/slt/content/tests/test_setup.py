from Products.CMFCore.utils import getToolByName
from slt.content.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def test_installed__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('slt.content'))

    def test_browserlayer(self):
        from slt.content.browser.interfaces import ISltContentLayer
        from plone.browserlayer import utils
        self.assertIn(ISltContentLayer, utils.registered_layers())

    def test_catalog__column__feed_order(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIn('feed_order', catalog.schema())

    def test_catalog__index__feed_order(self):
        from Products.PluginIndexes.FieldIndex.FieldIndex import FieldIndex
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIsInstance(catalog.Indexes['feed_order'], FieldIndex)

    def test_memberdata_properties(self):
        memberdata = getToolByName(self.portal, 'portal_memberdata')
        ids = ['birth_date', 'registration_number', 'allow_direct_marketing']
        for pid in ids:
            self.assertTrue(memberdata.hasProperty(pid))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-slt.content:default'), u'12')

    def test_metadata__installed__collective_cart_shopping(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.cart.shopping'))

    def test_rolemap__slt_content_Edit_Member_Area__rolesOfPermission(self):
        permission = "slt.content: Edit Member Area"
        self.assertEqual(self.get_roles(self.portal, permission), [
            'Manager',
            'Site Administrator'])

    def test_rolemap__slt_content_Edit_Member_Area__acquiredRolesAreUsedBy(self):
        permission = "slt.content: Edit Member Area"
        self.assertEqual(self.portal.acquiredRolesAreUsedBy(permission), '')

    def get_ctype(self, name):
        """Returns content type info.

        :param name: Name of content type.
        :type name: test_types__Plone_Site__filter_content_types
        """
        types = getToolByName(self.portal, 'portal_types')
        return types.getTypeInfo(name)

    def test_types_ShippingMethod(self):
        ctype = self.get_ctype('ShippingMethod')
        self.assertFalse(ctype.global_allow)

    def test_types_collective_cart_core_Article(self):
        ctype = self.get_ctype('collective.cart.core.Article')
        self.assertTrue(ctype.global_allow)
        self.assertEqual(ctype.schema, 'slt.content.schema.ArticleSchema')
        self.assertEqual(ctype.klass, 'slt.content.content.Article')
        self.assertEqual(ctype.behaviors, (
            'plone.app.content.interfaces.INameFromTitle',
            'plone.app.dexterity.behaviors.metadata.IDublinCore',
            'collective.behavior.sku.interfaces.ISKU',
            'collective.behavior.salable.interfaces.ISalable',
            'slt.content.interfaces.IDiscountBehavior',
            'collective.behavior.stock.interfaces.IStock',
            'collective.behavior.vat.interfaces.IVAT',
            'collective.behavior.size.interfaces.ISize'))

    def test_types_collective_cart_shopping_Shop(self):
        ctype = self.get_ctype('collective.cart.shopping.Shop')
        self.assertFalse(ctype.global_allow)

    def test_types__slt_content_MemberArea__i18n_domain(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.i18n_domain, 'slt.content')

    def test_types__slt_content_MemberArea__meta_type(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.meta_type, 'Dexterity FTI')

    def test_types__slt_content_MemberArea__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.title, 'Member Area')

    def test_types__slt_content_MemberArea__description(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.description, '')

    def test_types__slt_content_MemberArea__content_icon(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.getIcon(), 'group.png')

    def test_types__slt_content_MemberArea__allow_discussion(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertFalse(ctype.allow_discussion)

    def test_types__slt_content_MemberArea__global_allow(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertFalse(ctype.global_allow)

    def test_types__slt_content_MemberArea__filter_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertTrue(ctype.filter_content_types)

    def test_types__slt_content_MemberArea__allowed_content_types(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.allowed_content_types, (
            'collective.cart.shopping.CustomerInfo',))

    def test_types__slt_content_MemberArea__schema(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.schema, 'slt.content.schema.MemberAreaSchema')

    def test_types__slt_content_MemberArea__klass(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.klass, 'slt.content.content.MemberArea')

    def test_types__slt_content_MemberArea__add_permission(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.add_permission, 'slt.content.AddMemberArea')

    def test_types__slt_content_MemberArea__behaviors(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.behaviors,
            ('plone.app.content.interfaces.INameFromTitle',))

    def test_types__slt_content_MemberArea__default_view(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.default_view, 'view')

    def test_types__slt_content_MemberArea__default_view_fallback(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertFalse(ctype.default_view_fallback)

    def test_types__slt_content_MemberArea__view_methods(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(ctype.view_methods, ('view',))

    def test_types__slt_content_MemberArea__default_aliases(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        self.assertEqual(
            ctype.default_aliases,
            {'edit': '@@edit', 'sharing': '@@sharing', '(Default)': '(dynamic view)', 'view': '(selected layout)'})

    def test_types__slt_content_MemberArea__action__view__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.title, 'Orders')

    def test_types__slt_content_MemberArea__action__view__condition(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.condition, '')

    def test_types__slt_content_MemberArea__action__view__url_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.getActionExpression(), 'string:${folder_url}/')

    def test_types__slt_content_MemberArea__action__view__visible(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertTrue(action.visible)

    def test_types__slt_content_MemberArea__action__view__permissions(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.permissions, (u'View',))

    def test_types__slt_content_MemberArea__action__edit__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.title, 'Edit')

    def test_types__slt_content_MemberArea__action__edit__condition(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.condition, '')

    def test_types__slt_content_MemberArea__action__edit__url_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.getActionExpression(), 'string:${object_url}/edit')

    def test_types__slt_content_MemberArea__action__edit__visible(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertTrue(action.visible)

    def test_types__slt_content_MemberArea__action__edit__permissions(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.permissions, (u'slt.content: Edit Member Area',))

    def test_types__slt_content_MemberArea__action__addresses__title(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/addresses')
        self.assertEqual(action.title, 'Addresses')

    def test_types__slt_content_MemberArea__action__addresses__condition(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/addresses')
        self.assertEqual(action.condition, '')

    def test_types__slt_content_MemberArea__action__addresses__url_expr(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/addresses')
        self.assertEqual(action.getActionExpression(), 'string:${folder_url}/@@address-listing')

    def test_types__slt_content_MemberArea__action__addresses__visible(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/addresses')
        self.assertTrue(action.visible)

    def test_types__slt_content_MemberArea__action__addresses__permissions(self):
        types = getToolByName(self.portal, 'portal_types')
        ctype = types.getTypeInfo('slt.content.MemberArea')
        action = ctype.getActionObject('object/addresses')
        self.assertEqual(action.permissions, (u'Modify portal content',))

    def uninstall_package(self):
        """Uninstall package: slt.content."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['slt.content'])

    def test_uninstall__package(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('slt.content'))

    def test_uninstall__browserlayer(self):
        self.uninstall_package()
        from slt.content.browser.interfaces import ISltContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISltContentLayer, utils.registered_layers())

    def test_uninstall__metadata__installed__collective_cart_shopping(self):
        self.uninstall_package()
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.cart.shopping'))
