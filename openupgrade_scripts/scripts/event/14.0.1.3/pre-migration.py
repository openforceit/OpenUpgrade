# Copyright 2021 ForgeFlow S.L.  <https://www.forgeflow.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def mock_up_event_stage_table(cr):
    # This is necessary to make the ``_get_default_stage_id`` method work
    # properly when Odoo tries to initialize ``stage_id`` field on
    # ``event.event``.
    cr.execute("SELECT 1 FROM event_event LIMIT 1")
    if cr.rowcount and not openupgrade.table_exists(cr, 'event_stage'):
        # Adding only minimal set of columns, they will be overridden anyway
        # later on when Odoo initializes ``event.stage``
        openupgrade.logged_query(
            cr,
            """
            CREATE TABLE "event_stage"
            (id serial not null,
             name varchar not null,
             sequence int4,
             PRIMARY KEY(id))
            """
        )


@openupgrade.migrate()
def migrate(env, version):
    mock_up_event_stage_table(env.cr)
