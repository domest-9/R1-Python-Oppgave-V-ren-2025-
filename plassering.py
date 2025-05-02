import matplotlib.pyplot as plt
import numpy as np

def main():  
  # Data
    land = ['Norge', 'Sverige']
    første_plass = [3, 7]
    andre_plass = [1, 1]
    tredje_plass = [1, 4]

# Bredde på søylene
    bar_width = 0.25

# lager en liste for å plassere søylene riktig
    liste = np.arange(len(land))

# Plot
    plt.figure(figsize=(8, 6))

# Søylene for 1., 2. og 3. plass
    plt.bar(liste, første_plass, bar_width, label='1. plass', color='gold')
    plt.bar(liste + bar_width, andre_plass, bar_width, label='2. plass', color='silver')
    plt.bar(liste + 2 * bar_width, tredje_plass, bar_width, label='3. plass', color='#CD7F32')
  
    
    
    #style og graf
    plt.xlabel('Land')
    plt.ylabel('Antall')
    plt.title('Norge vs Sverige i Eurovision')
    plt.xticks(liste + bar_width, land) # x-akse  '
    plt.legend()
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
    print(len(1,2,3))


