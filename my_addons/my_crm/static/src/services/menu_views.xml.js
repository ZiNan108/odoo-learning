/** @odoo-module */

import { registry } from "@web/core/registry";

export const menu_views.xml = {
    dependencies: ["rpc", "orm"],
    async start(env, { rpc, orm }) {

        return {  };
    },
};

registry.category("services").add("menu_views.xml", menu_views.xml);