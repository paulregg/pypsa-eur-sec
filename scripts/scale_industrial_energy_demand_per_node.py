"""
scale (and possibly reshape) the default industry demand time series
"""

import shutil

if __name__ == "__main__":
    if "snakemake" not in globals():
        from helper import mock_snakemake

        snakemake = mock_snakemake(
            "industrial_energy_demand_per_node",
            simpl="",
            clusters=48,
        )

shutil.copy2(snakemake.input.industrial_energy_demand_per_node_unscaled, snakemake.output.industrial_energy_demand_per_node)
