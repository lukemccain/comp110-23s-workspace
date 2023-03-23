def stink(inp_list: dict[str, int]) -> list[int]:
    """Returns list of numbers from dict that are even and less than 11."""
    ret_list: list[int] = []
    for key in inp_list:
        if inp_list[key] % 2 == 0 and inp_list[key] < 11:
            ret_list.append(inp_list[key])
        return ret_list
    
print(stink({"vanilla":8 ,"chocolate":10 }))