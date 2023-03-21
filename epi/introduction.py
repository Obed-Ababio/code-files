"""
h-index: the largest number h such that a researcher has
published h papers that have been cited at least h times

"""
def h_index_1(publication_dict) -> int:
    """
    takes a dictionary mapping publications to 
    frequency of citation
    """
    publication_count = len(publication_dict.keys())
    
    for i in range(publication_count):
        citation_count = 0
        h_index = publication_count - i
        for pub in publication_dict.keys():
            if publication_dict[pub] >= h_index:
                citation_count = citation_count + 1
        if citation_count == h_index:
            return h_index

def h_index_2(publication_arr) -> int:
    """
    takes an array representing publication frequencies
    """
    publication_arr.sort()
    for i in range(len(publication_arr)):
        if publication_arr[i] >= len(publication_arr) - i:
            return len(publication_arr) - i


pub_dict_1 = {
    'A': 1,
    'B': 4,
    'C': 1,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 3,
    'H': 5,
    'I': 6,
}

pub_dict_2 = {
    1: 130,
    2: 85,
    3: 24,
    4: 15,
    5: 9,
    6: 4,
    7: 1
}

pub_arr = [1,4,1,4,2,1,3,5,6]
print(f"h_index: {h_index_1(pub_dict_2)}")
print(f"h_index_2: {h_index_2(list(pub_dict_2.values()))}")