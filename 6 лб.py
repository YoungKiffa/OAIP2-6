def main():
    # 1
    def quarters(*points):
        quarters_count = {1: 0, 2: 0, 3: 0, 4: 0}

        for point in points:
            x, y = point

            if x > 0 and y > 0:
                quarters_count[1] += 1
            elif x < 0 and y > 0:
                quarters_count[2] += 1
            elif x < 0 and y < 0:
                quarters_count[3] += 1
            elif x > 0 and y < 0:
                quarters_count[4] += 1

        return quarters_count

    points = (1, 2), (-3, 4), (-2, -5), (3, -1), (0, 0), (0, 7)
    result = quarters(*points)
    print("Количество точек в каждой четверти координатной плоскости:", result)

    # 2
    VIN = 42

    def future(*masses, **constants):
        acceleration_constant = constants.get('acceleration_constant', 0)  # Получаем значение ускоряющей константы

        total_mass = sum(masses)

        if total_mass * acceleration_constant > VIN:
            return "ACCELERATION"
        elif total_mass * acceleration_constant < VIN:
            return "DECELERATION"
        else:
            return "UNCHANGED"

    result = future(10, 20, 5, acceleration_constant=2)
    print("Предсказание будущего вселенной:", result)


if __name__ == "__main__":
    main()
