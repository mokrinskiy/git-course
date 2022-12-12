def duplicate_count(text):
    output_list = []
    total_list = set()
    count_list = []
    count = 1
    
    for i in text.lower():
        total_list.add(i)
        count_list.append(i)
        count += 1
        if count != len(count_list):
            output_list.append(i)

    print(output_list)

    return print(len(set(output_list)))

 
#duplicate_count("")
#duplicate_count("abcde")
#duplicate_count("abcdeaa")
#duplicate_count("abcdeaB")
duplicate_count("abacada")