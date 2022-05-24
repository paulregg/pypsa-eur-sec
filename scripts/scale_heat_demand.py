"""
scale (and possibly reshape) the default heat demand time serieses
"""
import shutil

if __name__ == "__main__":
    if "snakemake" not in globals():
        from helper import mock_snakemake

        snakemake = mock_snakemake(
            "scale_heat_demand",
            simpl="",
            clusters=48,
        )

shutil.copy2(snakemake.input.heat_demand_urban_unscaled,snakemake.output.heat_demand_urban)
shutil.copy2(snakemake.input.heat_demand_rural_unscaled,snakemake.output.heat_demand_rural)
shutil.copy2(snakemake.input.heat_demand_total_unscaled,snakemake.output.heat_demand_total)
