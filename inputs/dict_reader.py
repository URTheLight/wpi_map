import sys
import math

def read_dict(s):
    entry = s.split()
    entry[1:] = [' '.join(entry[1:])]
    return entry

def read_z(s):
    country = s.split()
    z = float(country.pop(-1))
    country[0:] = [' '.join(country[0:])]
    country.append(z)
    return country

def translate(d, c):
    translated = []
    for country in c:
        for item in d:
            if country[0] == item[1]:
                country[0] = item[0]
                translated.append(country)
    return translated

def adjust(s, m):
    adjusted_num = int(100 * (s[1] - m))
    s.append(adjusted_num)
    return s

def print_this(w, name):
    w.write(name[0] + ": {wpi: " + str(name[1]) + ", heatIndex: " + str(name[2]) + "},\n")

def create_dict(r, w):
    country_dict = []
    countries = []
    for i in range(245):
        s = r.readline()
        e = read_dict(s)
        country_dict.append(e)
    for i in range(192):
        s = r.readline()
        c = read_z(s)
        countries.append(c)
    translated_countries = translate(country_dict, countries)
    for country in translated_countries:
        adjusted_num = int(100 * (country[1] - 0))
        country.append(adjusted_num)
        print_this(w, country)

if __name__ == "__main__":
    create_dict(sys.stdin, sys.stdout)