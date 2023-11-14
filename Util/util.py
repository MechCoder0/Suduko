

class Util():

    @staticmethod
    def get_middle(left_position, right_position):
        return ((right_position - left_position)/2) + left_position
    
    @staticmethod
    def remove_text_from_list(list_of_strings, text_to_remove):
        list = []
        for l in list_of_strings:
            list.append(l.replace(text_to_remove, ""))
        return list