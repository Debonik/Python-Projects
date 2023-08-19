# Description of the Code
## Here's what the code does:

-   The **generate_data function** uses the Faker library to generate a
    > list of random names, and uses the random.randint function to
    > generate random marks (between 50 and 100) in three subjects for
    > the given number of students.

-   The **plot_histogram function** takes the generated data and creates
    > a histogram for each subject using **plt.hist**. The alpha
    > parameter is used to set the transparency level (so that
    > overlapping parts of the histograms are visible). A legend is
    > created using **plt.legend** and the axes are labelled using
    > **plt.xlabel** and **plt.ylabel**. The histogram is displayed with
    > **plt.show()**.

-   The data is generated and plotted by calling the **generate_data**
    > and **plot_histogram** functions at the end of the script.

-   The resulting plot gives an overview of how students in the class
    > are performing in the three subjects.
