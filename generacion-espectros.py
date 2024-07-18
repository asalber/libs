from simLIBS import SimulatedLIBS
from itertools import combinations, product
import os

# Create the examples folder if it does not exist
if not os.path.exists("datos/ejemplos"):
    os.makedirs("datos/ejemplos")

def generate_spectra(elements, percentages):
    name = "-".join([elements[i] + "-" + str(percentages[i]) for i in range(len(elements))])
    if not os.path.exists("datos/ejemplos/" + name + ".csv"):
        libs = SimulatedLIBS(
        Te = 1.0,
        Ne = 10**17,
        elements = elements,
        percentages = percentages,
        resolution = 1000,
        low_w = 200,
        upper_w = 1000,
        max_ion_charge = 3,
        webscraping = "static",
        )
        libs.save_to_csv("datos/ejemplos/" + name + ".csv")
    return

# Element lists to include in the spectra
elements = ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
concentrations = range(5, 100, 5)


elements_combinations = combinations(elements, 3)
percentages_combinations = product(concentrations, repeat = 3)
percentages_combinations = [i for i in percentages_combinations if sum(i) == 100]

for comb in elements_combinations:
    for perc in percentages_combinations:
        generate_spectra(comb, perc)
    

