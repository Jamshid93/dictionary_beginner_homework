def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    count_job=0
    for job in data:
        count_job+=1
    return count_job
print(count_jobs([{'name': 'John', 'job': 'Developer'}, {'name': 'Mary', 'job': 'Developer'}],"Developer"))