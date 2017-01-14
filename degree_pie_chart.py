import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg') #working on vagrant/headless
import matplotlib.pyplot as plt
# import gapjump
from collections import Counter
# degree data
# z = gapjump.count_degrees

def create_pie_chart(z):
    """Creating pie chart of edu degrees using matplotlib in vm environment, 
       saving it to file"""
    # Data to plot
    degree_counts = Counter(z) # degree data counted
    labels = 'BA/BS', 'MA/MS', 'MBA', 'PhD', 'None'
    colors = ['purple', 'blue', 'green', 'red', 'yellow']
    explode = (0.1, 0, 0, 0, 0)  # explode 1st slice
    sizes = [degree_counts["BA/BS"],degree_counts["MA/MS"],degree_counts["MBA"],degree_counts["PhD"],degree_counts["None"]]

    plt.figure()
    slices, text1, text2 = plt.pie(sizes, colors=colors, explode=explode,autopct='%1.1f%%',shadow=True, startangle=90)
    plt.legend(slices, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.title("Degree Breakdown")
    # saving to file/ working on vagrant/headless machine
    plt.savefig('degree_pie.png')
