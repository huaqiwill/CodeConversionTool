import os
import importlib.util

class PluginManager:
    def __init__(self):
        self.plugins = {}
    
    def load_plugins(self, plugin_dir):
        """加载插件目录中的所有插件"""
        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                plugin_path = os.path.join(plugin_dir, filename)
                self.load_plugin(plugin_path)
    
    def load_plugin(self, plugin_path):
        """加载单个插件"""
        name = os.path.basename(plugin_path)[:-3]
        spec = importlib.util.spec_from_file_location(name, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if hasattr(module, 'Plugin'):
            self.plugins[name] = module.Plugin()