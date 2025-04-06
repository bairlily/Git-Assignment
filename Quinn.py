from bair import rect_area
def rect_surface_area(length, width, height):
    return 2*rect_area(length, width)+2*rect_area(height, width)+2*rect_area(length,height)