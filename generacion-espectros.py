from simLIBS import SimulatedLIBS
from itertools import combinations, product
import os

def generate_spectra(elements, percentages, file):
    if not os.path.exists(file):
        libs = SimulatedLIBS(
        Te = 1.0,
        Ne = 10**17,
        elements = elements,
        percentages = percentages,
        resolution = 1000,
        low_w = 200,
        upper_w = 1000,
        max_ion_charge = 2,
        webscraping = "static",
        )
        libs.save_to_csv(file)
        libs.plot()
        plt.savefig("alumnio.png")
    return

# Element lists to include in the spectra
elements = ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
concentrations = range(5, 100, 5)

for n in range(1, 4):
    # Create the examples folder if it does not exist
    if not os.path.exists("datos/ejemplos" + str(n)):
        os.makedirs("datos/ejemplos" + str(n))
    # n is the number of elements in the combination.
    elements_combinations = combinations(elements, n)
    percentages_combinations = product(concentrations, repeat = n)
    percentages_combinations = [i for i in percentages_combinations if sum(i) == 100]

    for comb in elements_combinations:
        for perc in percentages_combinations:
            name = "-".join([comb[i] + "-" + str(perc[i]) for i in range(len(comb))])
            generate_spectra(comb, perc, "datos/ejemplos" + str(n) + "/" + name + ".csv")
    
