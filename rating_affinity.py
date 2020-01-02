#!/usr/bin/env python

"""rating_affinity.py: computes the affinity between two rating files."""

__author__ = "DeVon Young Herr"


from math import sqrt


def parse(f: str, num_first: bool = True) -> dict:
    """
    Parses a file into a dictionary of entry-rating pairs.
    :param f: A str containing the name of the file.
    :param num_first: Are the lines of the file given by rating-entry or entry-rating?
    :return: A dictionary of entry-ratings.
    """
    ratings = {}

    if num_first:
        with open(f, "r") as f_in:
            for line in f_in:
                line = line.strip()
                found = False
                for index, char in enumerate(line):
                    # We assume the first and only the first space to delimit the rating from the entry.
                    if found:
                        continue
                    if char == " ":
                        # Break the string into the portion before and after the space and add into dictionary.
                        ratings[line[index + 1:]] = line[:index]
                        found = True

    else:
        with open(f, "r") as f_in:
            for line in f_in:
                line = line.strip()
                found = False
                for index, char in enumerate(line):
                    if found:
                        continue
                    if char == " ":
                        ratings[line[:index]] = line[index + 1:]
                        found = True

    return ratings


def clean(v: dict) -> dict:
    """
    Converts str values in a dictionary into floats and removes all pairs with non-numeric values.
    :param v: A dictionary.
    :return: v_p: A dictionary with all values as floats.
    """
    v_p = {}
    for key in v:
        try:
            # attempt to convert the string into a float and add into the dictionary
            v_p[key] = float(v[key])
        except ValueError:
            # perhaps it ends in a percent?
            try:
                v_p[key] = float(v[key][:-1])
            except ValueError:
                continue

    return v_p


def dot(v1: dict, v2: dict) -> float:
    """
    Computes the dot product of two vectors, assuming a component to be zero if the key is not in the dictionary.
    :param v1: A dictionary
    :param v2: A dictionary
    :return: The dot product of the two vectors
    """
    prod = 0.0
    for key in v1:
        if key in v2:
            prod += v1[key] * v2[key]

    return prod


def affinity(v1: dict, v2: dict) -> float:
    """
    Computes the measure of similarity between two vectors, given by the cosine of their inner angle.
    :param v1: A vector represented as a dictionary.
    :param v2: A vector represented as a dictionary.
    :return: The affinity of the two vectors.
    """
    n = dot(v1, v2)
    d = sqrt(dot(v1, v1) * dot(v2, v2))

    return n/d


def main(f1: str, f2: str) -> None:
    """
    Computes the affinity of two ratings vectors from .txt files.
    :param f1: The filename of a set of ratings.
    :param f2: The filename of a set of ratings.
    """
    v1 = clean(parse(f1))
    v2 = clean(parse(f2))

    print("The affinity is {:.4f}%.".format(affinity(v1, v2) * 100))


if __name__ == '__main__':
    main("rating1.txt", "rating2.txt")
