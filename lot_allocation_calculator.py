def compute_min_max_allocations(total_area_ha):
    """
    Compute min/max area allocations (in hectares) for subdivision components
    based on PD 957 regulatory percentage ranges.
    """

    # Regulatory percentage bounds (decimals)
    P_rd_min, P_rd_max = 0.25, 0.30     # Roads & alleys
    P_os_min, P_os_max = 0.30, 0.40     # Open space (parks/playgrounds)
    P_cf_min, P_cf_max = 0.01, 0.03     # Community facilities
    P_ut_min, P_ut_max = 0.02, 0.03     # Utilities/setbacks/drainage

    # Compute component area ranges
    area = {}
    area['roads_min']         = total_area_ha * P_rd_min
    area['roads_max']         = total_area_ha * P_rd_max
    area['open_space_min']    = total_area_ha * P_os_min
    area['open_space_max']    = total_area_ha * P_os_max
    area['comm_fac_min']      = total_area_ha * P_cf_min
    area['comm_fac_max']      = total_area_ha * P_cf_max
    area['utilities_min']     = total_area_ha * P_ut_min
    area['utilities_max']     = total_area_ha * P_ut_max

    # Residual (saleable) area = 1 − sum(other percentages)
    pct_others_max = P_rd_max + P_os_max + P_cf_max + P_ut_max
    pct_others_min = P_rd_min + P_os_min + P_cf_min + P_ut_min

    area['saleable_min'] = total_area_ha * (1.0 - pct_others_max)
    area['saleable_max'] = total_area_ha * (1.0 - pct_others_min)

    return area


if __name__ == "__main__":
    # Example: 5 hectares total
    total_area = 10
    allocations = compute_min_max_allocations(total_area)

    print(f"Land-use allocation ranges for {total_area} ha:")
    for comp, ha in allocations.items():
        print(f"  • {comp.replace('_',' ').title()}: {ha:.3f} ha")
