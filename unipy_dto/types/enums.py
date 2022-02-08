from .base import BaseEnum


__all__ = [
    "ServiceType",
    "ServiceStatus",
]


class ServiceType(BaseEnum):
    LoadBalancer = "LoadBalancer"
    NodePort = "NodePort"
    ClusterIP = "ClusterIP"


class ServiceStatus(BaseEnum):
    """THIS ORDER IS REFERENCED. DO NOT CHANGE IT.
    """
    WAITING = "WAITING"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    COMPLETED = "COMPLETED"
    DELETED = "DELETED"
    UNKNOWN = "UNKNOWN"
    ERROR = "ERROR"
