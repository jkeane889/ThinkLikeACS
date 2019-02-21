def drop_first_last(grades):

#take the first item and store in "first" variable, take all items in the middle (no matter how many you have) and store in the middle, and then store the last in the final variable
# "*" star expression gives you more flexibility in assigning variables in a list

    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([76,65,95,45,21])