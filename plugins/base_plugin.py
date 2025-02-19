from abc import ABC, abstractmethod

class BasePlugin(ABC):
    @abstractmethod
    def name(self) -> str:
        """返回插件名称"""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """返回插件描述"""
        pass
    
    @abstractmethod
    def get_widget(self):
        """返回插件的主要界面部件"""
        pass