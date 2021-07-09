# Copyright 2021 ForgeFlow S.L.  <https://www.forgeflow.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def remove_crm_partner_binding_records(cr):
    openupgrade.logged_query(cr, """DELETE FROM crm_partner_binding""")


def remove_crm_partner_binding_selection_field_record(cr):
    openupgrade.logged_query(
        cr,
        """
        DELETE FROM ir_model_fields_selection
        WHERE field_id in (
            SELECT id
            FROM ir_model_fields
            WHERE model = 'crm.partner.binding'
        )
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    remove_crm_partner_binding_records(env.cr)
    remove_crm_partner_binding_selection_field_record(env.cr)
