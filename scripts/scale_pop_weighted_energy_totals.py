"""
Scale energy totals
"""

import shutil
import pandas as pd

if __name__ == "__main__":
    if "snakemake" not in globals():
        from helper import mock_snakemake

        snakemake = mock_snakemake(
            "scale_pop_weighted_energy_totals",
            simpl="",
            clusters=37,
        )

#shutil.copy2(snakemake.input.pop_weighted_energy_totals_unscaled, snakemake.output[0])

data = pd.read_csv(snakemake.input.pop_weighted_energy_totals_unscaled,index_col=0).T
scaling = pd.read_csv(snakemake.input.scaling,index_col=0)
scaling = scaling.fillna(1).T

if snakemake.config["scaling"]["energy_totals"]["by_nation"]:
    
    node_names = data.columns
    
    for nation in scaling.columns[:-1]:
        national_nodes = [n for n in node_names if n.startswith(nation)]
        
        if snakemake.config["scaling"]["energy_totals"]["by_sector"]:
            for sector in data.index:
                data.loc[sector,national_nodes]*=scaling.loc[sector,nation]
        else:
            data[national_nodes] *= scaling[nation]["all_sectors"]
    
else:
    if snakemake.config["scaling"]["energy_totals"]["by_sector"]:
        for sector in data.index:
            if sector == "total international navigation":
                x=0
            data.loc[sector]*=scaling.loc[sector]["all_countries"]
    else:
        data = data * snakemake.config["scaling"]["energy_totals"]["total"]
        
data = data.T
data.to_csv(snakemake.output[0],float_format="%.4f")