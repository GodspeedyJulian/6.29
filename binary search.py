def bi_search(list1,target):

    if len(list1)==0:

        missing_words.append(target)

        return missing_words

    else:

        mid=len(list1)//2

        if list1[mid]==target:

            return True

        else:

            if target<list1[mid]:

                return bi_search(list1[:mid],target)

            else:

                return bi_search(list1[mid+1:],target)
