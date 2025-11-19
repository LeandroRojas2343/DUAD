
class Head:
    def __init__(self):
        self.eyes = 2
        self.mouth = 1
        self.nose = 1

class Hand:
    def __init__(self):
        self.fingers = 5

class Arm:
    def __init__(self, hand):
        self.hand = hand
        self.elbow = True

class Foot:
    def __init__(self):
        self.toes = 5

class Leg:
    def __init__(self, foot):
        self.foot = foot
        self.knee = True

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg

class Human:
    def __init__(self):
        # Create individual parts
        self.head = Head()
        
        self.left_hand = Hand()
        self.right_hand = Hand()
        
        self.left_arm = Arm(self.left_hand)
        self.right_arm = Arm(self.right_hand)
        
        self.left_foot = Foot()
        self.right_foot = Foot()
        
        self.left_leg = Leg(self.left_foot)
        self.right_leg = Leg(self.right_foot)
        
        # Connect everything to the torso
        self.torso = Torso(
            self.head,
            self.left_arm,
            self.right_arm,
            self.left_leg,
            self.right_leg
        )

# Create a human
person = Human()

# Access parts
print("Fingers on right hand:", person.right_arm.hand.fingers)
print("Toes on left foot:", person.left_leg.foot.toes)



