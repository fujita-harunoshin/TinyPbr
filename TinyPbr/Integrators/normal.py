from Core.vector import Vector3
from Core.ray import Ray
from Geometry.scene import Scene
from Integrators.base import Integrator

class NormalIntegrator(Integrator):
    """
    物体の「法線」を色として出力する積分器
    """
    def render_pixel(self, ray: Ray, scene: Scene) -> Vector3:
        hit = scene.intersect(ray, t_min=0.001, t_max=100.0)

        if hit:
            n = hit.normal
            # 法線（-1.0～1.0）をRGB（0.0～1.0）に変換
            return Vector3(n.x + 1.0, n.y + 1.0, n.z + 1.0) * 0.5

        # 背景のグラデーション
        t = 0.5 * (ray.direction.y + 1.0)
        return (Vector3(1.0, 1.0, 1.0) * (1.0 - t)) + (Vector3(0.5, 0.7, 1.0) * t)
