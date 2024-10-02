# Pythagorean Triplets 🔺
This Python script generates exactly **10,000 Pythagorean triples** using a mathematical method that ensures all generated triples satisfy the equation: a² + b² = c².
 - Please note that it is almost completely useless.😁 This program is created because I was bored and wanted to make something funny lmao..


In a Pythagorean triple, `a`, `b`, and `c` represent the sides of a right-angled triangle, where `a` and `b` are the base and height and `c` is the hypotenuse. 

## How It Works 👷‍♂️

The script utilizes the following formula, based on two positive integers `m` and `n` (where `m > n`), to generate **primitive Pythagorean triples**:

- `a = m² - n²`
- `b = 2 * m * n`
- `c = m² + n²`

To ensure that `a`, `b`, and `c` form a valid Pythagorean triple, `m` and `n` must meet the following conditions:
1. `m > n`
2. `m` and `n` are coprime (i.e., their greatest common divisor is 1), and one of them is even.

After generating a **primitive triple**, the script produces **non-primitive triples** by multiplying the primitive triple by integer values `k`. This helps ensure that we generate enough triples to reach the goal of **10,000**.

### Code Flow ⏳

1. **Triple Generation**:
   - The script starts with `m = 2` and increases `m` while iterating over valid values of `n` such that `m > n`.
   - It checks if `m` and `n` are coprime and that one of them is even before generating a valid triple.
   
2. **Primitive and Non-Primitive Triples**:
   - For each valid pair `(m, n)`, the primitive triple is computed using the formula above.
   - The script then generates multiples of the primitive triple (non-primitive triples) until the list contains exactly **10,000** triples.

3. **Output**:
   - Once the script reaches **10,000** triples, it prints the results to the console. You can also limit the number of printed triples to a smaller number for easier viewing.

### Installation
To run the script and generate **10,000** Pythagorean triples, simply execute it in your Python environment:

## Installation 💻

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Saharsh000/Pythagorean_Triple_Generator.git
   cd Pythagorean_Triple_Generator
   ```

2. **Run the Program**:   
```bash
python code.py
```

### Customization
If you'd like to print a subset of the triples (for example, the first 10 triples), you can modify the print loop like this:
```bash
for triple in pythagorean_triples[:10]:
    print(triple)
```

# Thank You 😄
- Well, thank you for reading.
- As always, if you have any issues with the program, you can contact me on discord(metagross2010ss) or email me.
- If you have liked this, please star the repo!! ⭐
- Have a nice day :D !!!! 👋





