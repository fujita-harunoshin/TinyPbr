from abc import ABC, abstractmethod
from Core.ray import Ray
from Geometry.scene import Scene
from Core.vector import Vector3

class Integrator(ABC):
    @abstractmethod
    def render_pixel(self, ray: Ray, scene: Scene) -> Vector3:
        """
        与えられたレイとシーンからピクセルの色を計算
        """
        pass
