from Core.vector import Vector3

def main():
    v1 = Vector3(1.0, 2.0, 3.0)
    v2 = Vector3(4.0, 5.0, 6.0)

    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"v1 dot v2 = {v1.dot(v2)}")

    direction = Vector3(0.0, 3.0, 4.0)
    print(f"正規化された方向ベクトル: {direction.normalize()}")

if __name__ == "__main__":
    main()
