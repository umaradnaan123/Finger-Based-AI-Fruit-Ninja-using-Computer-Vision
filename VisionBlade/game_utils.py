def line_intersects_rect(p1, p2, rect):
    if not p1 or not p2:
        return False

    x1, y1, x2, y2 = rect

    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])

    return not (max_x < x1 or min_x > x2 or max_y < y1 or min_y > y2)
