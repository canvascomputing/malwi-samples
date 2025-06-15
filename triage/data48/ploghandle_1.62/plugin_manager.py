from polaris.pkg.model.context import ValueContext
from polaris.pkg.model.service import Instance
from polaris.pkg.config.api import Configuration


class PluginType:
    OUTLIER_DETECTION = 1
    SERVER_CONNECTOR = 2
    SERVICE_ROUTER = 3
    LOAD_BALANCE = 4
    CIRCUIT_BREAKER = 5
    LOCAL_CACHE = 6
    STAT_REPORTER = 7


class EventType:
    ON_LOCALVALUE_CREATED = 1


class DetectResult:
    def __init__(self, detect_type: str = "", ret_status: int = 0, detect_time: int = 0,
                 detect_instance: Instance = None):
        self.detect_type = detect_type
        self.ret_status = ret_status
        self.detect_time = detect_time
        self.detect_instance = detect_instance

    def get_detect_type(self):
        return self.detect_type

    def get_detect_time(self):
        return self.detect_time

    def get_detect_instance(self):
        return self.detect_instance

    def get_ret_status(self):
        return self.ret_status


class PluginManager:
    def __init__(self):
        self.plugin_container = {}
        self.plugin_instance = {}

    def register(self, plugin_type: PluginType, plugin_name: str, plugin_cls):
        # print('register plugin', plugin_type, plugin_name)
        if plugin_type not in self.plugin_container.keys():
            self.plugin_container[plugin_type] = {}
        self.plugin_container[plugin_type][plugin_name] = plugin_cls

    def get(self, plugin_type: PluginType, plugin_name: str):
        if plugin_type in self.plugin_container:
            return self.plugin_container[plugin_type][plugin_name]
        else:
            return ""

    def find_instance(self, plugin_type: PluginType, plugin_name: str) -> bool:
        if plugin_type in self.plugin_instance and plugin_name in self.plugin_instance[plugin_type]:
            return True
        return False

    def get_instance(self, plugin_type: PluginType, plugin_name: str):
        return self.plugin_instance[plugin_type][plugin_name]

    def set_instance(self, plugin_type: PluginType, plugin_name: str, instance):
        if plugin_type not in self.plugin_instance:
            self.plugin_instance[plugin_type] = {}

        DefaultPluginManager.plugin_instance[plugin_type][plugin_name] = instance

    def clear_instances(self):
        self.plugin_instance = {}

    def destroy_plugins(self):
        self.plugin_container = {}
        self.plugin_instance = {}


def register_plugin(plugin_type: PluginType, plugin_name: str):
    def decorator(cls):
        DefaultPluginManager.register(plugin_type, plugin_name, cls)
        return cls

    return decorator


# the function should be called after setup
def get_plugin(plugin_type: PluginType, plugin_name: str):
    return DefaultPluginManager.get_instance(plugin_type, plugin_name)


DefaultPluginManager = PluginManager()


def reload_global_plugin_manager():
    global DefaultPluginManager
    DefaultPluginManager.clear_instances()


class InitContext:
    def __init__(self, config: Configuration = None, value_ctx: ValueContext = None):
        self.config = config
        self.value_ctx = value_ctx


def setup(init_ctx: InitContext):
    reload_global_plugin_manager()

    for plugin_type, plugins in DefaultPluginManager.plugin_container.items():
        for plugin_name, plugin in plugins.items():
            if not DefaultPluginManager.find_instance(plugin_type, plugin_name):
                DefaultPluginManager.set_instance(plugin_type, plugin_name, plugin(init_ctx))


event_handle_map = {}


def register_event_handle(event_type, func):
    if event_handle_map.get(event_type, None) is not None:
        event_handle_map[event_type].append(func)
    else:
        event_handle_map[event_type] = [func]


def get_event_subscriber(event_type):
    return event_handle_map.get(event_type, None)
