from typing import List, Optional
from Core.ray import Ray, HitRecord
from Geometry.base import Shape

class Scene(Shape):
    def __init__(self):
        # シーン内の全オブジェクトを格納するリスト
        self.objects: List[Shape] = []

    def add(self, object: Shape):
        """シーンにオブジェクトを追加"""
        self.objects.append(object)

    def clear(self):
        """シーンを空にする"""
        self.objects.clear()

    def intersect(self, ray: Ray, t_min: float, t_max: float) -> Optional[HitRecord]:
        """
        シーン内の全てのオブジェクトと交差判定を行い、
        カメラから一番近い交差点の情報を返す
        """
        closest_hit = None
        closest_so_far = t_max # 現在の最も近い交差点の距離

        for obj in self.objects:
            # t_maxを「今のところ一番近い距離」に制限して交差判定
            hit = obj.intersect(ray, t_min, closest_so_far)

            if hit:
                # もっと近い交差点が見つかったら更新
                closest_hit = hit
                closest_so_far = hit.t

        return closest_hit

