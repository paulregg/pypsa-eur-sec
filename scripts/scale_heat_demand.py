#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:34:29 2022

@author: Paul
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
