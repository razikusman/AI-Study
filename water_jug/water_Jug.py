import jug
import sys

print("Water Jug Problem"); 

print("op-A = jug is empty fill it."); 
print("op-B = transfer water"); 
print("op-C = if the jug is full emty it"); 

cap_X = int(input("capacity of Jug X : "));
cap_Y = int(input("capacity of Jug Y : "));

if cap_X == cap_Y:
    print('jugs can\'t have equal capacity')
    sys.exit(1)

tv = int(input("target volume : "));

if tv > cap_X and tv > cap_Y:
    print('target volume can\'t be larger than jug capacities')
    sys.exit(1)

smaller = jug.Jug(min(cap_X, cap_Y), 'Jug 1')

action_count = [0, 0]

larger = jug.Jug(max(cap_X, cap_Y), 'Jug 2')


def getGCD(a, b):
    larger = max(a, b)
    smaller = min(a, b)
    if larger != smaller:
        smaller = getGCD(larger - smaller, smaller)
    return smaller


def execute(smaller, larger):
    
    if smaller.is_empty():
        smaller.fill()
        action_count[0] += 1
        print('op-A -> [', smaller.current_volume, ',', larger.current_volume,']')
        return True
  
    if larger.is_full():
        larger.dump()
        action_count[1] -= 1
        print('op-B -> [', smaller.current_volume, ',', larger.current_volume,']')
        return True

    if not(smaller.is_empty()):
        smaller.transfer(larger)
        print('op-op-C -> [', smaller.current_volume, ',', larger.current_volume,']')
        return True

def executes(smaller, larger):
    
    if larger.is_empty():
        larger.fill()
        action_count[0] += 1
        print('op-A -> [', smaller.current_volume, ',', larger.current_volume,']')
        return True
  
    if smaller.is_full():
        smaller.dump()
        action_count[1] -= 1
        print('op-B -> [', smaller.current_volume, ',', larger.current_volume,']')
        return True

    if not(larger.is_empty()):
        larger.transfers(smaller)
        print('op-op-C -> [', smaller.current_volume, ',', larger.current_volume,']')
        return True


gcd = getGCD(smaller.capacity, larger.capacity)

if tv % gcd != 0:
    print('no solution possible')
    sys.exit(0)

found_it = (smaller.current_volume + larger.current_volume) == tv
step_count = 0
while not(found_it):
    execute(smaller, larger)
    step_count += 1

    found_it = (smaller.current_volume + larger.current_volume) == tv

print("__________________________________________________________________")
smaller.current_volume = larger.current_volume = 0
found_its = (smaller.current_volume + larger.current_volume) == tv
step_counts = 0
while not(found_its):
    executes(smaller, larger)
    step_counts += 1

    found_its = (smaller.current_volume + larger.current_volume) == tv


print("__________________________________________________________________")
print('found target volume in', step_count, 'steps')
print('found target volume in', step_counts, 'steps')


# print(action_count)