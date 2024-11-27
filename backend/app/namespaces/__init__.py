from .chat import ChatNamespace
from .notifications import NotificationsNamespace

namespaces = [
    (ChatNamespace('/chat')),
    (NotificationsNamespace('/notifications'))
]