# Returns value bounded by min and max
def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


# Returns the squared magnitude of a vector
def mag_sq(vec):
    return vec[0]*vec[0] + vec[1]*vec[1]