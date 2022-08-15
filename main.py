A = "A"
S = "S"


class Times:
    def with_scooter(scooter):
        return scooter[A] * 5 + scooter[S] * 40

    def by_foot(foot):
        return foot[A] * 20 + foot[S] * 30


#%%
def solution(road):
    min_scooter = {A: 0, S: 0}
    scooter = {A: 0, S: 0}

    foot = {A: 0, S: 0}
    for r in road:
        foot[r] += 1

    min_foot = foot.copy()

    for r in road:
        scooter[r] += 1
        foot[r] -= 1
        if (Times.with_scooter(scooter) + Times.by_foot(foot)) < (
            Times.with_scooter(min_scooter) + Times.by_foot(min_foot)
        ):
            min_scooter = scooter.copy()
            min_foot = foot.copy()
    return Times.with_scooter(min_scooter) + Times.by_foot(min_foot)
