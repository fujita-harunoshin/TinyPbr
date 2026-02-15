from Core.vector import Vector3
from Core.ray import Ray

class Camera:
    def __init__(self, aspect_ratio: float = 16.0 / 9.0):
        """
        カメラの初期設定
        aspect_ratio: 画面の横幅と縦幅の比率
        """
        viewport_height = 2.0
        viewport_width = aspect_ratio * viewport_height
        focal_length = 1.0 # カメラからスクリーンまでの距離

        self.origin = Vector3(0.0, 0.0, 0.0)
        self.horizontal = Vector3(viewport_width, 0.0, 0.0)
        self.vertical = Vector3(0.0, viewport_height, 0.0)

        # スクリーンの左下の座標を計算して保存
        self.lower_left_corner = (
            self.origin
            - (self.horizontal * 0.5)
            - (self.vertical * 0.5)
            - Vector3(0.0, 0.0, focal_length)
        )

    def get_ray(self, u: float, v: float) -> Ray:
        """
        スクリーン上の位置割合(u, v)に対応するレイを生成して返す
        u: スクリーンの横方向の位置（0.0～1.0）
        v: スクリーンの縦方向の位置（0.0～1.0）
        """
        direction = (
            self.lower_left_corner
            + (self.horizontal * u)
            + (self.vertical * v)
            - self.origin
        )
        return Ray(self.origin, direction.normalize())
