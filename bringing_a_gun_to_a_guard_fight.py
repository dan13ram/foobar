from math import *

DISTANCE    = 0
SOURCE      = (0,0)
TARGET      = (0,0)
BOTTOM_LEFT = (0,0)
BOTTOM_RIGHT= (0,0)
TOP_RIGHT   = (0,0)
TOP_LEFT    = (0,0)

def getAngle(point):
    return degrees(atan2(point[1] - SOURCE[1], point[0] - SOURCE[0]))

def answer(tr, src, bp, dist):
    global BOTTOM_LEFT
    BOTTOM_LEFT = (0,0)
    global TOP_RIGHT
    TOP_RIGHT = tr
    global SOURCE
    SOURCE = src
    global TARGET
    TARGET = bp
    global DISTANCE
    DISTANCE = dist
    global BOTTOM_RIGHT
    BOTTOM_RIGHT = (TOP_RIGHT[0], BOTTOM_LEFT[1])
    global TOP_LEFT
    TOP_LEFT = (BOTTOM_LEFT[0], TOP_RIGHT[1])
    all_targets = get_targets(start_point = TARGET, distance = DISTANCE)
    all_targets_source = get_targets(start_point = SOURCE, distance = DISTANCE)

    tgt_angles = set()
    src_angles = set()
    tgt_mapping = {}
    src_mapping = {}
    for tgt in all_targets:
        tgt_angles.add(getAngle(tgt))
        if getAngle(tgt) not in tgt_mapping:
            tgt_mapping[getAngle(tgt)] = tgt

    for src in all_targets_source:
        src_angles.add(getAngle(src))
        if getAngle(src) not in src_mapping:
            src_mapping[getAngle(src)] = src

    intersect_set = tgt_angles.intersection(src_angles)
    excluder = 0
    removed = {}
    for angle in intersect_set:
        src_point = src_mapping[angle]
        tgt_point = tgt_mapping[angle]
        if(src_point != SOURCE) and (hypot(src_point[0] - SOURCE[0], src_point[1] - SOURCE[1]) < hypot(tgt_point[0] - SOURCE[0], tgt_point[1] - SOURCE[1])) and (hypot(src_point[0] - tgt_point[0], src_point[1] - tgt_point[1]) <= DISTANCE):
            excluder += 1

    if(SOURCE == TARGET):
        return 0
    print len(tgt_angles)
    return len(tgt_angles) - excluder

def get_mirrored(point):
    ret = []
    ret.append((point[0], point[1] - 2*(point[1] - TOP_RIGHT[1])))
    ret.append((point[0], point[1] - 2*(point[1] - BOTTOM_LEFT[1])))
    ret.append((point[0] - 2*(point[0] - BOTTOM_LEFT[0]), point[1]))
    ret.append((point[0] - 2*(point[0] - TOP_RIGHT[0]), point[1]))
    return ret

def get_targets(start_point, distance):
    targets = []
    targets.append(start_point)
    all_targets = set()
    all_targets.add((start_point[0],start_point[1]))
    last_targets = all_targets
    while True:
        new_level_targets = set()
        for tgt in last_targets:
            new_targets = get_mirrored(tgt)
            new_targets = set(t for t in new_targets if hypot(SOURCE[0] - t[0], SOURCE[1] - t[1]) <= DISTANCE)
            new_targets -= all_targets
            new_level_targets |= new_targets
        if not new_level_targets:
            break
        all_targets |= new_level_targets
        last_targets = new_level_targets
    return all_targets

#print (answer((3,2), (1,1), (1,1), 4)) #Answer 0
#print (answer((3,2), (1,1), (2,1), 4)) #Answer 7
#print (answer((300,275), (150,150), (185,100), 500)) #Answer 9
#print (answer((2,5), (1,2), (1,4), 11)) #Answer 27
print (answer((42, 59), (34, 44), (6, 34), 5000)) #Answer 30895 (incorrect) should be 30904
