def SD(L):
    avg = sum(L) / len(L)
    tot = 0
    for i in L:
        x = (i - avg) ** 2
        tot += x
    sd = (tot / len(L)) ** 0.5
    return sd, avg


def calculate_zscore(avgphy, sdphy, avgchem, sdchem, avgmath, sdmath):
    with open("zscore.txt", "w", encoding="utf-8") as file:
        while True:
            name = input("Enter name (or 'end' to finish): ")
            if name == 'end':
                break

            phymark = int(input("Enter physics mark: "))
            chemmark = int(input("Enter chemistry mark: "))
            mathmark = int(input("Enter maths mark: "))

            # Calculate z-score with protection against division by zero
            z_phy = (phymark - avgphy) / sdphy if sdphy != 0 else 0
            z_chem = (chemmark - avgchem) / sdchem if sdchem != 0 else 0
            z_math = (mathmark - avgmath) / sdmath if sdmath != 0 else 0

            z_score = (z_phy + z_chem + z_math) / 3
            file.write(f"{name}: {z_score:.2f}\n")
            print(f"{name}'s Z-score: {z_score:.2f}")
            print(f"  Physics Z-score: {z_phy:.2f}")
            print(f"  Chemistry Z-score: {z_chem:.2f}")
            print(f"  Math Z-score: {z_math:.2f}")


lphy = [int(i)
        for i in input("Enter physics marks separated by space: ").split()]
lchem = [int(i) for i in input(
    "Enter chemistry marks separated by space: ").split()]
lmath = [int(i)
         for i in input("Enter maths marks separated by space: ").split()]
sdphy, avgphy = SD(lphy)
sdchem, avgchem = SD(lchem)
sdmath, avgmath = SD(lmath)

print(f"Physics - Average: {avgphy:.2f}, Standard Deviation: {sdphy:.2f}")
print(f"Chemistry - Average: {avgchem:.2f}, Standard Deviation: {sdchem:.2f}")
print(f"Math - Average: {avgmath:.2f}, Standard Deviation: {sdmath:.2f}")

calculate_zscore(avgphy, sdphy, avgchem, sdchem, avgmath, sdmath)
