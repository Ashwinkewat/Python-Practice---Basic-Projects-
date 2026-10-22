coding_club = {101, 102, 103, 104, 105, 106}
sports_club = {104, 105, 107, 108, 109}
music_club = {101, 105, 108, 110, 111}
#ans second
x = int(input("enter a roll no to see if its in coding club:"))
# ans first
print("no. of students in coding club:",len(coding_club),"\nroll no's.",coding_club)
print("no. of students in sports club:",len(sports_club),"\nroll no's.",sports_club)
print("no. of students in music club:",len(music_club),"\nroll no's.",music_club)
#ans third
if x in coding_club:
    print("yes he is in coding club")
else:
    print("no he is not in coding club")
print("students that exist in both coding and sports club",coding_club.intersection(sports_club))
#ans fourth
print("students that exist in either coding or music club or in both",coding_club.union(music_club))
# ans fifth
print("students that exist incoding club but not in sports club ",coding_club.difference(sports_club))
# ans sixth
print("students that exist in coding and sports club bot not in both",coding_club.symmetric_difference(sports_club))
#ans seventh thala for a reason
print("students that exist in all three",coding_club|sports_club|music_club)
#ans eighth
a = sports_club&coding_club
b = coding_club&music_club
c = music_club&sports_club
print("students that belongs in more than one club:",a|b|c)
#ans ninth 
coding_list = list(coding_club)
print("coding club converted into list:",coding_list)
#ans tenth
y = set(input("enter a roll no. to see if its in sports club to remove it"))
print("updated sports set:",sports_club.difference(y))
        