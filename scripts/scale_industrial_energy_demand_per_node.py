"""
scale (and possibly reshape) the default industry demand time series
"""

import shutil
import pandas as pd

if __name__ == "__main__":
    if "snakemake" not in globals():
        from helper import mock_snakemake

        snakemake = mock_snakemake(
            "scale_industrial_energy_demand_per_node",
            simpl="",
            clusters=37,
        )

shutil.copy2(snakemake.input.industrial_energy_demand_per_node_unscaled, snakemake.output.industrial_energy_demand_per_node)
