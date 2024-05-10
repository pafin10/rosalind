from math import comb


def calculate_offspring(generations, minAaBb_organisms):

    offspring_count = 2**generations

    # These correspond, in order, to the genotypes AA, Aa, aa or BB, Bb, bb
    # genotype_expected_probabilites:  = [1/4, 1/2, 1/4]

    # the first generation is based on mating of Aa with Aa, leading to a distribution of 1/4 AA, 1/2 Aa and 1/4 aa.
    # in the next generation, the process is exactly the same for the Aa genotype, whose carrier mates with Aa again.
    # For AA and aa, the respective carriers mate with Aa as well. In total, this leads to the same distribution,
    # which stays true over all generations. The same applies for the B - genes, and as they are independent we can
    # treat them separately. Thus, the following:

    # look at case with none AaBb separately, as it would render the result 0 for i == 0 below.
    prob_no_AaBb = (3/4)**offspring_count

    # the probability to have equal or more than X AaBb organisms in generation k is equal to 1-P(less than X)
    # we need to use the binomial coefficient to account for all the different options to choose i AaBb out of
    # offspring_count. If we disregarded this, we would basically assume that there is only one way to choose i AaBb
    # organisms out of offspring_count.
    prob_less_than_X = sum([(1/4)**i * (3/4) ** (offspring_count - i) * comb(offspring_count, i) for i in range(1, minAaBb_organisms)]) + prob_no_AaBb

    return round(1 - prob_less_than_X, ndigits=3)


if __name__ == '__main__':
    print(calculate_offspring(5, 9))
