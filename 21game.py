import random
random_player = random.randint(0,1)
current_number = 0

if random_player == 0:
    current_player = "human"
    print("ban choi truoc")
elif random_player == 1:
    current_player = "computer"
    print("may choi truoc")

while current_number <21:
    if current_player == "human":
        player_choice = int(input("nhap mot so tu 1 den 3: "))
        while player_choice not in [1,2,3]:
            player_choice = int(input("vui long nhap lai: "))
        current_number += player_choice
        print("diem hien tai: ", current_number)
        if current_number >= 21:
            print("ban da thua")
        else:
            current_player = "computer"
    if current_player == "computer":
        computer_choice = random.randint(1,3)
        print("may chon so: ", computer_choice)
        current_number += computer_choice
        print("diem hien tai: ", current_number)
        if current_number >= 21:
            print("ban da thang")
        else:
            current_player = "human"
    if current_number >=21:
        play_again = input("ban co muon choi lai khong: ")
        if play_again == "y":
            random_player = random.randint(0,1)
            current_number = 0
            if random_player == 0:
                current_player = "human"
                print("ban choi truoc")
            elif random_player == 1:
                current_player = "computer"
                print("may choi truoc")
            continue
        elif play_again == "n":
            break
            