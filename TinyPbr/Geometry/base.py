from abc import ABC, abstractmethod
from typing import Optional
from Core.ray import Ray, HitRecord

class Shape(ABC):
    @abstractmethod
    def intersect(self, ray: Ray, t_min: float, t_max: float) -> Optional[HitRecord]:
        """
        レイと形状の交差判定を行う抽象メソッド
        ray: 判定するレイ
        t_min: 判定する距離の最小値（誤差対策）
        t_max: 判定する距離の最大値（誤差対策）
        戻り値: HitRecord（交差情報）またはNone（交差なし）
        """
        pass