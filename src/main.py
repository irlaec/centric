import pandas as pd
import json

from plot import plot_num_coupons_per_type, plot_percent_off_and_dollar_off_stats


def describe_series_to_dict_simplified(describe_series: pd.Series) -> dict:
    print(f"Max discount: {describe_series['max']}")
    print(f"Min discount: {describe_series['min']}")
    print(f"Mean discount: {describe_series['mean']}")
    print(f"Number of coupons: {describe_series['count']}")
    return {
        "max": describe_series["max"],
        "min": describe_series["min"],
        "mean": describe_series["mean"],
        "count": describe_series["count"],
    }


def get_coupons_dataframe() -> pd.DataFrame:
    with open("./data/coupons.json", "r") as file:
        data = json.load(file)
    return pd.json_normalize(data, "coupons")


def get_num_coupons_per_type(coupons_df: pd.DataFrame) -> dict:
    type_counts = coupons_df["promotion_type"].value_counts()
    print(f"Number of coupons for each promotion type:{type_counts}")
    return type_counts.to_dict()


def get_stats_for_percent_off_coupons(coupons_df: pd.DataFrame) -> dict:
    percent_off_coupons = coupons_df[coupons_df["promotion_type"] == "percent-off"]
    percent_off_stats = percent_off_coupons["value"].describe()
    print("\nStats for percent-off coupons:")
    return describe_series_to_dict_simplified(percent_off_stats)


def get_stats_for_dollar_off_coupons(coupons_df: pd.DataFrame) -> dict:
    dollar_off_coupons = coupons_df[coupons_df["promotion_type"] == "dollar-off"]
    dollar_off_stats = dollar_off_coupons["value"].describe()
    print("\nStats for dollar-off coupons:")
    return describe_series_to_dict_simplified(dollar_off_stats)


def get_stats_for_coupons_by_webshop_id(coupons_df: pd.DataFrame) -> dict:
    coupons_by_webshop_id = coupons_df.groupby(["promotion_type", "webshop_id"])[
        "value"
    ]
    coupons_by_webshop_id_stats = coupons_by_webshop_id.describe()
    print("\nStats for dollar-off coupons grouped by webshop_id:")
    results = {}
    for (promotion_type, webshop_id), stats in coupons_by_webshop_id_stats.iterrows():
        if stats["count"]:
            print(f" - Promotion Type: {promotion_type}, Shop Name: {webshop_id}")
            results[f"{webshop_id}/{promotion_type}"] = (
                describe_series_to_dict_simplified(stats)
            )
    return results


def write_results_to_file(results: dict):
    with open("./results/coupon_stats.json", "w") as file:
        json.dump(results, file)


if __name__ == "__main__":
    coupons_df = get_coupons_dataframe()
    results = {
        "num_coupons_per_type": get_num_coupons_per_type(coupons_df),
        "percent_off_coupon_stats": get_stats_for_percent_off_coupons(coupons_df),
        "dollar_off_coupon_stats": get_stats_for_dollar_off_coupons(coupons_df),
        "coupon_stats_by_webshop_id": get_stats_for_coupons_by_webshop_id(coupons_df),
    }
    write_results_to_file(results)

    plot_num_coupons_per_type(results["num_coupons_per_type"])
    plot_percent_off_and_dollar_off_stats(
        results["percent_off_coupon_stats"], results["dollar_off_coupon_stats"]
    )
