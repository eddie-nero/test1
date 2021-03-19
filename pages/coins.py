import time
import cv2
import numpy as np
import os
from django.conf import settings


def detect_coins(file):
    coins = cv2.imread(os.path.join(settings.MEDIA_ROOT, file), 1)

    gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(gray, 7)
    circles = cv2.HoughCircles(
        img,  # source image
        cv2.HOUGH_GRADIENT,  # type of detection
        1,
        50,
        param1=100,
        param2=50,
        minRadius=10,  # minimal radius
        maxRadius=380,  # max radius
    )

    coins_copy = coins.copy()

    for detected_circle in circles[0]:
        x_coor, y_coor, detected_radius = detected_circle
        coins_detected = cv2.circle(
            coins_copy,
            (int(x_coor), int(y_coor)),
            int(detected_radius),
            (0, 255, 0),
            4,
        )
    name = f'coins_detected_{time.time()}.png'
    cv2.imwrite(os.path.join(settings.MEDIA_ROOT, name), coins_detected)
    all_coins = len(circles[0])
    return circles, name, all_coins


def calculate_amount(file):
    roubles = {
        "1 RUB": {
            "value": 1,
            "radius": 20.5,
            "ratio": 1,
            "count": 0,
        },
        "2 RUB": {
            "value": 2,
            "radius": 23,
            "ratio": 1.12,
            "count": 0,
        },
        "5 RUB": {
            "value": 5,
            "radius": 25,
            "ratio": 1.22,
            "count": 0,
        },
        "10 RUB": {
            "value": 10,
            "radius": 22,
            "ratio": 1.073,
            "count": 0,
        },
    }

    circles, img_name, all_coins = detect_coins(file)
    radius = []
    coordinates = []

    for detected_circle in circles[0]:
        x_coor, y_coor, detected_radius = detected_circle
        radius.append(detected_radius)
        coordinates.append([x_coor, y_coor])

    smallest = min(radius)
    tolerance = 0.040
    total_amount = 0
    coins_circled = cv2.imread(os.path.join(settings.MEDIA_ROOT, img_name), 1)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for coin in circles[0]:
        ratio_to_check = coin[2] / smallest
        coor_x = coin[0]
        coor_y = coin[1]
        for rouble in roubles:
            value = roubles[rouble]['value']
            if abs(ratio_to_check - roubles[rouble]['ratio']) <= tolerance:
                roubles[rouble]['count'] += 1
                total_amount += roubles[rouble]['value']
                cv2.putText(coins_circled, str(value), (int(coor_x), int(coor_y)), font, 1,
                            (0, 0, 0), 4)

    print(f"The total amount is {total_amount} RUB")
    for rouble in roubles:
        pieces = roubles[rouble]['count']
        print(f"{rouble} = {pieces}x")

    name = f'coins_count_{time.time()}.png'
    cv2.imwrite(name, coins_circled)
    return all_coins, total_amount


if __name__ == "__main__":
    calculate_amount()
