import math


def area_of_surface(length, height):
    return length * height


def cans_needed(area, coverage):
    return math.ceil(area / coverage)


def cost_of_job(args):
    total_cans = cans_needed((area_of_surface(args['width'], args['height'])-args['door_area']), args['coverage'])
    total_cost = total_cans * args['cost']
    return total_cost


def door_area(width=1.5, height=2):
    return area_of_surface(width, height)


def job_vals():
    wi = float(input("wall width "))
    he = float(input("wall height "))
    cov = float(input("How much does one can cover ?"))
    cos = float(input("How much does a can cost "))
    d = int(input("How many doors "))
    td_area = 0
    if d > 0:
        for dr in range(int(d)):
            td_area += door_area()
    pms = {}
    if wi > 0:
        if he > 0:
            if cos > 0:
                if cov > 0:
                    if td_area >0:
                        pms['width'] = wi
                        pms['height'] = he
                        pms['coverage'] = cov
                        pms['cost'] = cos
                        pms['door_area'] = td_area
    return pms


def cost_job():
    return cost_of_job(job_vals())