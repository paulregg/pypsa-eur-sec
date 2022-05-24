#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:53:58 2022

@author: Paul
"""

import shutil


if __name__ == "__main__":
    if "snakemake" not in globals():
        from helper import mock_snakemake

        snakemake = mock_snakemake(
            "scale_transport_demand",
            simpl="",
            clusters=48,
        )


shutil.copy2(snakemake.input.transport_demand_unscaled, snakemake.output.transport_demand)
shutil.copy2(snakemake.input.transport_data_unscaled, snakemake.output.transport_data)
shutil.copy2(snakemake.input.avail_profile_unscaled, snakemake.output.avail_profile)
shutil.copy2(snakemake.input.dsm_profile_unscaled, snakemake.output.dsm_profile)

