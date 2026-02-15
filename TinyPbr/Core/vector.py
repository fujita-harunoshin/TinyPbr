import math
from dataclasses import dataclass

@dataclass(frozen=True)
class Vector3:
    """3次元ベクトルクラス"""
    x: float
    y: float
    z: float

    def __add__(self, other: 'Vector3') -> 'Vector3':
        """足し算（v1+v2）"""
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector3') -> 'Vector3':
        """引き算（v1-v2）"""
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> 'Vector3':
        """スカラー倍（v1*a）"""
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other: 'Vector3') -> float:
        """内積"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        """ベクトルの長さ"""
        return math.sqrt(self.dot(self))

    def normalize(self) -> 'Vector3':
        """正規化"""
        length = self.length()
        if length == 0:
            return Vector3(0, 0, 0)
        return self * (1.0 / length)