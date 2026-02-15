import sys
import matplotlib.pyplot as plt
from Core.vector import Vector3
from Core.camera import Camera
from Geometry.sphere import Sphere
from Geometry.scene import Scene
from Integrators.normal import NormalIntegrator

def main():
    image_width = 400
    aspect_ratio = 16.0 / 9.0
    image_height = int(image_width / aspect_ratio)

    # --- 1. 各モジュールの準備 ---
    camera = Camera(aspect_ratio)
    
    world = Scene()
    world.add(Sphere(center=Vector3(0.0, 0.0, -1.0), radius=0.5))
    world.add(Sphere(center=Vector3(0.0, -100.5, -1.0), radius=100.0))

    integrator = NormalIntegrator()

    # --- 2. レンダリングループ ---
    image_data = []
    for j in range(image_height - 1, -1, -1):
        sys.stdout.write(f"\r残りスキャンライン: {j} ")
        sys.stdout.flush()
        
        row_colors = []
        for i in range(image_width):
            u = float(i) / (image_width - 1)
            v = float(j) / (image_height - 1)
            
            ray = camera.get_ray(u, v)
            pixel_color = integrator.render_pixel(ray, world)
            row_colors.append([pixel_color.x, pixel_color.y, pixel_color.z])
            
        image_data.append(row_colors)

    print("\nレンダリング完了")

    # --- 3. 画像の表示 ---
    fig = plt.figure(figsize=(8, 4.5))
    fig.canvas.manager.set_window_title("TinyPbr Preview")
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.imshow(image_data)
    plt.show()

if __name__ == "__main__":
    main()
