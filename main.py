#choose your adventure story 
print("There was once a very happy corgi dog named")
name = input("What's the dog's name?")
print(f"{name} loves to eat snacks. His favourite snack is")
favourite_snack = input(f"What's {name}'s favourite snack?")
print(f"{name} ate so much {favourite_snack} that he was becoming very chonky")
print("His pawrents were starting to get concerned, so they took him to the vet, when he stepped on the scale he weighed")
weight = float(input(f"How many kilo's does {name} weigh?"))
height = .2
print(f"{weight}kg! That is very heavy for a dog who is only {height} metres tall.")
bmi = weight / (height ** 2)
healthy_min = 10 / (height ** 2)
healthy_max = 16 / (height ** 2)
print(f"{name} is the fattest dog I have ever seen! His BMI is {bmi:.1f}. He must exercise and not eat any more {favourite_snack}. You will have to bring him back each month until his BMI is between {healthy_min:.0f} and {healthy_max:.0f}.")
print(f"{name} was very sad. He needs help thinking of a fun exercise he could do:")
exercises = ["agility training", "dog dancing", "fetching balls"]
for i, exercise in enumerate(exercises, start=1):
    print(f"{i}: {exercise}")
exercise_choice = int(input(f"Which exercise should {name} do?"))
chosen_exercise = exercises [exercise_choice - 1]
print(f"{chosen_exercise}! {name} will love that!")
print(f"{name} and is pawrents had a lot of fun doing {chosen_exercise} for hours and hours and hours each day")
print("Soon it was time to go back to the vet")

weigh_ins = [weight]
while bmi > healthy_max or bmi < healthy_min:
    print(f"When {name} went back to the vet, the vet said: let's get {name} on the scale and see what he weighs now")
    weight = float(input(f"How many kilo's does {name} weigh now?"))
    bmi = weight / (height ** 2)
    weigh_ins.append(weight)

    if bmi > healthy_max:
        print(f"oh dear. {name} is still very chonky! {name} has a BMI of {bmi:.1f}. Keep exercising and back next month to weigh {name} again")
        print(f"so {name} went back home again. Huffing and puffing he did {chosen_exercise} over and over and over. He certainly ate no {favourite_snack}")
        print(f"before {name} knew it, it was time to go back to the vet again")

    elif healthy_min <= bmi <= healthy_max:
        print(f"Oh {name}, you have done a very good job. You are now a healthy weight! You can go home and eat {favourite_snack} now sometimes again")

    else:
        print(f"Uh oh {name}, you have done so much {chosen_exercise}, that you are now too skinny. Your BMI is {bmi:.1f}. You need to go home, relax and eat some {favourite_snack}. Come back again next month to try again.")

print("I would love to take a picture of you to put on the wall and inspire the other chonky dogs. Smile for the camera!")
countdown = [3, 2, 1]
for count in countdown:
    print(count)
print("Flash! That is a great photo, thank you.")
print(f"By the way {name}'s weight loss journey took {len(weigh_ins)} vet visits! That will be {len(weigh_ins) * 1000000}$")
