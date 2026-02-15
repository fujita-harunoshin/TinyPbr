import math
from typing import Optional
from Core.vector import Vector3
from Core.ray import Ray, HitRecord
from Geometry.base import Shape

class Sphere(Shape):
    def __init__(self, center: Vector3, radius: float):
        self.center = center
        self.radius = radius

    def intersect(self, ray: Ray, t_min: float, t_max: float) -> Optional[HitRecord]:
        # レイの起点から球の中心へのベクトル（o - c）
        oc = ray.origin - self.center

        # 二次方程式の係数を計算
        a = ray.direction.dot(ray.direction)
        b = 2 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius

        # 判別式を計算
        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return None  # 交差なし

        # 2つの解（交差点）のうち、カメラに近い方（マイナスの方）を求める
        sqrtd = math.sqrt(discriminant)
        root = (-b - sqrtd) / (2.0 * a)

        # もし近い方の解が t_min ～ t_max の範囲外なら、もう一方の解を試す
        if root < t_min or t_max < root:
            root = (-b + sqrtd) / (2.0 * a)
            # それも範囲外なら交差なし
            if root < t_min or t_max < root:
                return None

        t = root # レイから交差点までの距離
        p = ray.at(t) # 交差点の座標

        # 法線ベクトルの計算（交差点から球の中心へのベクトルを正規化）
        normal = (p - self.center).normalize()

        return HitRecord(t=t, p=p, normal=normal)