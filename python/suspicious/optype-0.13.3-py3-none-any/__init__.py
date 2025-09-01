def __getattr__(name: str) -> object:
    if submodule := _submodules.get(name):
        return _importlib.import_module(f"{__name__}.{submodule}")
    try:
        return globals()[name]
    except KeyError:
        msg = f"module '{__name__}' has no attribute '{name}'"
        module = _importlib.import_module(__name__)
        raise AttributeError(msg, name=name, obj=module) from None
