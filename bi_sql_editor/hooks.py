# Copyright 2015-2017 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def uninstall_hook(env):
    recs = env["bi.sql.view"].search([])
    for rec in recs:
        rec.button_set_draft()


def post_init_hook(env):
    parent_menu_id = env.ref("bi_sql_editor.menu_bi_sql_editor").id
    env["bi.sql.view"].search(
        [("parent_menu_id", "=", False)]
    ).parent_menu_id = parent_menu_id
