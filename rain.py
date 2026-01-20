import itertools

def ai_decision(rain, umbrella):

    if rain and not umbrella:

        return "Stay Home "

    elif rain and umbrella:

        return "Go Outside "

    else:

        return "Go Outside "

print("Rain\tUmbrella\tDecision")

print("-"*40)

for rain, umbrella in itertools.product([True, False], repeat=2):

    print(f"{rain}\t{umbrella}\t{ai_decision(rain, umbrella)}")