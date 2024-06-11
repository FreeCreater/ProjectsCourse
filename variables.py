# Через какое время T лиса догонит зайца,
# если скорость V зайца (вводится с клавиатуры),
# скорость V лисы (вводится с клавиатуры),
# а начальное расстояние S между ними (вводится с клавиатуры) м?

hare_speed = int(input('enter hare speed: '))
fox_speed = int(input('enter hare speed: '))
delta_speed = fox_speed - hare_speed
distance = int(input('enter distance: '))
time = distance/delta_speed
print(f'fox catches hare in {time} seconds')



