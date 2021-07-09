# Copyright 2021 ForgeFlow S.L.  <https://www.forgeflow.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def assign_event_default_stage(env):
    event_obj = env['event.event']
    default_stage = event_obj._get_default_stage_id()
    event_obj.search([]).write({'stage_id': default_stage.id})


@openupgrade.migrate()
def migrate(env, version):
    assign_event_default_stage(env)
