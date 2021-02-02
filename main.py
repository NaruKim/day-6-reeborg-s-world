def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while wall_on_right():
        while wall_in_front():
            turn_left()
        move()
    if not at_goal():
        turn_right()
        move()

#2021-02-02 퇴근, 운동후 시작해서 지금 2106 이니까, 세 시간 걸렸다. 그러고 보니 일도 세시간 자고 나갔었네. 잠은 달아났어. 이렇게 쉬운 것도 못해서 열등감이 들었는데, 정작 강의를 들어보니 어려운 문제니까 넘어가라고 했다. 편법을 쓴 것 같긴 한데, 해결은 했어.