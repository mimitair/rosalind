# given:
# k = int()  # homozygous A
# h = int()  # heterozygous
# n = int()  # homozygous a
# return:
# proportion of two random ind to produce offspring with A


# This function calculates the proportion of dominant alleles out of all the alleles in the population
def proportion_dominant_alleles(k, h, n):
    total_alleles = (k + h + n) * 2  # Every individual carries two alleles
    dominant_alleles = k * 2 + h
    proportion = dominant_alleles / total_alleles
    return proportion

# This function calculates the proportion of recessive alleles out of all the alleles in the population
def proportion_recessive_alleles(k, h, n):
    total_alleles = (k + h + n) * 2  # Every individual carries two alleles
    recessive_alleles = n * 2 + h
    proportion = recessive_alleles / total_alleles
    return proportion

def probability_dominant_allele(k, h, n):
    t = k + h + n

    # Consider a decision tree with two steps:
    # 1. pick one individual that is AA, Aa or aa
    # 2. pick another individual (from a population that shrunk one individual) that is either AA, Aa or aa
    # If a dominant allele is passed in the pairing, multiply by the chance of finding that dominant allele
    # in the offspring
    prob_AA_aa = (k / t) * (n / (t-1))
    prob_AA_Aa = (k / t) * (h / (t-1))
    prob_AA_AA = (k / t) * ((k-1) / (t-1))

    prob_Aa_aa = (h / t) * (n / (t-1)) * 0.50  # 1 in 2 chance that Aa passes A
    prob_Aa_Aa = (h / t) * ((h-1) / (t-1)) * 0.75  # 3 in 4 chance to find A amongst offspring
    prob_Aa_AA = (h / t) * (k / (t-1))

    prob_aa_aa = (n / t) * ((n-1) / (t-1))
    prob_aa_Aa = (n / t) * (h / (t-1)) * 0.50  # 1 in 2 chance that Aa passes A
    prob_aa_AA = (n / t) * (k / (t-1))

    # Sum over all the probabilities where A is passed
    prob_dominant = prob_AA_aa + prob_AA_Aa + prob_AA_AA + prob_Aa_aa + prob_Aa_Aa + prob_Aa_AA + prob_aa_Aa + prob_aa_AA
    return prob_dominant
