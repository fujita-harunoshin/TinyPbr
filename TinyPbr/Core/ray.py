from dataclasses import dataclass
from typing import Any
from Core.vector import Vector3

class Ray:
    def __init__(self, origin: Vector3, direction: Vector3):
        """
        origin: レイの始点
        direction: レイの方向（基本的に正規化前提）
        """
        self.origin = origin
        self.direction = direction

    def at(self, t: float) -> Vector3:
        """
        媒介変数tに応じた空間上の座標 P(t) を返す
        数式: P(t) = O + tD
        """
        return self.origin + (self.direction * t)

@dataclass
class HitRecord:
    """
    レイがオブジェクトに交差した際の情報を格納するクラス
    """
    t: float # 起点からの距離
    p: Vector3 # 空間上の座標
    normal: Vector3 # 交差地点の法線ベクトル
    # material: Any
