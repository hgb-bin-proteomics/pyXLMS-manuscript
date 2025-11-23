#!/usr/bin/env python3
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "biopandas",
# ]
# ///

# Scale BFactor Correctly
# 2025 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

from biopandas.pdb import PandasPdb


def main(argv=None) -> None:
    pdb = PandasPdb().read_pdb("./AlphaLink2_97923.pdb")
    pdb.df["ATOM"]["b_factor"] = pdb.df["ATOM"]["b_factor"].apply(lambda x: x * 100.0)
    pdb.to_pdb(
        path="./AlphaLink2_97923_fixed.pdb", records=None, gz=False, append_newline=True
    )
    return


if __name__ == "__main__":
    main()
