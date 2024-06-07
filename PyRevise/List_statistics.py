def analyze_list(numbers):
    lmin = min(numbers)
    lmax = max(numbers)
    lmean = sum(numbers) / len(numbers)
    
    stats = {
        "min": lmin,
        "max": lmax,
        "mean": lmean
    }
    
    return stats

numbers = [500, 900, 340, 210, 560]
stats = analyze_list(numbers)
print(f"List statistics: {stats}")
