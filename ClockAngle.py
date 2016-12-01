def clock_angle(time):

    hours = time.split(":")

    if int(hours[0]) <= 12:
        h = int(hours[0])
    else:
        h = int(hours[0]) - 12

    m = int(hours[1])

    print(h, m)

    h_angle = h * 30 + 0.5 * m
    m_angle = m * 6

    print(h_angle, m_angle)

    if h_angle > m_angle:
        angle = h_angle - m_angle
    else:
        angle = m_angle - h_angle

    if angle > 180:
        angle_result = 360 - angle
    else:
        angle_result = angle

    return angle_result
