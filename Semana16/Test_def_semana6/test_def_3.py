from def_3 import sum_list 


def test_of_sum_list(): 
    #Arrange 
    list_input = [4, 6, 2, 29]
    expend = [41]
    #Act
    result = sum_list([4, 6, 2, 29])
    #Assert 
    assert result == 41 
    