import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return ()


def lines(cue_angle, cue_ball_center, second_ball_center):
    print(cue_angle)
    lower_ball_angle = ((second_ball_center[1]-1)-cue_ball_center[1])/((second_ball_center[0]-1)-cue_ball_center[0])
    upper_ball_angle = ((second_ball_center[1]+1)-cue_ball_center[1])/((second_ball_center[0]+1)-cue_ball_center[0])
    lines = []
    lines.append((math.tan(math.radians(cue_angle)), cue_ball_center, (cue_ball_center[1] - cue_ball_center[0]*math.tan(math.radians(cue_angle)))))

    #building quadratic equation
    a = 1 + lines[0][0]**2
    b = (-2*second_ball_center[0]) + (2*lines[0][0]* lines[0][2]) - (2*lines[0][0]*second_ball_center[1])
    c = second_ball_center[0]**2 + second_ball_center[1]**2 + lines[0][2]**2 - (2*lines[0][2]*second_ball_center[1]) - (0.5625*4)#accounting for the first ball not being a point object
    roots = solve_quadratic_equation(a, b, c)
    if len(roots) == 2:
        collision_point = 0
        if cue_ball_center[0] < second_ball_center[0]:
            collision_point = roots[0] if roots[0]<roots[1] else roots[1]
        else:
            collision_point = roots[1] if roots[0]<roots[1] else roots[0]
        m = (second_ball_center[1] - (lines[0][0]*collision_point + lines[0][2]))/(second_ball_center[0]-collision_point)
        lines.append((m, second_ball_center, (second_ball_center[1] - second_ball_center[0]*m)))
        last_point = extend_line((collision_point, (lines[0][0]*collision_point + lines[0][2])), second_ball_center, m, lines[1][2])
        #last_point = extend_line(m, lines[1][2])
        print(collision_point)
        x_plot = [cue_ball_center[0], collision_point, second_ball_center[0], last_point[0]]
        y_plot = [cue_ball_center[1], (lines[0][0]*collision_point + lines[0][2]), second_ball_center[1], last_point[1]]
    elif len(roots) == 1:
        collision_point = roots[0]
        m = (second_ball_center[1] - (lines[0][0]*collision_point + lines[0][2]))/(second_ball_center[0]-collision_point)
        lines.append((m, second_ball_center, (second_ball_center[1] - second_ball_center[0]*m)))
        last_point = extend_line((collision_point, (lines[0][0]*collision_point + lines[0][2])), second_ball_center, m, lines[1][2])
        #last_point = extend_line(m, lines[1][2])
        #print(collision_point)
        x_plot = [cue_ball_center[0], collision_point, second_ball_center[0], last_point[0]]
        y_plot = [cue_ball_center[1], (lines[0][0]*collision_point + lines[0][2]), second_ball_center[1], last_point[1]]
    else:
        last_point = extend_line1(cue_angle, lines[0][2])
        x_plot = [cue_ball_center[0], last_point[0]]
        y_plot = [cue_ball_center[1], last_point[1]]
    
    return (x_plot, y_plot)

def extend_line(point1, point2, m, c):
    if point1[0] < point2[0]:
        x = 1000
    else:
        x = -1000
    y = m*x + c
    return (x,y)
def extend_line1(cue_angle, c):
    if cue_angle in range(-180,0) or cue_angle in range(180, 360)  :
        x = -1000
    else:
        x = 1000
    y = (math.tan(math.radians(cue_angle)))*x + c
    return (x,y)
    
    


    

