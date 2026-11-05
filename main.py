"""A choose-your-own-adventure story about a corgi's trip to the vet."""

HEIGHT_M = 0.2
HEALTHY_MIN_KG = 10
HEALTHY_MAX_KG = 16
EXERCISES = ("agility training", "dog dancing", "fetching balls")
COUNTDOWN_START = 3
FEE_PER_VISIT = 1_000_000


def calculate_bmi(weight_kg: float) -> float:
    """Return the BMI of a dog of height HEIGHT_M weighing weight_kg."""
    return weight_kg / HEIGHT_M**2


HEALTHY_MIN_BMI = calculate_bmi(HEALTHY_MIN_KG)
HEALTHY_MAX_BMI = calculate_bmi(HEALTHY_MAX_KG)


def ask_text(prompt: str) -> str:
    """Prompt until the player enters some text."""
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("Please type an answer.")


def ask_weight(prompt: str) -> float:
    """Prompt until the player enters a positive weight in kilograms."""
    while True:
        try:
            weight_kg = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if 0 < weight_kg < float("inf"):
            return weight_kg
        print("Please enter a weight above zero.")


def ask_exercise(prompt: str) -> str:
    """Show the exercises and prompt until the player picks a valid one."""
    for number, exercise in enumerate(EXERCISES, start=1):
        print(f"{number}: {exercise}")

    while True:
        try:
            choice = int(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue
        if 1 <= choice <= len(EXERCISES):
            return EXERCISES[choice - 1]
        print(f"Please choose a number from 1 to {len(EXERCISES)}.")


def meet_the_dog() -> tuple[str, str]:
    """Open the story and return the dog's name and favourite snack."""
    print("There was once a very happy corgi dog named")
    name = ask_text("What's the dog's name? ")
    print(f"{name} loves to eat snacks. His favourite snack is")
    snack = ask_text(f"What's {name}'s favourite snack? ")
    print(f"{name} ate so much {snack} that he was becoming very chonky")
    return name, snack


def first_vet_visit(name: str, snack: str) -> float:
    """Tell the story of the first weigh-in and return the dog's BMI."""
    print(
        "His pawrents were starting to get concerned, so they took him to the "
        "vet, when he stepped on the scale he weighed"
    )
    weight_kg = ask_weight(f"How many kilos does {name} weigh? ")
    print(
        f"{weight_kg}kg! That is very heavy for a dog who is only "
        f"{HEIGHT_M} metres tall."
    )
    bmi = calculate_bmi(weight_kg)
    print(
        f"{name} is the fattest dog I have ever seen! His BMI is {bmi:.1f}. "
        f"He must exercise and not eat any more {snack}. You will have to "
        f"bring him back each month until his BMI is between "
        f"{HEALTHY_MIN_BMI:.0f} and {HEALTHY_MAX_BMI:.0f}."
    )
    return bmi


def choose_exercise(name: str) -> str:
    """Let the player pick an exercise for the dog and return it."""
    print(f"{name} was very sad. He needs help thinking of a fun exercise he could do:")
    exercise = ask_exercise(f"Which exercise should {name} do? ")
    print(f"{exercise}! {name} will love that!")
    print(
        f"{name} and his pawrents had a lot of fun doing {exercise} "
        "for hours and hours and hours each day"
    )
    print("Soon it was time to go back to the vet")
    return exercise


def describe_weigh_in(name: str, snack: str, exercise: str, bmi: float) -> None:
    """Print the vet's verdict for a follow-up weigh-in."""
    if bmi > HEALTHY_MAX_BMI:
        print(
            f"oh dear. {name} is still very chonky! {name} has a BMI of "
            f"{bmi:.1f}. Keep exercising and come back next month to weigh "
            f"{name} again"
        )
        print(
            f"so {name} went back home again. Huffing and puffing he did "
            f"{exercise} over and over and over. He certainly ate no {snack}"
        )
        print(f"before {name} knew it, it was time to go back to the vet again")
    elif bmi < HEALTHY_MIN_BMI:
        print(
            f"Uh oh {name}, you have done so much {exercise}, that you are now "
            f"too skinny. Your BMI is {bmi:.1f}. You need to go home, relax and "
            f"eat some {snack}. Come back again next month to try again."
        )
    else:
        print(
            f"Oh {name}, you have done a very good job. You are now a healthy "
            f"weight! You can go home and eat {snack} now sometimes again"
        )


def follow_up_visits(name: str, snack: str, exercise: str, bmi: float) -> int:
    """Repeat vet visits until the BMI is healthy and return the visit count."""
    visits = 1
    while not HEALTHY_MIN_BMI <= bmi <= HEALTHY_MAX_BMI:
        print(
            f"When {name} went back to the vet, the vet said: let's get {name} "
            "on the scale and see what he weighs now"
        )
        bmi = calculate_bmi(ask_weight(f"How many kilos does {name} weigh now? "))
        visits += 1
        describe_weigh_in(name, snack, exercise, bmi)
    return visits


def finish_story(name: str, visits: int) -> None:
    """Take the victory photo and present the bill."""
    print(
        "I would love to take a picture of you to put on the wall and inspire "
        "the other chonky dogs. Smile for the camera!"
    )
    for count in range(COUNTDOWN_START, 0, -1):
        print(count)
    print("Flash! That is a great photo, thank you.")
    print(
        f"By the way {name}'s weight loss journey took {visits} vet visits! "
        f"That will be {visits * FEE_PER_VISIT}$"
    )


def main() -> None:
    """Play the story from start to finish."""
    name, snack = meet_the_dog()
    bmi = first_vet_visit(name, snack)
    exercise = choose_exercise(name)
    visits = follow_up_visits(name, snack, exercise, bmi)
    finish_story(name, visits)


if __name__ == "__main__":
    main()