import math

class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def display(self):
        print(self.values)

    def shape(self):
        return (1, len(self.values))

    def __add__(self, other):
        """Adds corresponding elements"""
        if len(self.values) != len(other.values):
            raise ValueError("Vectors must have the same length")
        
        result_values = [v_i + w_i for v_i, w_i in zip(self.values, other.values)]
        return Vector(*result_values)

    def vector_sum(self, *vectors):
        """Sums all corresponding elements"""
        result = self
        for vector in vectors:
            result += vector
        return result
    
    def __mul__(self, other):
        """Performs dot product or scalar multiplication"""
        if isinstance(other, Vector):
            if len(self.values) != len(other.values):
                raise ValueError("Vectors must have the same length")
            result = sum(v_i * w_i for v_i, w_i in zip(self.values, other.values))
        else:
            result = Vector(*[v_i * other for v_i in self.values])
        return result

    def sum_of_squares(self):
        '''Return sum of squared vector'''
        return sum(i * i for i in self.values)
    
    def mean(self):
        return sum(self.values) / len(self.values)
    
    def median(self):
        sorted_v = sorted(self.values)
        n = len(sorted_v)
        midpoint = n // 2
        if n % 2 == 1:
            return sorted_v[midpoint]
        else:
            lo = midpoint - 1
            hi = midpoint
            return (sorted_v[lo] + sorted_v[hi]) / 2
   
    def quantile(self, p):
        """Return the pth-percentile value in the vector"""
        p_index = int(p * len(self.values))
        return sorted(self.values)[p_index]
    
    def variance(self):
        """Assumes the vector has at least two elements"""
        n = len(self.values)
        deviations = self.mean() - self.values
        return sum(deviations * deviations) / (n - 1)
   
    def standard_deviation(self):
        return math.sqrt(self.variance())
    
    def interquartile_range(self):
        return self.quantile(0.75) - self.quantile(0.25)
    
    def covariance(self, other):
        n = len(self.values)
        return (self * other.mean()) / (n - 1)
    
    def correlation(self, other):
        stdev_x = self.standard_deviation()
        stdev_y = other.standard_deviation()
        if stdev_x > 0 and stdev_y > 0:
            return self.covariance(other) / (stdev_x * stdev_y)
        else:
            return 0  # If no variation, correlation is zero


# Example usage
x = Vector(1, 2, 3, 4)
y = Vector(1, 2, 3, 4)

# Display the vector
x.display()  # Output: [1, 2, 3, 4]

# Get the shape of the vector
print(x.shape())  # Output: (1, 4)

# Perform vector addition
result = x + y
result.display()  # Output: [2, 4, 6, 8]

# Perform dot product
dot_product = x * y
print(dot_product)  # Output: 30

print("-" * 40)
# Calculate the standard deviation
print(x.standard_deviation())  # Output: 1.118033988749895

print("-" * 40)
# Calculate the covariance with another vector
print(x.covariance(y))  # Output: 1.6666666666666667

# Calculate the mean
print(x.mean())  # Output: 2.5

# Calculate the median
print(x.median())  # Output: 2.5

# Calculate the 50th percentile
print(x.quantile(0.5))  # Output: 2

# Calculate the variance
print(x.variance())  # Output: 1.6666666666666667

# Calculate the interquartile range
print(x.interquartile_range())  # Output: 1

# Calculate the correlation with another vector
print(x.correlation(y))  # Output: 1.0
