EXCLUDED_PLUGINS = {
    "step_decorator": [
        "metaflow.plugins.aws.batch.batch_decorator"
    ]
}

for plugin_type, plugins in EXCLUDED_PLUGINS.items():
    for plugin in plugins:
        if plugin in globals()[plugin_type.upper() + 'S']:
            globals()[plugin_type.upper() + 'S'].remove(plugin)
