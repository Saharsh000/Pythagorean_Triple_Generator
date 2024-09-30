import math

#gpt is just Generating Pythagorean Triples
def gpt(limit):
    triples = []
    m = 2

    # Loop until we have exactly 100000 triples.
    while len(triples) < limit:
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:  # Ensure m > n, co-prime, and one is even.
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                k = 1
                # Generate multiples of the primitive triples
                while len(triples) < limit:
                    triples.append((k*a, k*b, k*c))
                    k += 1
        m += 1
    
    return triples[:limit]  # Return only the first 'limit' triples

# Generate 100,000 Pythagorean triples
pythagorean_triples = gpt(100000)

# Verify the number of triples generated
print(f"Number of Pythagorean triples generated: {len(pythagorean_triples)}")

for triple in pythagorean_triples:
    print(f"{triple[0]}, {triple[1]}, {triple[2]}")

#It may not generate all 100k triplets but atleast 10k

