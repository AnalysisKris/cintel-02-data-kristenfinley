import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset

# Load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# Set the page options for the Shiny app
ui.page_opts(title="Kristen's Penguin Data: Numerical Data Histograms", fillable=True)

# Define the numerical columns. This section is not necessary, but is an artifact from an attempt to render all columns simulatneously.
# numerical_columns = [
#    "bill_length_mm",
#    "bill_depth_mm",
#    "flipper_length_mm",
#    "body_mass_g",
# ]

# Define the layout and the individual plot renderings
with ui.layout_columns():

    # Define individual histogram plots
    @render_plotly
    def plot_bill_length():
        return px.histogram(
            penguins_df, x="bill_length_mm", title="Histogram of Bill Length (mm)"
        )

    @render_plotly
    def plot_bill_depth():
        return px.histogram(
            penguins_df, x="bill_depth_mm", title="Histogram of Bill Depth (mm)"
        )

    @render_plotly
    def plot_flipper_length():
        return px.histogram(
            penguins_df, x="flipper_length_mm", title="Histogram of Flipper Length (mm)"
        )

    @render_plotly
    def plot_body_mass():
        return px.histogram(
            penguins_df, x="body_mass_g", title="Histogram of Body Mass (g)"
        )
