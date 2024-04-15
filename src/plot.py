import seaborn as sns
import matplotlib.pyplot as plt


def plot_num_coupons_per_type(num_coupons_per_type: dict):
    types = list(num_coupons_per_type.keys())
    counts = list(num_coupons_per_type.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=types, y=counts, hue=types, palette='viridis', dodge=False, legend=False)

    plt.xlabel('Coupon Type')
    plt.ylabel('Number of Coupons')
    plt.title('Number of Coupons per Type')

    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig('results/coupons_per_type.png')


def plot_percent_off_and_dollar_off_stats(percent_off_stats: dict, dollar_off_stats: dict):
    stats_names = list(percent_off_stats.keys())
    percent_off_values = list(percent_off_stats.values())
    dollar_off_values = list(dollar_off_stats.values())

    plt.figure(figsize=(10, 6))
    plt.bar(stats_names, percent_off_values, color='skyblue', alpha=0.5, label='Percent-off')
    plt.bar(stats_names, dollar_off_values, color='orange', alpha=0.5, label='Dollar-off')

    plt.xlabel('Statistics')
    plt.ylabel('Values')
    plt.title('Comparison of Coupon Statistics')
    plt.legend()

    plt.tight_layout()
    plt.savefig('results/percent_vs_dollar_off.png')
